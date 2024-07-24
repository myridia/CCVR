#!/usr/bin/env python
import os,re 
import configparser
import sortedcontainers
from pathlib import Path
from binaryornot.check import is_binary

class App():
  def __init__(self):
    print("...init")
    
  def check(self):  
    config_file = Path('config.ini')
    print("...looking for config file in {0}".format(config_file))    
    if config_file.is_file():
      self.config = configparser.ConfigParser()
      self.config.read(config_file)
    else:
      print("...error: config.ini file does not exists! copy config_default.ini to config.ini and adjust it.")
      return

    _dir = self.config['path']['dir_name']
    _file = self.config['path']['file_name_start']
    #created the reg at : https://regex101.com/
    regex = 'GET \\/[a-zA-Z0-9_]+\\/_design\\/[a-zA-Z0-9_]+\\/_view\\/[a-zA-Z0-9_]+'    
    counter = sortedcontainers.SortedDict()
    if os.path.isdir(_dir):
      for (root, dirs, file) in os.walk(_dir):
        for filename in file:
          if filename.startswith(_file):
            filepath = _dir + "/" + filename
            if is_binary(filepath) == False:
              print("...looking for: {}".format(filepath))
              with open(filepath, 'r') as f:
                for l in f:
                  for match in re.finditer(regex, l, re.S):
                    match_text = match.group()
                    a = match_text.split('/')
                    _id = "{0}---{1}---{2}".format(a[1],a[3],a[5])
                    if _id not in counter:
                      counter[_id] = 1
                    else:
                      counter[_id] += 1                      
    for i in counter:
      print("{0}\t{1}".format(counter[i],i))
      
if __name__ == "__main__":
  a = App()
  a.check()
