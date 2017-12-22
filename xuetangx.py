# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 18:51:47 2017

@author: liusifan
"""

import pandas as pd
import codecs
import urllib
from bs4 import BeautifulSoup
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

f = codecs.open('xuetangx.txt','w','utf8')                    
for i in range(2):
    url = "http://www.xuetangx.com/courses?credential=0&page_type=0&cid=0&process=0&org=0&course_mode=0&page="+str(i)
    res = urllib.urlopen(url)
    soup = BeautifulSoup(res,"html.parser")
    course_div = soup.find_all(attrs={"class":"coursename"})
    
    for course in course_div:
        
        print course.find(attrs={"class":"coursetitle"}).string
        x = course.find(attrs={"class":"coursetitle"}).string
        f.write(x)
        teacher = course.find(attrs={"class":"fl name"})
        print teacher.find("span").string    
        print course.find(attrs={"class":"model"}).string