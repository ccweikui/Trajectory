# /usr/bin/python
# -*- coding=utf8 -*-
"""
	此方法主要统计每个经纬度基站位置上的统计信息
	每个位置可能包含多个基站
"""
if __name__ == "__main__":
	#数据集中总用户数量
	USERNUMBER = 474080
	locations = {}
	station_location = {}
	writer = open('output/result_location',"w")
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
			locations[(longitude,latitude)] = {}
		locations[(longitude,latitude)][(lac,ci)] = {}
		locations[(longitude,latitude)][(lac,ci)]['name'] = name
		locations[(longitude,latitude)][(lac,ci)]['usercount'] = 0
		station_location[(lac,ci)] = (longitude,latitude)
	for text in open("output/result").readlines():
		datas = text.split()
		lac = datas[0]
		ci = datas[1]
		usercount = int(datas[2])
		locations[station_location[(lac,ci)]][(lac,ci)]['usercount'] = usercount
	for location in locations:
		print location,locations[location]
	
	writer.write("经度\t纬度\t基站数目\t包含用户\t占总人数百分比\n")
	sortedlocations = sorted(locations.items(),key = lambda d:sum([ int(d[1][x]['usercount']) for x in d[1] ]),reverse = True)
	for location in sortedlocations:
		usercountTotal = sum([location[1][x]['usercount'] for x in location[1]])
		writer.write("%s\t%s\t%d\t%d\t%.4f\n" % (location[0][0],location[0][1],len(location[1]),usercountTotal,usercountTotal*1.0/USERNUMBER))
		print "%s\t%s\t%d\t%d\t%.4f\n" % (location[0][0],location[0][1],len(location[1]),usercountTotal,usercountTotal*1.0/USERNUMBER)
	writer.close()
