<html>
<head>
  <title>
    Request basics 3
  </title>
</head>
  <body background="bg.jpg">
    <h2>Source Code</h2>
    <?php show_source("source.php")?>
  <h2>Your request Headers</h2>  
  -------------
    <?php
    function getReqHeader() {
    $headers = array();
    foreach($_SERVER as $key => $value) {
        if (substr($key, 0, 5) <> 'HTTP_') {
            continue;
        }
        $header = str_replace(' ', '-', ucwords(str_replace('_', ' ', strtolower(substr($key, 5)))));
        $headers[$header] = $value;
    }
    return $headers;
}

$headers = getReqHeader();

foreach ($headers as $header => $value){
    echo "$header: $value <br />\n";
}

if (empty($_SERVER['HTTP_FLAG'])){
    echo "----------------<br><h4>Add 'flag' as HTTP Header, with the appropriate value</h4>";
}
else if ($_SERVER['HTTP_FLAG'] === "n0s"){
  echo "<h2>FLAG: Securinets{GoOd_job!_Read_more_about_http_headers!!}</h2>";
}
else{
  echo "----------------<br><h4>Very Close, try again!</h4>";
}
    
    ?>
----------------<br>
<h2>Ressource</h2>
<a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers">Http headers</a>
  </body>
</html>