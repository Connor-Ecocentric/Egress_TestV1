#!/bin/bash

more /etc/hostname >>egress.txt
more /media/sdcard/config.ini | grep client_id | awk '{print $3}' >>egress.txt
more /home/root/config.bak | grep client_id | awk '{print $3}' >>egress.txt
eco-feature-extract -e | grep Serial | awk '{print $4}' >>egress.txt
#All of the above should match the Serial number of the Collector.

stat / | grep Device | awk '{print $2}' >>egress.txt
stat /media/sdcard | grep Device | awk '{print $2}' >>egress.txt
#The above should return b11h and b302h respectively

sha1sum /eco-overlay.tar.gz | awk '{print $1}' >>egress.txt
sha1sum /run/media/mmcblk1p2/eco-overlay.tar.gz | awk '{print$1}' >>egress.txt

#The above checks the collector version on both the A and B partition

df -Th | grep mmcblk0 | grep /dev/mmcblk0p2 | awk '{print $2,$3,$4}' >>egress.txt
#Check that sd card has been exteneded. column1 is type (ext4) 2 is size (12gb) and 3 is used space (should be low)

tail -30 /media/sdcard/eco-feature-extract.log | grep RMS | awk '{print $39,$41,$43}' >>egress.txt
#Check the voltage readings across all 3 phases (this will confirm hw mods are ok and voltage calibration is correct)
hdparm -t /dev/mmcblk0 | awk '{printf $11}' >>egress.txt
echo "" >>egress.txt
hdparm -t /dev/mmcblk1 | awk '{printf $11}' >>egress.txt
echo "" >>egress.txt