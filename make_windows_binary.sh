# See https://myridia.com/dev_posts/view/3489 for more info 
docker run -v "$(pwd):/src/" batonogov/pyinstaller-linux "pyinstaller -F main.py"
docker run -v "$(pwd):/src/" batonogov/pyinstaller-windows

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
   sudo cp log_example dist/ -rf 
fi


