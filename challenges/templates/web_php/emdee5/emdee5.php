<?php
    $flag="flag{l00s3_c0mp4r1s0n_1s_d4ng3r0us}";
    if(isset($_POST["userdata"])){
        $userdata = $_POST["userdata"];
        $var1 = md5("240610708");
        $var2 = md5($userdata);
        if($var1==$var2){
            echo $flag;
        }
        else{
            echo "Try harder";
        }
    }
?>