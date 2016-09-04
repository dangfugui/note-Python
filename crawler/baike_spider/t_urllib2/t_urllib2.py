#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016年8月30日

@author: duang
'''
import urllib2
import cookielib
url="http://www.baidu.com"
class Myurllib2:#爬取一个url
    url="http://www.baidu.com"
    def urlopen(self,url):
        response=urllib2.urlopen(url);
        print response.getcode()
        print len(response.read())
        return response
        
    def request(self,url):
        request=urllib2.Request(url)
        request.add_header("user-agent", "Mozilla/5.0")
        response=urllib2.urlopen(url)
        print response.getcode()
        print len(response.read())
        return response
    
    def cookielib(self,url):
        cj=cookielib.CookieJar()
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        response=urllib2.urlopen(url)
        print response.getcode()
        print cj
        print len(response.read())
        #print response.read()
        return response
       
if __name__ == '__main__':
    url="http://www.baidu.com"
    myurllib2=Myurllib2()
    myurllib2.urlopen(url)
    myurllib2.request(url)
    myurllib2.cookielib(url)