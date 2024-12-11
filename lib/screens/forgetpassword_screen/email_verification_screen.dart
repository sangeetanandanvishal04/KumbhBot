import 'package:chatbot/constants.dart';
import 'package:chatbot/screens/forgetpassword_screen/otp_verification_page.dart';
import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:http/http.dart' as http;

class EmailVerificationPage extends StatefulWidget {
  static String routeName = 'ForgetPasswordScreen';

  const EmailVerificationPage({super.key});

  @override
  _EmailVerificationPageState createState() => _EmailVerificationPageState();
}

class _EmailVerificationPageState extends State<EmailVerificationPage> {
  final _formKey = GlobalKey<FormState>();
  String? _email;

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
      body: Container(
        padding: const EdgeInsets.only(top: 60, left: 40, right: 40),
        color: kOtherColor,
        child: Form(
          key: _formKey,
          child: ListView(
            children: <Widget>[
              Column(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: <Widget>[
                  Column(
                    children: <Widget>[
                      SizedBox(
                        width: 200,
                        height: 200,
                        child: SvgPicture.asset(
                          'assets/icons/change-password-icon.svg',
                          height: 40.0,
                          width: 40.0,
                          color: kPrimaryColor,
                        ),
                      ),
                      sizedBox,
                      const Text(
                        "Forget Password?",
                        style: TextStyle(
                          fontSize: 36,
                          color: kTextBlackColor,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      sizedBox,
                      const Text(
                        "Enter the email address associated to your account.",
                        style: TextStyle(
                          fontSize: 18,
                          color: kTextBlackColor,
                          fontWeight: FontWeight.normal,
                        ),
                      ),
                      sizedBox,
                    ],
                  ),
                  SizedBox(
                    width: double.infinity,
                    child: Column(
                      children: <Widget>[
                        TextFormField(
                          textAlign: TextAlign.start,
                          keyboardType: TextInputType.emailAddress,
                          style: Theme.of(context)
                              .textTheme
                              .titleSmall!
                              .copyWith(color: kTextBlackColor),
                          decoration: const InputDecoration(
                            labelText: "Email",
                            floatingLabelBehavior: FloatingLabelBehavior.always,
                            isDense: true,
                          ),
                          validator: (value) {
                            if (value == null || value.isEmpty) {
                              return 'Please Enter Some Text';
                            }
                            RegExp regExp = RegExp(emailPattern);
                            if (!regExp.hasMatch(value)) {
                              return 'Please Enter a valid Email Address';
                            }
                            return null;
                          },
                          onSaved: (value) {
                            _email = value;
                          },
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
                                "Send OTP",
                                style: TextStyle(
                                  fontWeight: FontWeight.bold,
                                  color: kTextWhiteColor,
                                  fontSize: 20,
                                ),
                                textAlign: TextAlign.center,
                              ),
                              onPressed: () {
                                if (_formKey.currentState!.validate()) {
                                  _formKey.currentState!.save();
                                  _performEmailVerification(context, _email!);
                                }
                              },
                            ),
                          ),
                        ),
                        sizedBox,
                      ],
                    ),
                  )
                ],
              )
            ],
          ),
        ),
      ),
    );
  }
}

void _performEmailVerification(BuildContext context, String email) async {
  try {
    final response = await http.post(
      Uri.parse('${baseURL}forgot-password/$email'),
      headers: {'Content-Type': 'application/json'},
    );

    if (response.statusCode == 200) {
      verifiedEmail = email;
      Navigator.pushNamed(
        context,
        OTPVerificationPage.routeName,
      );
    } else {
      _showErrorSnackBar(context, 'Invalid Email Address');
    }
  } catch (e) {
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
