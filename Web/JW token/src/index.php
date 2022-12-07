<!DOCTYPE html>
<?php
$cookie_name = "token";
$cookie_value = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IlBsYXllciIsImZsYWciOiJTZWN1cmluZXRze1N1Y2Nlc3NmdWxseV9EZWNvZGVkX0pXVH0iLCJpYXQiOjE1MTYyMzkwMjJ9.THDgWRRCxHgNplAY4WQ8F18yzgExWyfEJ2g8NLvvOkg";
setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day
?>
<html>
<head>
	<title>JW token</title>
</head>
<body background="./background.jpg">

Bon appetit!
</body>
</html>