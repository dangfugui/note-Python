#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016年9月4日

@author: duang
'''


class HtmlPutputer(object):
    def  __init__(self):
        self.datas=[]
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        fout=open('output.html','w')
        fout.write("<html>")
        fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></meta></head>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:#ascii
            fout.write("<tr>\n")
            fout.write("<td>%s</td>" % data["url"].encode("utf-8"))
            fout.write("<td>%s</td>" % data["title"].encode("utf-8"))
            fout.write("<td>%s</td>" % data["summary"].encode("utf-8"))
            fout.write("</tr>\n")
            
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
    
    
    
    



