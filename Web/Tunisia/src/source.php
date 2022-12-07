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