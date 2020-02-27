# Bobby Phischer, the easier phishing tool for bad webisites

Bobby Phischer helps you understand how phishing works and how easy it is, everything it does is:
* download page
* replace actions
* start PHP server 
* print POST data to logs.txt
* rediect to real website

## usage 
* python3 main.py  URL PORT
* only URL if you just want to download the website and replace the action of every form, in windows use just "python"

If you want to do something different with the POST data, edit action.php

## vulnerable webisites
This tool works with websites having the following form structure
~~~~
<form action="..." method="post">
    <input type="...">
    ...
</form>
~~~~
If this tool doesn't work with the website you wantyou need to do some more modification such as deleting javascript, adding actions or moving forms

## requirements
* wget
* php
* python3
* MinGW (for Windows)