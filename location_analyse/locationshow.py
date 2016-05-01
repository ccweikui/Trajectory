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

	url = "http://api.map.baidu.com/staticimage/v2?ak=tMOqfmvxDxbKYXB4G8bYj51G&center="
	for index,location in enumerate(location_labels):
		if index >= 50:
			break
		if index != 0:
			url += "|"
		else:
			url += location[0] + "," + location[1] + "width=1024&height=500&zoom=15&markers="

		url = url + location[0] + "," + location[1]
	url += "&markerStyles=l,A|m,B|l,C|l,D|m,E|,|l,G|m,H"
	print url
