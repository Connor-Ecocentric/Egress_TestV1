#!/bin/bash
more /etc/hostname >>$HOSTNAME.txt
more /media/sdcard/config.ini | grep client_id | awk '{print $3}' >>$HOSTNAME.txt
more /home/root/config.bak | grep client_id | awk '{print $3}' >>$HOSTNAME.txt; value=$(more /home/root/config.bak | wc -l); if [ $value -lt 1 ]; then  echo 'NaN'; fi>>$HOSTNAME.txt 
# The above have an if statement that checks if the value is empty (file doesnt exist) and returns a NaN, else it just returns the exprected value
eco-feature-extract -e | grep Serial | awk '{print $4}' >>$HOSTNAME.txt
#All of the above should match the Serial number of the Collector.
stat / | grep Device | awk '{print $2}' >>$HOSTNAME.txt
stat /media/sdcard | grep Device | awk '{print $2}' >>$HOSTNAME.txt
#The above should return b11h and b302h respectively
sha1sum /eco-overlay.tar.gz | awk '{print $1}' >>$HOSTNAME.txt; value=$(sha1sum /eco-overlay.tar.gz | wc -l); if [ $value -lt 1 ]; then  echo 'NaN'; fi>>$HOSTNAME.txt
sha1sum /run/media/mmcblk1p2/eco-overlay.tar.gz | awk '{print$1}' >>$HOSTNAME.txt; value=$(sha1sum /eco-overlay.tar.gz | wc -l); if [ $value -lt 1 ]; then  echo 'NaN'; fi>>$HOSTNAME.txt
#The above checks the collector version on both the A and B partition
df -Th | grep mmcblk0 | grep /dev/mmcblk0p2 | awk '{print $2,$3,$6}' >>$HOSTNAME.txt
#Check that sd card has been exteneded. column1 is type (ext4) 2 is size (12gb) and 3 is used space (should be low)
tail -30 /media/sdcard/eco-feature-extract.log | grep RMS | awk '{print $39,$41,$43}' >>$HOSTNAME.txt
#Check the voltage readings across all 3 phases (this will confirm hw mods are ok and voltage calibration is correct)
hdparm -t /dev/mmcblk0 | awk '{printf $11}' >>$HOSTNAME.txt
echo "" >>$HOSTNAME.txt
hdparm -t /dev/mmcblk1 | awk '{printf $11}' >>$HOSTNAME.txt
echo "" >>$HOSTNAME.txt
#Run a BIT and return only the results that have failed
numen9_bit | grep FAIL >>$HOSTNAME.txt
#Confirm CPU temperature
cat /sys/class/thermal/thermal_zone0/temp >>$HOSTNAME.txt
# Confirm wifi strength and link quality
iwconfig wlan0 | grep 'Link Quality' | awk '{print $2}' >>$HOSTNAME.txt
iwconfig wlan0 | grep 'Link Quality' | awk '{print $4}' >>$HOSTNAME.txt
# check the schema version of both the config.ini and config.default not sure if the default file is meant to have a schema or not.....
more /media/sdcard/config.ini | grep schema | awk '{print $3}' >>$HOSTNAME.txt
more /media/sdcard/config.ini.default | grep schema | awk '{print $3}' >>$HOSTNAME.txt
#check all eeprom values and make sure that they are unique
eco-feature-extract -e | grep Gain | awk '{print $7,$8,$17}' >>$HOSTNAME.txt
# SD card endurance checking
./SMART_Tool_Sample_armabihf /dev/mmcblk0 | grep Erase | grep Average | awk '{print $4}' >>$HOSTNAME.txt
./SMART_Tool_Sample_armabihf /dev/mmcblk0 | grep Erase | grep Maximum | awk '{print $4}' >>$HOSTNAME.txt

