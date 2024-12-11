import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:speech_to_text/speech_to_text.dart' as stt;
import 'package:kumbh_mela_chatbot/constants.dart';

class BotScreen extends StatefulWidget {
  static const String routeName = "BotScreen";

  const BotScreen({super.key});

  @override
  _BotScreenState createState() => _BotScreenState();
}

class _BotScreenState extends State<BotScreen> {
  final TextEditingController _controller = TextEditingController();
  final List<Map<String, String>> _messages = [];
  late stt.SpeechToText _speech;
  bool _isListening = false;

  @override
  void initState() {
    super.initState();
    _speech = stt.SpeechToText();
  }

  Future<void> _sendMessage(String message) async {
    setState(() {
      _messages.add({'type': 'user', 'text': message});
    });

    try {
      final response = await http.get(
        Uri.parse("http://127.0.0.1:8000/ask?user_query=$message"),
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer $accessVerificationToken',
        },
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(utf8.decode(response.bodyBytes)); // Decode for UTF-8
        _handleChatbotResponse(data);
      } else {
        setState(() {
          _messages.add({
            'type': 'error',
            'text': "Oops! Something went wrong. Please try again later."
          });
        });
      }
    } catch (e) {
      setState(() {
        _messages.add({
          'type': 'error',
          'text': "Failed to connect to the server. Please check your internet connection."
        });
      });
    }
  }

  void _handleChatbotResponse(Map<String, dynamic> data) {
    if (data['status'] == 'success') {
      setState(() {
        _messages.add({'type': 'bot', 'text': data['output']});
        if (data['Tips'] != null) {
          _messages.add({'type': 'bot', 'text': "Tips: ${data['Tips']}"});}
        if (data['Suggestions'] != null) {
          _messages.add({'type': 'suggestion', 'text': data['Suggestions']});}
      });
    } else {
      setState(() {
        _messages.add({
          'type': 'error',
          'text': "Could not process your request. Please try again."
        });
      });
    }
  }

  Future<void> _startListening() async {
    if (!_isListening) {
      bool available = await _speech.initialize(
        onStatus: (val) {},
        onError: (val) {},
      );
      if (available) {
        setState(() => _isListening = true);
        _speech.listen(
          onResult: (val) {
            setState(() {
              _controller.text = val.recognizedWords; // Update input field with recognized text
              if (val.finalResult) {
                _isListening = false;
              }
            });
          },
        );
      }
    } else {
      setState(() => _isListening = false);
      _speech.stop();
    }
  }

  void _onSubmit() {
    final message = _controller.text.trim();
    if (message.isNotEmpty) {
      _sendMessage(message);
      _controller.clear();
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Kumbh Mela Bot'),
        backgroundColor: Colors.deepPurpleAccent,
        actions: [
          IconButton(
            icon: Icon(
              _isListening ? Icons.mic : Icons.mic_none,
              color: Colors.white,
            ),
            onPressed: _startListening,
          ),
        ],
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              padding: const EdgeInsets.symmetric(horizontal: 8.0),
              itemCount: _messages.length,
              itemBuilder: (context, index) {
                final message = _messages[index];
                bool isUserMessage = message['type'] == 'user';

                return Align(
                  alignment: isUserMessage
                      ? Alignment.centerRight
                      : Alignment.centerLeft,
                  child: Container(
                    margin: const EdgeInsets.symmetric(vertical: 4.0),
                    padding: const EdgeInsets.all(12.0),
                    constraints: const BoxConstraints(maxWidth: 250),
                    decoration: BoxDecoration(
                      color: isUserMessage
                          ? Colors.deepPurpleAccent
                          : Colors.grey[200],
                      borderRadius: BorderRadius.circular(12).copyWith(
                        topLeft: isUserMessage ? const Radius.circular(12) : Radius.zero,
                        topRight: isUserMessage ? Radius.zero : const Radius.circular(12),
                      ),
                    ),
                    child: Text(
                      message['text']!,
                      style: GoogleFonts.notoSans(
                        textStyle: TextStyle(
                          color: isUserMessage ? Colors.white : Colors.black87,
                          fontSize: 16.0,
                        ),
                      ),
                    ),
                  ),
                );
              },
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(10.0),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _controller,
                    onSubmitted: (_) => _onSubmit(),
                    style: GoogleFonts.notoSans(
                      textStyle: const TextStyle(color: Colors.black),
                    ),
                    decoration: InputDecoration(
                      hintText: 'Type a message...',
                      hintStyle: GoogleFonts.notoSans(
                          textStyle: const TextStyle(color: Colors.black54)),
                      filled: true,
                      fillColor: Colors.grey[200],
                      contentPadding:
                      const EdgeInsets.symmetric(vertical: 10.0, horizontal: 15.0),
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(30.0),
                        borderSide: BorderSide.none,
                      ),
                    ),
                  ),
                ),
                const SizedBox(width: 10),
                FloatingActionButton(
                  onPressed: _onSubmit,
                  backgroundColor: Colors.deepPurpleAccent,
                  child: const Icon(Icons.send, color: Colors.white),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
