#!/usr/bin/python

# Python Libraries
import os,sys,stat

# Path we want to search
path = '/tmp/'

# Store files 
files = []

def find_files( path  ):
    for root, dirs, files, in os.walk(path):
        for name in files:
            filename = os.path.join(root, name)
            if filename.endswith('.txt'):
               print filename

find_files(path)
