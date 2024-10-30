from fastapi import FastAPI, status, HTTPException, Depends, BackgroundTasks, Request
from .database import get_db, engine
from sqlalchemy.orm import Session
from . import schemas, tablesmodel, utils, oAuth2
from fastapi.middleware.cors import CORSMiddleware
import difflib
from typing import Optional

app = FastAPI()

#origins = ["www.youtube.com", "www.google.com"]
origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tablesmodel.Base.metadata.create_all(bind = engine)

@app.get("/")
def root():
    return {"message" : "Welcome to my API...."}

""" {
    "email": "email@iiita.ac.in",
    "password": "password"
} """
@app.post("/signup", response_model=schemas.UserOut)
async def create_user(user:schemas.UserCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    
    user_found = db.query(tablesmodel.User).filter(tablesmodel.User.email==user.email).first()

    if user_found:
       raise HTTPException(status_code=status.HTTP_302_FOUND, detail="Email already exists")
    
    hashed_password = utils.hash(user.password)
    new_user = tablesmodel.User(email=user.email, password=hashed_password, role=user.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    background_tasks.add_task(utils.send_signup_email, user.email)
    return new_user   

""" {
    "email": "email@iiita.ac.in",
    "password": "password"
} """
@app.post("/login")
async def login_user(user_credentials:schemas.UserLogin ,db: Session = Depends(get_db)):

    user = db.query(tablesmodel.User).filter(tablesmodel.User.email==user_credentials.email).first()

    if not user:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    access_token = oAuth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "Bearer"}

#http://127.0.0.1:8000/forgot-password/email@iiita.ac.in
@app.post("/forgot-password/{email}")
async def forgot_password(email: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    user = db.query(tablesmodel.User).filter(tablesmodel.User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with this email does not exist")

    otp = utils.generate_otp()
    db_otp = tablesmodel.OTP(email=email, otp=otp)
    db.add(db_otp)
    db.commit()
    background_tasks.add_task(utils.send_otp_email, user.email, otp)

    return {"message": "OTP sent successfully"}

@app.post("/resend-otp/{email}")
async def resend_otp(email: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    user = db.query(tablesmodel.User).filter(tablesmodel.User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with this email does not exist")

    db.query(tablesmodel.OTP).filter(tablesmodel.OTP.email==email).delete(synchronize_session=False)
    db.commit()

    otp = utils.generate_otp()

    db_otp = tablesmodel.OTP(email=email, otp=otp)
    db.add(db_otp)
    db.commit()
    background_tasks.add_task(utils.send_otp_email, user.email, otp)

    return {"message": "OTP resend successfully"}

""" {
    "email": "email@iiita.ac.in",
    "otp": "5294"
} """
@app.post("/otp-verification")
async def reset_password(otp_data: schemas.OTP, db: Session = Depends(get_db)):
    user = db.query(tablesmodel.User).filter(tablesmodel.User.email == otp_data.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email not found")

    otp_record = db.query(tablesmodel.OTP).filter(tablesmodel.OTP.email == otp_data.email).first()
    if not otp_record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OTP not found")
    
    if otp_data.otp != otp_record.otp:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid OTP")
    
    db.delete(otp_record)
    db.commit()

    return {"message": "OTP is correct"}

""" {
    "email": "email@iiita.ac.in",
    "new_password": "password",
    "confirm_password": "password"
} """
@app.post("/reset-password")
async def reset_password(password_data: schemas.PasswordReset, db: Session = Depends(get_db)):
    user = db.query(tablesmodel.User).filter(tablesmodel.User.email == password_data.email).first()

    if password_data.new_password != password_data.confirm_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New password and confirm password do not match")

    hashed_password = utils.hash(password_data.new_password)
    user.password = hashed_password

    db.commit()
    return {"message": "Password reset successfully"}