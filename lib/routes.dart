import 'package:flutter/cupertino.dart';
import 'package:kumbh_mela_chatbot/screens/chatbot_screen/chatbot_screen.dart';
import 'package:kumbh_mela_chatbot/screens/forgetpassword_screen/email_verification_screen.dart';
import 'package:kumbh_mela_chatbot/screens/forgetpassword_screen/new_password_screen.dart';
import 'package:kumbh_mela_chatbot/screens/forgetpassword_screen/otp_verification_page.dart';
import 'package:kumbh_mela_chatbot/screens/login_screen/login_screen.dart';
import 'package:kumbh_mela_chatbot/screens/signup_screen/signup_screen.dart';
import 'package:kumbh_mela_chatbot/screens/splash_screen/splash_screen.dart';

Map<String, WidgetBuilder> routes = {
  SplashScreen.routeName : (context) => const SplashScreen(),
  LoginScreen.routeName : (context) => const LoginScreen(),
  BotScreen.routeName : (context) => BotScreen(),
  EmailVerificationPage.routeName : (context) => const EmailVerificationPage(),
  OTPVerificationPage.routeName : (context) => const OTPVerificationPage(),
  CreateNewPasswordScreen.routeName : (context) => const CreateNewPasswordScreen(),
  SignupScreen.routeName: (context) => const SignupScreen()
};