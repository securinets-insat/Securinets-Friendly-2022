<!DOCTYPE html>
<html lang="en">

<head>
  <meta http-equiv="content-type" content="text/html; charset=UTF-8">
  <title>Tunisia</title>
  <script src="data.js"></script>
  <script src="tunisia.js"></script>
</head>

<body>
  <?php 
  show_source("source.php");
  if (!isset($_GET['placeholder1'])){
    echo "<br><br><br><b>missing GET param</b>";
  }
  else{
    $res=$_GET['placeholder1'];
    echo $res;
  }
  

  ?>
  <div id="placeholder2"></div>

</body>

</html>