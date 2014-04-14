#!/usr/bin/python

__author__ = 'nicolas'

import zipfile
import optparse
from threading import Thread

def extractFile(zfile,password):
    try:
        zfile.extractall(pwd=password)
        print "[+] Found password" + password+"\n"
    except:
        pass

def main():
    parser=optparse.OptionParser("usage%prog -f <zipfile> -d <dictionary>")
    parser.add_option("-f",dest="zname",type="string",help="specify zip file")
    parser.add_option("-d",dest="dname",type="string",help="specify dictionary txt file")
    (options, args)=parser.parse_args()
    if(options.zname==None) |(options.dname==None):
        print parser.usage
        exit(0)
    else:
        zname=options.zname
        dname=options.dname

    zname=zipfile.ZipFile(zname)
    passFile=open(dname)

    for line in passFile.readlines():
        password=line.strip("\n")
        t=Thread(target=extractFile,args=(zname,password))
        t.start()
    print "password not found"
main()
