import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:chatbot/components/custom_buttons.dart';
import 'package:chatbot/constants.dart';
import 'package:chatbot/screens/chatbot_screen/chatbot_screen.dart';
import 'package:chatbot/screens/login_screen/login_screen.dart';

late bool _passwordVisible;

class SignupScreen extends StatefulWidget {
  static String routeName = 'SignupScreen';

  const SignupScreen({super.key});

  @override
  State<SignupScreen> createState() => _SignupScreenState();
}

class _SignupScreenState extends State<SignupScreen> {
  final _formKey = GlobalKey<FormState>();
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

  @override
  void initState() {
    super.initState();
    _passwordVisible = true;
  }

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
      body: GestureDetector(
        onTap: () => FocusManager.instance.primaryFocus?.unfocus(),
        child: Scaffold(
          body: ListView(
            children: <Widget>[
              SizedBox(
                width: MediaQuery.of(context).size.width,
                height: MediaQuery.of(context).size.height / 2.8,
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Image.asset(
                      'assets/images/splash.jpeg',
                      height: 150.0,
                      width: 150.0,
                    ),
                    const SizedBox(
                      height: kDefaultPadding / 2,
                    ),
                    const Text(
                      'SIGN UP',
                      style: TextStyle(
                        color: kTextWhiteColor,
                        fontWeight: FontWeight.normal,
                        fontSize: 35.0,
                      ),
                    ),
                    const SizedBox(
                      height: kDefaultPadding / 6,
                    ),
                  ],
                ),
              ),
              Container(
                width: MediaQuery.of(context).size.width,
                height: MediaQuery.of(context).size.height,
                decoration: const BoxDecoration(
                  borderRadius: BorderRadius.only(
                    topLeft: Radius.circular(kDefaultPadding * 3),
                    topRight: Radius.circular(kDefaultPadding * 3),
                  ),
                  color: kOtherColor,
                ),
                child: Padding(
                  padding: const EdgeInsets.all(kDefaultPadding),
                  child: Column(
                    children: [
                      Form(
                        key: _formKey,
                        child: Column(
                          children: [
                            sizedBox,
                            buildEmailField(),
                            sizedBox,
                            buildPasswordField(),
                            sizedBox,
                            DefaultButton(
                              onPress: () async {
                                if (_formKey.currentState!.validate()) {
                                  _performSignup(context);
                                }
                              },
                              title: 'SIGN UP',
                              iconData: Icons.arrow_forward_outlined,
                            ),
                            const SizedBox(height: kDefaultPadding),
                            GestureDetector(
                              onTap: () {
                                Navigator.pushNamed(
                                    context, LoginScreen.routeName);
                              },
                              child: const Align(
                                alignment: Alignment.center,
                                child: Text(
                                  'Already have an account? Sign In',
                                  style: TextStyle(
                                    fontSize: 16.0,
                                    color: kPrimaryColor,
                                  ),
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  TextFormField buildEmailField() {
    return TextFormField(
      controller: _emailController,
      textAlign: TextAlign.start,
      keyboardType: TextInputType.emailAddress,
      style: Theme.of(context)
          .textTheme
          .titleSmall!
          .copyWith(color: kTextBlackColor),
      decoration: const InputDecoration(
        labelText: 'Email Address',
        floatingLabelBehavior: FloatingLabelBehavior.always,
        isDense: true,
      ),
      validator: (value) {
        RegExp regExp = RegExp(emailPattern);
        if (value == null || value.isEmpty) {
          return 'Please Enter Some Text';
        } else if (!regExp.hasMatch(value)) {
          return 'Please Enter a valid Email Address';
        }
      },
    );
  }

  TextFormField buildPasswordField() {
    return TextFormField(
      controller: _passwordController,
      obscureText: _passwordVisible,
      textAlign: TextAlign.start,
      keyboardType: TextInputType.visiblePassword,
      style: Theme.of(context)
          .textTheme
          .titleSmall!
          .copyWith(color: kTextBlackColor),
      decoration: InputDecoration(
        labelText: 'Password',
        floatingLabelBehavior: FloatingLabelBehavior.always,
        isDense: true,
        suffixIcon: IconButton(
          onPressed: () {
            setState(() {
              _passwordVisible = !_passwordVisible;
            });
          },
          icon: Icon(
            _passwordVisible ? Icons.visibility : Icons.visibility_off,
          ),
        ),
      ),
      validator: (value) {
        if (value!.length < 6) {
          return 'Must be more than 6 characters';
        }
      },
    );
  }

  void _performSignup(BuildContext context) async {
    final String email = _emailController.text.trim();
    final String password = _passwordController.text.trim();

    try {
      final response = await http.post(
        Uri.parse('${baseURL}signup'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          'email': email,
          'password': password,
        }),
      );

      if (response.statusCode == 200) {
        Navigator.pushNamedAndRemoveUntil(
            context, LoginScreen.routeName, (route) => false);
      } else {
        _showErrorSnackBar(context, 'Signup Failed');
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
}