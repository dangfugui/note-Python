#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016年9月4日

@author: duang
'''
import urllib2
import cookielib


class HtmlDownloader(object):
    
    
    

    
    def download(self,url):
        if url is None:
            return None;
        response=self.urlopen(url)
        if response.getcode()!=200:
            return None
        return response.read()
        
        
    def urlopen(self,url):#下载一个网页
        response=urllib2.urlopen(url);
        return response
        
    def request(self,url):#下载一个网页
        request=urllib2.Request(url)
        request.add_header("user-agent", "Mozilla/5.0")
        response=urllib2.urlopen(url)
        print response.getcode()
        print len(response.read())
        return response
    
    def cookielib(self,url):#下载一个网页
        cj=cookielib.CookieJar()
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        response=urllib2.urlopen(url)
        print response.getcode()
        print cj
        print len(response.read())
        #print response.read()
        return response
       
    
    
    



