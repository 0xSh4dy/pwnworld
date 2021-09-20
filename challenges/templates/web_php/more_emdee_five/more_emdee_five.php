<?php
    $flag = "flag{0h_y34h_1_4m_g3n1us_w0000oooo00w}";
    if(isset($_GET["data"])){
        $userInput = $_GET["data"];
        $hash = md5($userInput);
        if($hash==$userInput){
            echo $flag;
        }
        else{
            echo "Try harder";
        }
    }
    else{
        echo "Try harder";
    }
?>