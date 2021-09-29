import 'package:http/http.dart' as http;
import 'dart:developer';

Object getCompaignById(String id) {
  return {};
}

void getAllCompaigns() async {
  var url = Uri.parse('http://10.0.2.2:8000/api/types/');

  var response = await http.get(url);
  log('Response status: $url');
  log('Response status: ${response.statusCode}');
  log('Response body: ${response.body}');
}

Object registerNewComment(String token, String compaign) {
  return {};
}

Object updateComment(String id, String token, String payload, String title) {
  return {};
}

Object delete(String id, String token) {
  return {};
}
