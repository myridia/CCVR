#!/bin/sh

rm -rf dist 
rm -rf build

pyinstaller main.py -F -w -n ccvr_macos

if [ -f config.ini ] #check if file exists
then
   echo "...copy config.ini to dist/config.ini"    
   sudo cp config.ini dist/
else
   echo "...copy config_defaut.ini to dist/config.ini"
   sudo cp config_default.ini dist/config.ini
fi



if [ -d log_example ] #check if file exists
then
   echo "...copy log example"    
   sudo cp -rf log_example dist/ 
fi





 

