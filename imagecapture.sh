#!/bin/bash
# Image capture script, allocated at the EC2

ssh -i id_rsatel u0_a170@localhost -p 43023 "termux-camera-photo -c 0 /data/data/com.termux/files/home/pics/testpic2.jpg; exit"
ssh -i id_rsatel u0_a170@localhost -p 43023 "cd /data/data/com.termux/files/home/.local/bin; ./aws s3 sync '/data/data/com.termux/files/home/pics/' s3://ee542temperatureflowdata; exit "

