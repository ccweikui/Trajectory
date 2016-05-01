# /usr/bin/python
# -*- coding=utf8 -*-
"""
	此方法主要统计每个经纬度基站位置上的统计信息
	每个位置可能包含多个基站
	输出按照从多到少顺序输出
"""
import sys
sys.path.append("../")
from config import *

if __name__ == "__main__":
	users = set()
	locations = {}
	station_location = {}
	writer = open(LOCATION_STAT,"w")
	# 处理基站的地址
	for index,text in enumerate(open(WEIBIAO_FILE).readlines()):
		if index == 0:
			continue
		datas = text.split()
		name = datas[0]
		lac = datas[1]
		ci = datas[2]
		longitude = datas[3]
		latitude = datas[4]
		if (not (longitude,latitude) in locations):
			locations[(longitude,latitude)] = {}
			locations[(longitude,latitude)]['station'] = 0
			locations[(longitude,latitude)]['user'] = set()
		locations[(longitude,latitude)]['station'] += 1
		station_location[(lac,ci)] = (longitude,latitude)
	for text in open(ORIGIN_FILE).readlines():
	#for text in open("../data/testfile").readlines():
		datas = text.split(",")
		date = datas[0]
		userid = datas[1]
		lac = datas[3]
		ci = datas[4]
		longitude, latitude = station_location[(lac, ci)]
		locations[(longitude,latitude)]['user'].add(userid)
		users.add(userid)
	sortedLocations = sorted(locations.items(),key = lambda d:len(d[1]['user']),reverse = True)
	
	writer.write("经度\t纬度\t基站数目\t包含用户\t占总人数百分比\n")
	userNumber = len(users)
	print "用户总数:%d" % userNumber
	for location in sortedLocations:
		writer.write("%s\t%s\t%d\t%d\t%.4f\n" % (location[0][0],location[0][1],location[1]['station'], len(location[1]['user']), len(location[1]['user']) * 1.0 / userNumber))
		#print "%s\t%s\t%d\t%d\t%.4f\n" % (location[0][0],location[0][1],location[1]['station'], len(location[1]['user']), len(location[1]['user']) * 1.0 / userNumber)
	writer.close()
