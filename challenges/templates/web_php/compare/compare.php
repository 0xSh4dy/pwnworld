<?php
    $flag = "flag{n0w_I_d3t3ct3d_vu1n3r4b1l17y_1n_s7rcmp}";
    if(isset($_POST["flag"])){
        $var = $_POST["flag"];
        if(strcmp($var,$flag)==0){
            echo "Haha, I was kidding. There is no such thing as admin over here. Take a flag as a reward: ",$flag;
        }
        else{
            echo "Sorry, you are not admin";
        }
    }
    else{
        echo "Hmmmph, you are not admin";
    }

?>