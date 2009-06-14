#!/usr/bin/python

# Python Libraries
import os,sys,stat

# Path we want to search
backuppath = '/pool/static/backup/clients/'

def find_files( backuppath  ):
    for root, dirs, files, in os.walk(backuppath):
        for name in files:
            filename = os.path.join(root, name)
            if filename.endswith('.sql'):
               print filename

find_files
