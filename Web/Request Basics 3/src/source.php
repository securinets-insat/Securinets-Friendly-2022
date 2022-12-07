 <?php
 // Display incoming http Headers, OUT OF THE CHALLENGE SCOPE.
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
// function call.
$headers = getReqHeader();
// iterate over array
foreach ($headers as $header => $value){
    echo "$header: $value <br />\n";
}
// Flag here

if (empty($_SERVER['HTTP_FLAG'])){
    echo "----------------<br><h4>Add 'flag' as HTTP Header, with the appropriate value</h4>";
}
else if ($_SERVER['HTTP_FLAG'] === "n0s"){
  echo "<h2>FLAG: Securinets{Redacted}</h2>";
}
else{
  echo "----------------<br><h4>Very Close, try again!</h4>";
}
    
    ?>