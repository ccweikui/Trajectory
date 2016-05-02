# /usr/bin/python
# -*- coding=utf8 -*-
"""
	此方法将基站信息转换成地理位置的标号标记
	主要标记通过label文件中标记进行表示
"""
import sys
sys.path.append("../")
from config import *

if __name__ == "__main__":
	#数据集中总用户数量
	writer = open(LOCATION_LABEL,"w")
	labels = [label.strip() for label in open(LABEL_FILE).readlines()]
	print labels
	# 每个经纬度坐标点的标记
	location_labels = {}
	# 每个基站的标记
	station_labels = {}
	index = -1
	gps_maps = {}

	for text in open(WEIBIAO_FILE_NEW).readlines():
		datas = text.split()
		longitude = datas[3]
		latitude = datas[4]
		glongitude = datas[5]
		glatitude = datas[6]
		gps_maps[(glongitude,glatitude)] = (longitude, latitude)

	for text in open(LOCATION_CLUSTER).readlines():
		if "聚类" in text:
			index += 1;
			continue
		datas = text.split()
		if len(datas) != 3:
			continue
		glongitude = datas[0]
		glatitude = datas[1]
		location_labels[gps_maps[(glongitude, glatitude)]] = labels[index]
		print labels[index]

	print index
	print len(location_labels)

	for index,text in enumerate(open(WEIBIAO_FILE).readlines()):
		if index == 0:
			continue
		datas = text.split()
		name = datas[0]
		lac = datas[1]
		ci = datas[2]
		longitude = datas[3]
		latitude = datas[4]
		if (longitude, latitude) in location_labels:
			station_labels[(lac,ci)] = location_labels[(longitude, latitude)]
	print len(station_labels)
	covered = 0
	uncovered = 1
	for index,text in enumerate(open(ORIGIN_FILE).readlines()):
	#for index,text in enumerate(open("../data/testfile").readlines()):
		datas = text.split(",")
		date = datas[0]
		userid = datas[1]
		lac = datas[3]
		ci = datas[4]
		if (lac, ci) in station_labels:
			writer.write("%s,%s,%s\n" % (date,userid,station_labels[(lac,ci)]))
			covered += 1
		else :
			uncovered += 1
	print "总记录:%d\t覆盖记录:%d\t覆盖比率:%s" % (uncovered + covered, covered, covered * 1.0 / (uncovered + covered))
	writer.close()
