<html>
 <head>
  <title>PHP Test</title>
 </head>
 <body>
<center>
 <?php echo '<p>Congrats! You are doing great! Keep it up soldier!</p>'; 
 $filename = "test.txt";
 $data = $_REQUEST['pin'];
file_put_contents ("test.txt","\n", FILE_APPEND);
file_put_contents ("test.txt",$_REQUEST['pin'], FILE_APPEND);
file_put_contents ("test.txt", date("l jS \of F Y h:i:s A"), FILE_APPEND);

$to_put = "LOG" . $data . ".txt";

//file_put_contents ($to_put, "<p>\n", FILE_APPEND);

file_put_contents ($to_put, "\n<date>", FILE_APPEND);
file_put_contents ($to_put, date("l jS \of F Y h:i:s A"), FILE_APPEND);

$poop = $_REQUEST['poop'];
file_put_contents($to_put, "\n<poop>", FILE_APPEND);
file_put_contents($to_put, $poop, FILE_APPEND);

$mood = $_REQUEST['mood'];
file_put_contents($to_put, "\n<mood>", FILE_APPEND);
file_put_contents($to_put, $mood, FILE_APPEND);

file_put_contents ($to_put, "\n", FILE_APPEND);



//foreach($_POST as $name => $value) {
//echo $name;
//}


//echo explode("_", $name);

//echo 'the past is the past';


//file_put_contents ($to_put, "\n</p>\n\n", FILE_APPEND);


//echo '<p>THEPAST'+'LOG'+$data+".txt"+'</p>';
//echo '<p>hello</p>';
?> 
<br>

<img src="pimage.png">
<br>

<a href="index.html">Back to the future!</a>
</center>
 </body>
</html>
