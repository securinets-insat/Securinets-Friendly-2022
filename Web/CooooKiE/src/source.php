<html>
  <head>
    <title>
      COOOooookiee
    </title>
    <style>
      .bg{
        background-image: url("bg.webp");
        background-repeat: no-repeat;
        background-size: cover;
        background-position: center;
      }
      span{
        color: white;
        font-size: 20px;
      }

    </style>
  </head>
  <body class="bg">
    
<?php
$cookie_name = "admin";
$cookie_value = "false";
setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/");
if (empty($_SERVER['HTTP_COOKIE'])){
    echo "<span>c2VjdXJpbmV0cw==</span>";
}
else if ($_SERVER['HTTP_COOKIE'] === "admin=true"){
  echo "<span>might be good, but nah</span>";
}


    
    ?>

  </body>
</html>