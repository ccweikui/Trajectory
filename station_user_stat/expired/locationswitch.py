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
	locations_num = {}
	station_location = {}
	num = 1
	writer = open('output/data_switch',"w")
	for index,text in enumerate(open("../data/weibiao.txt").readlines()):
		if index == 0:
			continue
		datas = text.split()
		name = datas[0]
		lac = datas[1]
		ci = datas[2]
		longitude = datas[3]
		latitude = datas[4]
		if (not (longitude,latitude) in locations_num):
			locations_num[(longitude,latitude)] = num
			num += 1
		station_location[(lac,ci)] = locations_num[(longitude,latitude)]
	for index,text in enumerate(open("../data/cdr_ler_20100916.TXT").readlines()):
		datas = text.split(",")
		date = datas[0]
		userid = datas[1]
		lac = datas[3]
		ci = datas[4]
		writer.write("%s,%s,%d\n" % (date,userid,station_location[(lac,ci)]))
	writer.close()
