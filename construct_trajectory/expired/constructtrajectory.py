# /usr/bin/python
# -*- coding=utf8 -*-
"""
   该方法主要用来构建用户的移动轨迹
   对于用户数据要按照时间顺序进行排序
"""
import time

def convertTime(timeStampStr):
	times = timeStampStr.split('.')
	timeStamp = times[0]
	timeArray = time.strptime(timeStamp, "%Y-%m-%d %H:%M:%S")
	return int(time.mktime(timeArray))

if __name__ == "__main__":
	users = {}	
	locations = {}
	#writer = open('output/trajectorybyuser_test',"w")
	writer = open('output/trajectorybyuser_20100923',"w")
	#for text in open("data/cdr_ler_20100916.TXT").readlines():
	for text in open("data/cdr_ler_20100923.TXT").readlines():
	#for text in open("data/testfile").readlines():
		datas = text.split(",")
		date = datas[0]
		userid = datas[1]
		lac = datas[3]
		ci = datas[4]
		if (not userid in users):
			users[userid] = []
		users[userid].append(text)

	for index,text in enumerate(open("data/result_location_mark").readlines()):
		if index == 0:
			continue
		datas = text.split()
		lac = int(datas[0])
		ci = int(datas[1])
		locationId = datas[2]
		longitude = datas[3]
		latitude = datas[4]
		locations[(lac,ci)] = locationId
	
	for userid in users:
		specificUser = {}
		for text in users[userid]:
			datas = text.split(",")
			date = convertTime(datas[0])
			specificUser[date] = text

		recordsByTime = sorted(specificUser.items(),key = lambda d:d[0])
		firstLocationId = -1
		for record in recordsByTime:
			timeStamp = record[0]
			text = record[1]
			datas = text.split(",")
			date = datas[0]
			userid = datas[1]
			lac = int(datas[3])
			ci = int(datas[4])
			locationId = locations[(lac,ci)]
			if locationId != firstLocationId:
				writer.write("%s\t%s\t%s\t%s\n" % (date,timeStamp,userid,locationId))
				firstLocationId = locationId
	writer.close()
