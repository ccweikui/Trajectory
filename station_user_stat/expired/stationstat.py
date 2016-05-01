# /usr/bin/python
# -*- coding=utf8 -*-
"""
	此方法主要统计每个基站位置上每天存在记录的用户数量
"""
if __name__ == "__main__":
	stations = {}	
	writer = open('output/result',"w")
	for text in open("../data/cdr_ler_20100916.TXT").readlines():
	#for text in open("../data/testfile").readlines():
		datas = text.split(",")
		date = datas[0]
		userid = datas[1]
		lac = datas[3]
		ci = datas[4]
		if (not (lac,ci) in stations):
			stations[(lac,ci)] = set()
		stations[(lac,ci)].add(userid)
	
	sortedStations = sorted(stations.items(),key = lambda d:len(d[1]),reverse = True)
	for station in sortedStations:
		writer.write("%s\t%s\t%d\n" % (station[0][0],station[0][1],len(station[1])))
	writer.close()
