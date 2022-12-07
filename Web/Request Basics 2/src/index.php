<html>
<head>
  <title>Basic Request (2)</title>
</head>
  <body background="bg.jpg">
    <h2>Source Code</h2>
    <?php
    show_source("source.php");
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (!isset($_POST['flag'])){
    $_POST['flag']=null;
  }
  
  $result = $_POST['flag'];
  if (empty($result)) {
    echo "<h2>FLAG : no data provided : empty http body or wrong key value pair</h2>";
  } else {
    if ($result === "BasicButImportant"){
      echo "<h2>FLAG : Securinets{POST_ReqUest_woRking_liKe_Charm}</h2>";
    }
    else{
      echo "<h2>FLAG : u're very close, but wrong value</h2>";
    }
  }
}
?>

<p>-----------------</p>
<h2>The POST Method</h2>
<p>POST is used to send data to a server to create/update a resource.</p>
<p>The data sent to the server with POST is stored in the request body of the 
HTTP request:</p>
<div>
 <div>
POST /demo_form.php HTTP/1.1<br>
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
<h2>Useful ressources</h2>
<a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST" target="_blank">Content-type</a>
<a href="https://everything.curl.dev/http/post/simple" target="_blank">Curl</a>
<a href="https://www.postman.com/" target=_blank>Postman</a>
  </body>
</html>