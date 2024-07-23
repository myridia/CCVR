#!/usr/bin/env python3
import os,re 
import configparser
import magic 
import sortedcontainers

class App():
  def __init__(self):
    self.config = configparser.ConfigParser()
    self.config.read(os.path.dirname(os.path.abspath(__file__))+'/config.ini')
    _dir = self.config['path']['dir_name']
    _file = self.config['path']['file_name_start']
    #created the reg at : https://regex101.com/
    #regex = 'GET \/\w+\/_design\/\w+\/_view\/\w+'
    regex = 'GET \\/[a-zA-Z0-9_]+\\/_design\\/[a-zA-Z0-9_]+\\/_view\\/[a-zA-Z0-9_]+'    
    counter = sortedcontainers.SortedDict()
    if os.path.isdir(_dir):
      for (root, dirs, file) in os.walk(_dir):
        for filename in file:
          if filename.startswith(_file):
            filepath = _dir + "/" + filename
            f = magic.Magic(mime=True)
            if f.from_file(filepath) == 'text/plain':
              print(filepath)
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
