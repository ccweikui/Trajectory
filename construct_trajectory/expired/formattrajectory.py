# /usr/bin/python
# -*- coding=utf8 -*-
"""
   该方法主要用来将用户数据转换成适合处理的格式
"""
if __name__ == "__main__":
	locations = {}
	#writer = open('output/trajectorybyuser_test',"w")
	writer = open('output/format_trajectory_20100923.txt',"w")
	preUserId = ""
	index = 0
	for text in open("data/trajectorybyuser_20100923").readlines():
	#for text in open("data/testfile").readlines():
		#if index > 100:
		#	break;
		datas = text.split()
		userid = datas[3]
		locationId = datas[4]
		if (preUserId and userid != preUserId):
			writer.write("-2\n")
			index += 1
		writer.write("%s -1 " % locationId)
		preUserId = userid
	writer.close()
