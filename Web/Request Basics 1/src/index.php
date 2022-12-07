<!DOCTYPE html>

<html>
<head>
  <title>Request basics (1)</title>
   <style>
      table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
   </style>
</head>
<body background="bg.jpg">
   <h2>Source Code</h2>
   <?php
show_source("source.php");
if (!isset($_GET['flag'])){
   $_GET['flag'] = null;
}
if ($_GET['flag'] === 'BasicButImportant')
   print("<script>alert('Securinets{SucCessful_Get_pArAm}')</script>");
?>
   <h2>What is HTTP?</h2>
<p>The Hypertext Transfer Protocol (HTTP) is designed to enable 
communications between clients and servers.</p>
<p>HTTP works as a request-response protocol between a client and server.</p>
<p>Example: A client (browser) sends an HTTP request to the server; then the server 
returns a response to the client. The response contains status information about 
the request and may also contain the requested content.</p>
<hr>

<h2>HTTP Methods</h2>
<ul>
  <li><b>GET</b></li>
  <li><b>POST</b></li>
  <li><strong>PUT</strong></li>
  <li><strong>HEAD</strong></li>
  <li><strong>DELETE</strong></li>
  <li><strong>PATCH</strong></li>
  <li><strong>OPTIONS</strong></li>
  <li><strong>CONNECT</strong></li>
  <li><strong>TRACE</strong></li>
</ul>
<p>The two most common HTTP methods are: GET and POST.</p>
<hr>

<h2>The GET Method</h2>
<p>GET is used to request data from a specified 
resource.</p>

<p>Note that the query string (name/value pairs) is sent in the URL of 
a GET request:</p>
<div>
<div>
/test/demo_form.php?name1=value1&amp;name2=value2
</div></div>

<p><b>Some notes on GET requests:</b></p>
<ul>
  <li>GET requests can be cached</li>
  <li>GET requests remain in the browser history</li>
  <li>GET requests can be bookmarked</li>
  <li>GET requests should never be used when dealing with sensitive data</li>
  <li>GET requests have length restrictions</li>
  <li>GET requests are only used to request data (not modify)</li>
</ul>
<hr>

<h2>The POST Method</h2>
<p class="intro">POST is used to send data to a server to create/update a resource.</p>
<p>The data sent to the server with POST is stored in the request body of the 
HTTP request:</p>
<div>
 <div>
POST /test/demo_form.php HTTP/1.1<br>
Host: w3schools.com<br><br>
   name1=value1&amp;name2=value2
</div></div>
<p><b>Some notes on POST requests:</b></p>
<ul>
  <li>POST requests are never cached</li>
  <li>POST requests do not remain in the browser history</li>
  <li>POST requests cannot be bookmarked</li>
  <li>POST requests have no restrictions on data length</li>
</ul>
<hr>

<h2>Compare GET vs. POST</h2>
<p>The following table compares the two HTTP methods: GET and POST.</p>
<div >
<table>
  <tr>
    <th style="width:30%">&nbsp;</th>
    <th style="width:35%">GET</th>
    <th>POST</th>
  </tr>
  <tr>
    <td>BACK button/Reload</td>
    <td>Harmless</td>
    <td>Data will be re-submitted (the browser should alert the user that the data are about to be re-submitted)</td>
  </tr>
  <tr>
    <td>Bookmarked</td>
    <td>Can be bookmarked</td>
    <td>Cannot be bookmarked</td>
  </tr>
  <tr>
    <td>Cached</td>
    <td>Can be cached</td>
    <td>Not cached</td>
  </tr>
  <tr>
    <td>Encoding type</td>
    <td>application/x-www-form-urlencoded</td>
    <td>application/x-www-form-urlencoded or multipart/form-data. Use multipart encoding for binary data</td>
  </tr>
  <tr>
    <td>History</td>
    <td>Parameters remain in browser history</td>
    <td>Parameters are not saved in browser history</td>
  </tr>
  <tr>
    <td>Restrictions on data length</td>
    <td>Yes, when sending data, the GET method adds the data to the URL; and the length of a URL is limited (maximum URL length is 2048 characters)</td>
    <td>No restrictions</td>
  </tr>
  <tr>
    <td>Restrictions on data type</td>
    <td>Only ASCII characters allowed</td>
    <td>No restrictions. Binary data is also allowed</td>
  </tr>
  <tr>
    <td>Security</td>
    <td>GET is less secure compared to POST because data sent is part of the URL<br>
 <br>
 Never use GET when sending passwords or other sensitive information!</td>
    <td>POST is a little safer than GET because the parameters are not stored in browser history or in web server logs</td>
  </tr>
  <tr>
    <td>Visibility</td>
    <td>Data is visible to everyone in the URL</td>
    <td>Data is not displayed in the URL</td>
  </tr>
  </table>
</div>
<hr>

<hr>

<h2>The PUT Method</h2>
<p>PUT is used to send data to a server to create/update a resource.</p>
<p>The difference between POST and PUT is that PUT requests are idempotent. That 
is, calling the same PUT request multiple times will always produce the same 
result. In contrast, calling a POST request repeatedly have side effects of 
creating the same resource multiple times.</p>
<hr>

<h2>The HEAD Method</h2>
<p>HEAD is almost identical to GET, but without the response body.</p>
<p>In other words, if GET /users returns a list of users, then HEAD /users will 
make the same request but will not return the list of users.</p>
<p>HEAD requests are useful for checking what a GET request will return before 
actually making a GET request - like before downloading a large file or response 
body.</p>
<hr>

<h2>The DELETE Method</h2>
<p>The DELETE method deletes the specified resource.</p>
<hr>

<h2>The PATCH Method</h2>
<p>The PATCH method is used to apply partial modifications to a resource.</p>
<hr>

<h2>The OPTIONS Method</h2>
<p>The OPTIONS method describes the communication options for the target 
resource.</p>
<hr>

<h2>The CONNECT Method</h2>
<p>The CONNECT method is used to start a two-way communications (a tunnel) with 
the requested resource.</p>
<hr>

<h2>The TRACE Method</h2>
<p>The TRACE method is used to perform a message loop-back test that 
tests the path for the target resource (useful for debugging purposes).</p>

<br>
<a href="https://www.w3schools.com/php/php_forms.asp" target="_about">&#169; W3school</a>
   
   
   </body>
</html>