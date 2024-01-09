#!/usr/bin/python3
if __name__ == "__main__":
   from hidden_4 import *
   def_names = dir()
   for i in range(0, len(def_names)):
        if def_names[i][:2] != '__':
            print("{:s}".format(def_names[i]))
