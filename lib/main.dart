import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:kumbh_mela_chatbot/screens/splash_screen/splash_screen.dart';
import 'constants.dart';
import 'package:kumbh_mela_chatbot/routes.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'MahaKumbh: Journey Helper',
      theme: ThemeData(
        scaffoldBackgroundColor: kPrimaryColor,
        primaryColor: kPrimaryColor,
        appBarTheme: const AppBarTheme(
          color: kPrimaryColor,
          elevation: 0,
        ),
        textTheme: GoogleFonts.sourceSans3TextTheme(
          Theme.of(context).textTheme.apply(
                bodyColor: kTextWhiteColor,
                displayColor: kTextWhiteColor,
              ),
        ),
        inputDecorationTheme: const InputDecorationTheme(
          labelStyle: TextStyle(
            fontSize: 15.0,
            color: kTextLightColor,
          ),
          hintStyle: TextStyle(
            fontSize: 16.0,
            color: kTextBlackColor,
          ),
        ),
      ),
      initialRoute: SplashScreen.routeName,
      routes: routes,
    );
  }
}