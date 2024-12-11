## Problem Statement: Maha Kumbh Mela 2025 ChatBot using Flutter(dart), FastAPI(Python) and PostgreSQL database.

## Introduction:
Welcome to my project! This ReadME will guide you through the setup and usage of this application.

## Technologies Used:
Frontend: Flutter(dart)
Backend: FastAPI(Python)
Database: PostgreSQL

## Installation
Follow these steps to set up and run the project in your local environment:

## Prerequisites
- Android Studio installed on your machine.
- Flutter SDK installed on your machine.
- VS Code installed on your machine.
- Python 3.12.2 installed on your machine.
- Git installed on your machine.
- PostgreSQL installed on your machine.

## 1. Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/sangeetanandanvishal04/KumbhBot.git

### Installation steps of backend in VS Code editor:
### 2. Create and Activate a Virtual Environment
Open Command prompt inside your VS Code editor:
Create the virtual environment: python3 -m venv venv
Activate the virtual environment:
---For Windows: venv\Scripts\activate
---For macOS and Linux:source venv/bin/activate

### 3.Install Dependencies
Once the virtual environment is activated, install the required Python dependencies from
the requirements.txt file:  pip install -r requirements.txt

### 4. Set Up the PostgreSQL Database
Create a PostgreSQL database for the project and then create ".env" file and update these
required values to connect with the PostgreSQL database.

    DATABASE_HOSTNAME = localhost,
    DATABASE_PORT = 5432,
    DATABASE_PASSWORD = "YOUR_DATABASE_PASSWORD",
    DATABASE_NAME = "YOUR_DATABASE_NAME",
    DATABASE_USERNAME = "YOUR_DATABASE_USERNAME",
    SECRET_KEY = 09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
    ALGORITHM = HS256
    ACCESS_TOKEN_EXPIRE_MINUTES = 300

### 5. Set Up values of SMTP Email and Password:
    EMAIL = "YOUR_EMAIL"
    SMTP_PASSWORD = "YOUR_SMTP_PASSWORD"

    Steps to get SMTP Password:
    --- Open Google Chrome: Launch the Chrome browser on your computer or device.
    --- Go to your Google Account settings: Click on your profile picture or initials in the top right 
        corner of the Chrome window. From the dropdown menu, select "Manage your Google Account."
    --- Navigate to "Security" settings: In your Google Account settings, find and click on the 
        "Security" tab on the left-hand side menu. This is where you manage security-related settings for 
        your Google Account.
    --- Find the section for "Signing in to other sites" or "Third-party app access": Look for a section 
        related to signing in to other sites or granting access to third-party applications. This is 
        where you'll manage access to your Gmail account for your Python script.
    --- Generate an app password if necessary: If you have two-step verification enabled for your Google 
        Account, you may need to generate an app password specifically for your Python script. Look for 
        an option to generate an app password and follow the instructions to create one. Make sure to 
        copy this password as you'll need it in your Python script.
    --- Now, Update SMTP_PASSWORD in ".env" file.

### Installation steps of frontend in Android studio:
Check out at the link given below for the frontend code and its proper setup:
- https://github.com/sangeetanandanvishal04/KumbhBot.git

### 9. Run the Application:
    First, Run the FastAPI Server using command prompt in VS Code: uvicorn FastAPI.main:app --reload
    After successfull run of FastAPI Server, run front-end of the Application inside Android studio."