# /usr/bin/python
# -*- coding=utf8 -*-
"""
   该方法主要用来统计每个用户的记录,
   将相同用户的记录放在一起
"""
if __name__ == "__main__":
	users = {}	
	writer = open('output/locationbyuser',"w")
	for text in open("../data/cdr_ler_20100916.TXT").readlines():
	#for text in open("../data/testfile").readlines():
		datas = text.split(",")
		date = datas[0]
		userid = datas[1]
		lac = datas[3]
		ci = datas[4]
		if (not userid in users):
			users[userid] = []
		users[userid].append(text)
	
	for userid in users:
		for text in users[userid]:
			writer.write("%s" % (text))
	writer.close()
