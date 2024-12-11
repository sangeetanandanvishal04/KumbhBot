import 'package:kumbh_mela_chatbot/constants.dart';
import 'package:flutter/material.dart';
import 'package:flutter_svg/svg.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:kumbh_mela_chatbot/screens/forgetpassword_screen/new_password_screen.dart';

class OTPVerificationPage extends StatefulWidget {
  static String routeName = 'OTPVerificationScreen';

  const OTPVerificationPage({super.key});

  @override
  _OTPVerificationPageState createState() => _OTPVerificationPageState();
}

class _OTPVerificationPageState extends State<OTPVerificationPage> {
  late final List<String> _otpDigits = List.filled(4, '');

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        automaticallyImplyLeading: true,
        leading: IconButton(
          icon: const Icon(Icons.arrow_back),
          color: kOtherColor,
          onPressed: () => Navigator.pop(context, false),
        ),
      ),
      resizeToAvoidBottomInset: false,
      backgroundColor: kPrimaryColor,
      body: Container(
        color: kOtherColor,
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: 24, horizontal: 32),
          child: Column(
            children: [
              SvgPicture.asset(
                'assets/icons/change-password-icon.svg',
                height: 80.0,
                width: 80.0,
                color: kPrimaryColor,
              ),
              sizedBox,
              const Text(
                'Verification',
                style: TextStyle(
                  fontSize: 22,
                  fontWeight: FontWeight.bold,
                ),
              ),
              sizedBox,
              const Text(
                "Enter OTP sent to your email",
                style: TextStyle(
                  fontSize: 14,
                  fontWeight: FontWeight.bold,
                  color: kTextBlackColor,
                ),
                textAlign: TextAlign.center,
              ),
              sizedBox,
              Container(
                padding: const EdgeInsets.all(kDefaultPadding),
                decoration: BoxDecoration(
                  color: kTextWhiteColor,
                  borderRadius: BorderRadius.circular(kDefaultPadding / 2),
                ),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: List.generate(4, (index) => _textFieldOTP(index: index)),
                ),
              ),
              sizedBox,
              Container(
                height: 60,
                alignment: Alignment.centerLeft,
                decoration: const BoxDecoration(
                  gradient: LinearGradient(
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                    stops: [0.3, 1],
                    colors: [
                      kSecondaryColor,
                      kPrimaryColor,
                    ],
                  ),
                  borderRadius: BorderRadius.all(
                    Radius.circular(5),
                  ),
                ),
                child: SizedBox.expand(
                  child: TextButton(
                    child: const Text(
                      "Verify OTP",
                      style: TextStyle(
                        fontWeight: FontWeight.bold,
                        color: kTextWhiteColor,
                        fontSize: 20,
                      ),
                      textAlign: TextAlign.center,
                    ),
                    onPressed: () {
                      _performOTPVerification();
                    },
                  ),
                ),
              ),
              sizedBox,
              const Text(
                "Didn't receive OTP?",
                style: TextStyle(
                  fontSize: 14,
                  fontWeight: FontWeight.bold,
                  color: kTextBlackColor,
                ),
                textAlign: TextAlign.center,
              ),
              sizedBox,
              GestureDetector(
                onTap: () {
                  _resendOTP();
                },
                child: const Text(
                  "Resend OTP Again",
                  style: TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                    color: kPrimaryColor,
                  ),
                  textAlign: TextAlign.center,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _textFieldOTP({required int index}) {
    return SizedBox(
      width: 60,
      child: TextField(
        onChanged: (value) {
          _otpDigits[index] = value;
        },
        maxLength: 1,
        textAlign: TextAlign.center,
        keyboardType: TextInputType.number,
        style: const TextStyle(
            color: kSecondaryColor, fontSize: 24, fontWeight: FontWeight.bold),
        decoration: const InputDecoration(
          counter: Offstage(),
          border: OutlineInputBorder(
            borderSide: BorderSide(width: 2, color: kTextBlackColor),
          ),
          focusedBorder: OutlineInputBorder(
            borderSide: BorderSide(width: 2, color: kPrimaryColor),
          ),
        ),
      ),
    );
  }

  void _performOTPVerification() async {
    try {
      final otp = _otpDigits.join('');
      final response = await http.post(
        Uri.parse('${baseURL}otp-verification'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          'email': verifiedEmail,
          'otp': otp,
        }),
      );

      if(response.statusCode == 200){
        Navigator.pushNamed(context, CreateNewPasswordScreen.routeName);
      }
      else {
        _showErrorSnackBar(context, 'Invalid OTP');
      }
    }
    catch (e) {
      _showErrorSnackBar(context, 'No Internet Connection');
    }
  }

  void _resendOTP() async {
    try {
      await http.post(
        Uri.parse('${baseURL}forgot-password/$verifiedEmail'),
        headers: {'Content-Type': 'application/json'},
      );
    }
    catch (e) {
      _showErrorSnackBar(context, 'No Internet Connection');
    }
  }

  void _showErrorSnackBar(BuildContext context, String message) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(message),
        backgroundColor: Colors.red,
      ),
    );
  }
}
