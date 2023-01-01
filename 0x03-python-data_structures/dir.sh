#!/bin/bash
x=$RANDOM
base64 flag.txt > /tmp/$x
function finish{
&nbsp;&nbsp;rm /tmp/$x
}
trap finish EXIT
sleep 15
