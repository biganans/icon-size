#!/usr/bin/python
# coding=utf-8
import os
import shutil
import time
import sys
import Image  
import glob, os  
import string

   

   
#图片批处理  
def timage(filename,outpath,outname,size,height):  
        print filename
        print outpath
        print outname
        print size
        #判断opfile是否存在，不存在则创建  
        if (os.path.isdir(outpath)==False):  
            os.mkdir(outpath)  
        im = Image.open(filename)  
        im_ss = im.resize(( string.atoi(size),  string.atoi(height)),Image.ANTIALIAS)  
        im_ss.save(outpath+'/'+outname,"png")  


def readAndfile(refilename,outpath):
    f = file(refilename)
    while True:
        line = f.readline().strip('\n')
        if len(line) == 0:
            break
        else:
           array=line.split()
           if( not (array[0] == '#')) :
                timage(outpath+'/xx.png',outpath,array[0],array[1],array[2])
    f.close()

def readPath(filename):
    f = file(filename)
    while True:
        line = f.readline().strip('\n')
        if len(line) == 0:
            break
        else:
           array=line.split()
           if( not (array[0] == '#')) :
               readAndfile("listfilename",array[0])
    f.close()

readPath("listiconfiles")
