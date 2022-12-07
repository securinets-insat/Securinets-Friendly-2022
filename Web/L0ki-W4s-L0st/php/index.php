

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>The orcale's sight</title>
    <link rel="stylesheet" href="https://unpkg.com/flowbite@1.5.3/dist/flowbite.min.css" />
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body class="bg-gray-900 text-white  w-sceen py-10">

  <script src="https://unpkg.com/flowbite@1.5.3/dist/flowbite.js"></script>
<main class="px-16">
    <h1 class="text-6xl font-bold"> Where is Loki ? </h1>
<h2>These are the realms of the Norse world, Loki should be in one of them can you find him ?</h2>
<div class="h-10"></div>
<div class="flex flex-col space-y-3 px-[13] ">
    <a href="?page=asgard.html" class="text-purple-400 underline">Asgard</a>
    <a href="?page=alfheim.html" class="text-purple-400 underline">Alfheim</a>
    <a href="?page=jothunheim.html" class="text-purple-400 underline">Jothunheim</a>
    <a href="?page=midgard.html" class="text-purple-400 underline">Midgard</a>
    <a href="?page=muspleheim.html" class="text-purple-400 underline">Muspelheim</a>
    <a href="?page=nidavellir.html" class="text-purple-400 underline">Nidavellir</a>
    <a href="?page=nilfheim.html" class="text-purple-400 underline">Nilfheim</a>
    <a href="?page=svartalfheim.html" class="text-purple-400 underline">Svartalfheim</a>
</div>
</main>

<div>
<?php 

if(isset($_GET['page'])){
  $file_contents= file_get_contents($_GET['page']);
    $realm_name=ucwords(preg_replace('/(.html)/i','',$_GET['page']));
  echo "<h1 class='text-4xl  text-cyan-700 mt-10 px-16'><span class='italic'>".$realm_name."</span> Realm</h1><div class='bg-gray-700 w-screen min-h-[400px] mt-8 p-10'><p class='text-2xl text-yellow-400'>".$file_contents."</p></div>";
}
?>


<div></div>



  </body>

</html>
