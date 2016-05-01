# /usr/bin/python
# -*- coding=utf8 -*-
"""
	此方法主要统计每个经纬度基站位置上的位置进行编号
"""
if __name__ == "__main__":
	locations = {}
	writer = open('output/result_location_mark',"w")
	for index,text in enumerate(open("../data/weibiao.txt").readlines()):
		if index == 0:
			continue
		datas = text.split()
		name = datas[0]
		lac = datas[1]
		ci = datas[2]
		longitude = datas[3]
		latitude = datas[4]
		if (not (longitude,latitude) in locations):
			locations[(longitude,latitude)] = []
		locations[(longitude,latitude)].append((lac,ci))

	writer.write("lac\tci\t编号\t经度\t纬度\n")
	for index,location in enumerate(locations):
		print index,location[0],location[1]
		for (lac,ci) in locations[location]:
			writer.write("%s\t%s\t%s\t%s\t%s\n" % (lac,ci,index,location[0],location[1]))
