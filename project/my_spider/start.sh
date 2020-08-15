#!/bin/bash

set -x

curPath=$(readlink -f "$(dirname "$0")")
echo $curPath

cd $curPath

# ps -ef | grep python | grep -v grep | awk '{print "kill -9 "$2}'|bash
ps ux | grep -E 'spider_' | grep -v grep |awk '{print $2}' |xargs kill -s 9



file=./log/$(date "+%Y%m%d_%H%M%S.log")
echo $file
echo ''>>$file
nohup python3 ./spider_classification.py > $file  2>&1 &
echo 'end'
