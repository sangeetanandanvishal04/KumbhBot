import 'package:flutter/material.dart';

const Color kPrimaryColor = Color(0xFF345F84);
const Color kSecondaryColor = Color(0xFF6789CA);
const Color kTextBlackColor = Color(0xFF313131);
const Color kTextWhiteColor = Color(0xFFFFFFFF);
const Color kContainerColor = Color(0xFF777777);
const Color kOtherColor = Color(0xFFF6F6F7);
const Color kTextLightColor = Color(0xFFA5A5A5);
const Color kErrorBorderColor = Color(0xFFE74C3C);

const sizedBox = SizedBox(
    height: kDefaultPadding,
);

const kWidthSizedBox = SizedBox(
    width: kDefaultPadding,
);

const kHalfSizedBox = SizedBox(
    height: kDefaultPadding / 2,
);

const kHalfWidthSizedBox = SizedBox(
    width: kDefaultPadding / 2,
);

const kDefaultPadding = 20.0;

const kTopBorderRadius = BorderRadius.only(
    topLeft: Radius.circular(kDefaultPadding),
    topRight: Radius.circular(kDefaultPadding),
);

const baseURL = 'http://127.0.0.1:8000/';
String verifiedEmail = '';

String accessVerificationToken = '';

const String mobilePattern = r'(^(?:[+0]9)?[0-9]{10,12}$)';

const String emailPattern = r'^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$';