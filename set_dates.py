#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 17:44:11 2019

@author: gykovacs
"""

import os
from glob import glob
import subprocess
import sys

files= glob("*.png")

for f in files:
    filename= os.path.basename(f)
    splitted= f.split('-')
    
    year= int(splitted[0])
    month= 2
    day= 2
    
    if len(splitted) > 2:
        print(splitted[0], splitted[1], splitted[2])
    
    try:
        if len(splitted) > 1:
            if len(splitted[1]) == 2:
                month= int(splitted[1])
                if not (month >= 1 and month <= 12):
                    month= 2
                if len(splitted) > 2:
                    day= int(splitted[2])
                    if not (day >= 1 and day <= 31):
                        day= 2
    except Exception as e:
        print(e)
    
    print(year, month, day)
    
    jpgname= f[:-3] + "jpg"
    date="%d:%02d:%02d 12:00:00" % (year, month, day)
    
    subprocess.call(["convert", f, "-quality", "100", jpgname])
    subprocess.call(["exiftool", '-datetimeoriginal="%s"' % date, '-createdate="%s"' % date, '-modifydate="%s"' % date, '-filemodifydate="%s"' % date, jpgname])
