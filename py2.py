# -*- coding:utf-8 -*-  
import re 
import urllib2
res= urllib2.urlopen('http://www.heibanke.com/lesson/crawler_ex00/')
f= res.read().decode('utf-8')
b= re.compile(u'你')
s = re.findall(b,f)
print s[0].encode('utf-8')



