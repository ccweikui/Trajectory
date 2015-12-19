# /usr/bin/python
# -*- coding=utf8 -*-
"""
   该方法主要用来统计用户在基站之间的位置转移
   不同百分比的数量
"""
if __name__ == "__main__":
	users = {}	
	writer = open('output/result',"w")
	for text in open("../data/cdr_ler_20100916.TXT").readlines():
	#for text in open("../data/testfile").readlines():
		datas = text.split(",")
		date = datas[0]
		userid = datas[1]
		lac = datas[3]
		ci = datas[4]
		if (not userid in users):
			users[userid] = {}
			users[userid]['occur'] = 1
			users[userid]['move'] = 1
			users[userid]['loc'] = []
		else:
			users[userid]['occur'] += 1

		users[userid]['loc'].append((lac,ci))
	
	for userid in users:
		locationList = users[userid]['loc']
		length = len(locationList)
		for index,location in enumerate(locationList):
			if (index != length -1):
				nextLocation = locationList[index + 1]
				if (location[0] != nextLocation[0] or location[1] != nextLocation[1]):
					users[userid]['move'] += 1

	length = len(users)
	total = 0
	splitNumber = 6;
	for index,user in enumerate(users):
		total += users[user]['move']
		for i in range(splitNumber):
			if (index == length/splitNumber*(i+1)):
				print index,total
