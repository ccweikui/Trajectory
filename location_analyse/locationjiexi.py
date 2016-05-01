# /usr/bin/python
# -*- coding=utf8 -*-
"""
	用百度地图显示经纬度的所有坐标位置
"""
import sys
sys.path.append("../")
from config import *

if __name__ == "__main__":
	# 每个经纬度坐标点的标记
	location_labels = set()
	for index,text in enumerate(open(WEIBIAO_FILE).readlines()):
		if index == 0:
			continue
		datas = text.split()
		name = datas[0]
		lac = datas[1]
		ci = datas[2]
		longitude = datas[3]
		latitude = datas[4]
		if not (longitude, latitude) in location_labels:
			location_labels.add((longitude, latitude))

	
	for index,location in enumerate(location_labels):
		print "new BMap.Point(" + location[0] + "," + location[1] + "),\n",
