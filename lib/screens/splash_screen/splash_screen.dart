import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:kumbh_mela_chatbot/constants.dart';
import 'package:kumbh_mela_chatbot/screens/login_screen/login_screen.dart';

class SplashScreen extends StatelessWidget {
  static String routeName = 'SplashScreen';

  const SplashScreen({super.key});

  @override
  Widget build(BuildContext context) {
    Future.delayed(
      const Duration(seconds: 5),
      () {
        Navigator.pushNamedAndRemoveUntil(context, LoginScreen.routeName, (route) => false);
      },
    );

    return Scaffold(
      body: Center(
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceAround,
          children: <Widget>[
            Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(
                  'KumbhBot',
                  style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                        color: kTextWhiteColor,
                        fontSize: 50.0,
                        fontStyle: FontStyle.italic,
                        letterSpacing: 3.0,
                      ),
                ),
                Text(
                  'Smart Journey',
                  style: GoogleFonts.pattaya(
                    fontSize: 50.0,
                    fontStyle: FontStyle.italic,
                    color: kTextWhiteColor,
                    letterSpacing: 3.0,
                    fontWeight: FontWeight.w700,
                  ),
                ),
              ],
            ),
            Image.asset(
              'assets/images/splash.jpeg',
              height: 150.0,
              width: 150.0,
            ),
          ],
        ),
      ),
    );
  }
}
