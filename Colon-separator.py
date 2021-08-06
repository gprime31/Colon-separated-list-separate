#!/usr/bin/env python3

#Script By Oxconft

import sys

def writex(data, filename):
    with open(filename,"a") as f:
        f.write(data+"\n")

with open('username.txt',"a") as uname, open('password.txt',"a") as passwd:
    for a in sys.stdin:
        username,password = a.strip().split(":")
        uname.write(username+"\n")
        passwd.write(password+"\n")
