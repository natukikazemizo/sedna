#!BPY
# -*- coding: UTF-8 -*-
# Log
#
# 2017.07.17 Natukikazemizo
import datetime

def start(pyName):
    print(datetime.datetime.today().\
        strftime("%Y/%m/%d %H:%M:%S.%f ") + pyName + " START")

def end(pyName):
    print(datetime.datetime.today().\
        strftime("%Y/%m/%d %H:%M:%S.%f ") + pyName + " END")

