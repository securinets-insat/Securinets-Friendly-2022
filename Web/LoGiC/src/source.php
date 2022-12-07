<?php
   		if (isset($_POST['name']) && isset($_POST['secret'])){
	      if (preg_match("/[^A-Za-z']/",$_POST['secret'] ) || preg_match("/[^A-Za-z']/",$_POST['name'] )) {
	         die ("Only alphabetic chars are allowed (A-Z , a-z), without spaces");
	      }
	      else{
	      	echo "Welcome ". $_POST['name']. "<br />";
	      	$str = $_POST['secret'];
			$pattern = '/flag/i';
			$secret = preg_replace($pattern, '', $str);
			if ($secret === 'flag'){
			//Real flag will be displayed once you solve the task
	      	echo "Securinets{fake_flag}";
			}
			else{
				echo "you can't reveal my secret";
			}
			exit();
	      }
	      
		}
?>