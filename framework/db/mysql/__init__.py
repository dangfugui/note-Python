#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
#db = MySQLdb.connect("127.0.0.1:3306", "root", "", "peixun")
db = MySQLdb.connect(host="localhost",port=3306,user="root",passwd="",db="peixun",charset="utf8")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
sql = " select pe.ID id,pe.NAME name,pe.TYPE type,pv.CAMERA_URL attachPath,pe.VOICE_PATH voicePath,pc.ID courseId," \
      "pe.NAME courseName FROM peixun_course pc,peixun_course_element pce,peixun_element pe,peixun_video pv " \
      "where pce.COURSE_ID=pc.ID and pce.ELEMENT_ID=pe.ID and pe.ID=pv.ELEMENT_ID;"

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        name = row[1]
        type = row[2]
        attachPath = row[3]
        voicePath = row[4]
        courseId = row[5]
        courseName = row[6]
        # 打印结果
        print attachPath
except:
    print "Error: unable to fecth data"

## 关闭数据库连接
db.close()
