# /usr/bin/python
# -*- coding=utf8 -*-
"""
   该方法主要用来构建用户的移动轨迹
   对于用户数据要按照时间顺序进行排序
"""
import time
import sys
sys.path.append("../")
from config import *

def convertTime(timeStampStr):
	times = timeStampStr.split('.')
	timeStamp = times[0]
	timeArray = time.strptime(timeStamp, "%Y-%m-%d %H:%M:%S")
	return int(time.mktime(timeArray))

if __name__ == "__main__":
	users = {}	
	locations = {}
	writer = open(RECORD_SORTED_USER,"w")
	for index,text in enumerate(open(LOCATION_LABEL).readlines()):
		#if index > 10000:
		#	break
		datas = text.strip().split(",")
		userid = datas[1]
		if (not userid in users):
			users[userid] = []
		users[userid].append(text)
	print "用户总数:%d" % len(users)
	for index, userid in enumerate(users):
		if index % 1000 == 0:
			print "正在处理第:%d个用户" % index
		specificUser = {}
		for text in users[userid]:
			datas = text.split(",")
			date = convertTime(datas[0])
			specificUser[date] = text
		recordsByTime = sorted(specificUser.items(),key = lambda d:d[0])
		preLabel = None
		for record in recordsByTime:
			timeStamp = record[0]
			text = record[1]
			datas = text.split(",")
			date = datas[0]
			userid = datas[1]
			label = datas[2].strip()
			if not preLabel or label != preLabel:
				writer.write("%s,%s,%s,%s\n" % (date,timeStamp,userid,label))
				preLabel = label
	writer.close()
