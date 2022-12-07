<?php
if (!isset($_GET['flag'])){
   $_GET['flag'] = null;
}
if ($_GET['flag'] === 'BasicButImportant')
   print("<script>alert('Securinets{Redacted}')</script>");
?>