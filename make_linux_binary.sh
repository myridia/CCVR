# See https://myridia.com/dev_posts/view/3489 for more info 
docker run -v "$(pwd):/src/" engineervix/pyinstaller-linux "pyinstaller -F main.py"
docker run -v "$(pwd):/src/" engineervix/pyinstaller-linux
sudo cp config.ini dist/
sudo cp config.ini dist/linux
