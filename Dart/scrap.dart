import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}


class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: Colors.blue,
        appBar: AppBar(
          title: Text("My App Bar"),
          backgroundColor: Color.fromARGB(255, 192, 236, 121),
          elevation: 0,
          leading: Icon(Icons.menu),
          actions: [
            IconButton(onPressed: () {}, icon: Icon(Icons.logout))
          ],
        ),
        body: Center(
          child: Container(
            height: 300,
            width: 300,
            decoration: BoxDecoration(
               color: Color.fromARGB(255, 245, 210, 70),
               borderRadius: BorderRadius.circular(20)

            ),
            padding: EdgeInsets.all(25),
            child: Icon(
              Icons.favorite, 
              color: Colors.white, 
              size: 45,)   
          ),
        ),
      ),
    );
  }
}
