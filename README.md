# count_couchdb_view_requests
Count CouchDB View Requests From a Haproxy Logs files 

# How to run the Script File 

## Copy config_default.ini to config.ini and adjust it
```console
cp config_default.ini config.ini
```

## Enviroment Setup 
```console
python3.12 -m venv env
. env/bin/activate
pip install pip --upgrade
pip install -r requirements.txt
```

## Set Permission and run the script
```console
sudo chmod +x main.py
python main.py 
```


## To make a binary release for linux or windows try 
```console
./make_linux_binary.sh
./make_windows_binary.sh
```
