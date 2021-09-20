<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
        
</head>
<style>
    
</style>
<body>
    <!-- Set the background as Naruto's image -->
    <h3>Hi, I am Naruto Uzumaki. Believe it. I am gonna be a hokage some day. I never give up on my word. That's my ninja way.</h3>
    <form action="naruto.php" method="POST">
        <input type="text" name="specialJutsu" placeholder="What is my favorite food?">
        <input type="text" name="favoriteFood" placeholder="What is my special jutsu?">
        <input type="submit" value="Check">
    </form>
    <!-- <p>
    class Naruto {  
    public $specialJutsu="chidori";  
    public $favoriteFood="hamburger";
    public function hinata() {  
        if ($this->specialJutsu === "Rasengan" and $this->favoriteFood ==="IchirakuRamen") {  
          global $flag;
          echo $flag;
        }  
        else {  
            echo "You ain't a true Naruto fan";  
        }  
    }  
}  
  
if (isset($_POST['specialJutsu'])) { 
        $naruto = unserialize($_POST['specialJutsu']);
        $naruto->hinata();  
  
} else {  
    echo "<h3>You ain't a true Naruto fan</h3>";  

}
    </p> -->
</body>

</html>
 
 
<?php 
$flag = "<h3>flag{php_w17h_n4ru70_is_1n73r3s71ng_yeee333aaa44}</h3>";
class Naruto {  
    public $specialJutsu="chidori";  
    public $favoriteFood="hamburger";
    public function hinata() {  
        if ($this->specialJutsu === "Rasengan" and $this->favoriteFood ==="IchirakuRamen") {  
          global $flag;
          echo $flag;
        }  
        else {  
            echo "You ain't a true Naruto fan";  
        }  
    }  
}  
  
if (isset($_POST['specialJutsu'])) { 
        $naruto = unserialize($_POST['specialJutsu']);
        $naruto->hinata();  
  
} else {  
    echo "<h3>You ain't a true Naruto fan</h3>";  

}

?> 