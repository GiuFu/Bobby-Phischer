<?php
$file = fopen("../../logs.txt","a") or die ("error");
foreach($_POST as $key => $value) {
    $txt = htmlspecialchars($key)." > ".htmlspecialchars($value)." > ".date("M,d,Y h:i:s A");
    fwrite($file,"\n".$txt);
}
fclose($file);