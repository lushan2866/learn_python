# -*- coding:utf-8 -*-  
import re 
import urllib2

url = 'http://www.heibanke.com/lesson/crawler_ex00/'
def read_html():
    res= urllib2.urlopen(url)
    f= res.read().decode('utf-8')
    b= re.compile(u'你需要在网址后输入数字\d{5}')
    s = re.findall(b,f)
    print s[0].encode('utf-8')


read_html()

