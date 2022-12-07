<!DOCTYPE html>

<html>
<head>
	<title>LoGiC?</title>
</head>
   <body>
   <h2>Fill the form</h2>
      <form action = "/home.php" method = "POST">
         Name: <input type = "text" name = "name" />
         Secret: <input type = "text" name = "secret" />
         <input type = "submit" />
      </form>

      <h2>Source Code of the task</h2>
      <?php show_source("source.php"); ?>
   
   </body>
</html>