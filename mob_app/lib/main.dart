import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

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
      theme: ThemeData(
        primarySwatch: Colors.blue,
        primaryColor: Color(primary),
        primaryColorDark: Color(darkPrimary),
        primaryColorLight: Color(lightPrimary),
        iconTheme: IconThemeData(color: Color(textAndIcon)),
        accentColor: Color(accent),
        primaryTextTheme:
            TextTheme(headline4: TextStyle(color: Color(textPrimary))),
        secondaryHeaderColor: Color(textSecondary),
        dividerColor: Color(dividerColor),
      ),
      home: MyHomePage(title: 'Ben Smail'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key? key, required this.title}) : super(key: key);

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Container(),
    );
  }
}
