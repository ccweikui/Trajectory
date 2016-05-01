# /usr/bin/python
# -*- coding=utf8 -*-
"""
	用百度地图显示经纬度的所有坐标位置
"""
import sys
sys.path.append("../")
from config import *

def cmp(x, y):
	len_iter = min(len(x), len(y))
	for index in range(len_iter):
		if (x[index] < y[index]):
			return -1;
		elif x[index] > y[index]:
			return 1;
		else:
			continue
	return 0

if __name__ == "__main__":
	# 每个经纬度坐标点的标记
	writer = open("test.txt","w")
	location_writer = open("location_cluster.txt", "w")
	baidu_writer = open("baidu_show.txt", "w")
	pre_prefix = ""
	pre_name = ""
	location_cluster = {}
	index_name = []

	location_names = []
	for index,text in enumerate(open(WEIBIAO_FILE_NEW).readlines()):
		if index == 0:
			continue
		datas = text.split()
		name = datas[0]
		location_names.append(text.strip())
	
	location_names.sort(cmp)
	for text in location_names:
		datas = text.split()
		name = datas[0]
		n_prefix = name[:6]
		lac = datas[1]
		ci = datas[2]
		longitude = datas[3]
		latitude = datas[4]
		if pre_prefix == "" or n_prefix != pre_prefix:
			location_cluster[n_prefix] = set()
			index_name.append(n_prefix)
			pre_prefix = n_prefix
			#writer.write("%s\n" % ( name))
			writer.write("%s,%s\n" % (pre_name, name))
			pre_name = name
			#print pre_name,name
		if not (longitude,latitude) in location_cluster[n_prefix]:
			location_cluster[n_prefix].add((longitude,latitude))

	print len(location_cluster)
	#for index,key in enumerate(location_cluster):
	for index, key in enumerate(index_name):
		#writer.write("%s\n" % key)
		print index+1,key 
		location_writer.write("聚类:%s\n" % (index + 1))
		baidu_writer.write("聚类:%s\n" % (index + 1))
		for location in location_cluster[key]:
			location_writer.write("%s\t%s\n" % (location[0], location[1]))
			print "new BMap.Point(" + location[0] + "," + location[1] + "),"
			url = "new BMap.Point(" + location[0] + "," + location[1] + "),\n"
			baidu_writer.write(url)
			#writer.write("%s,%s\n" % (location[0], location[1]))
	location_writer.close()
	writer.close()
	baidu_writer.close()
