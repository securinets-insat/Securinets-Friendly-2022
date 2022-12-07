    <?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (!isset($_POST['flag'])){
    $_POST['flag']=null;
  }
  
  $result = $_POST['flag'];
  if (empty($result)) {
    echo "no data provided : empty http body or wrong key value pair";
  } else {
    if ($result === "BasicButImportant"){
      echo "Securinets{Redacted}";
    }
    else{
      echo "u're very close, but wrong value";
    }
  }
}
?>