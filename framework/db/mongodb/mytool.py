#!/usr/bin/python
# -*- coding:utf-8 -*-
from pymongo import MongoClient

# 连接mongodb数据库
#client = MongoClient(['172.23.221.24', '172.23.221.25', '172.23.221.26'])
client = MongoClient(['172.24.8.15', '172.24.7.58', '172.24.7.59'])
# 指定数据库名称
db = client['crawler']
#db.authenticate(name="crawler", password="Xdu+77hw", source='crawler')
db.authenticate(name="manager", password="mongodb123", source='admin')
# 获取非系统的集合
collectionlist = db.collection_names(include_system_collections=False)
print db.shardingStatus()
for collection in collectionlist:
    print collection
   # print db[collection].getShardDistribution()
    break
    # if '_parser' in collection:
    #     haveIndex = 0
    #     for indexKey in db[collection].index_information():
    #         #print db[collection].index_information()[indexKey]['key']
    #         # for fileName in db[collection].index_information()[indexKey]['key']:
    #         #     if fileName[0] == u'index_groupUniqueId':
    #         #         haveIndex = 1;
    #         if u'groupUniqueId' in indexKey:
    #             haveIndex =1
    #     if haveIndex ==0:
    #         print 'not hava index_fetcher===================================================',collection,db[collection].count()



# print db.dongcha_sogou_normal_d_list.index_information()
# for indexs in db.dongcha_sogou_normal_d_list.index_information():
#     print db.dongcha_sogou_normal_d_list.index_information()[indexs]['key']

