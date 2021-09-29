import 'dart:async';
import 'dart:developer';

import 'package:flutter/material.dart';
import 'api/compaign.dart';

void main() {
  runApp(MyApp());
}

// ignore: must_be_immutable
class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  var primary = 0x009688;
  var darkPrimary = 0x00796B;
  var lightPrimary = 0xB2DFDB;
  var textAndIcon = 0xFFFFFF;
  var accent = 0xFFEB3B;
  var textPrimary = 0x212121;
  var textSecondary = 0x757575;
  var dividerColor = 0xBDBDBD;
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key? key}) : super(key: key);

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    getAllCompaigns();

    return Scaffold(
      appBar: AppBar(
        title: Text('widget.title'),
      ),
      body: Container(child: Text('here we go')),
    );
  }
}
