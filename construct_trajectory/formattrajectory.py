# /usr/bin/python
# -*- coding=utf8 -*-
"""
   该方法主要用来将按照时间排序合并后的用户数据输出成轨迹
"""
import sys
sys.path.append("../")
from config import *

if __name__ == "__main__":
	#writer = open('output/format_trajectory_20100923.txt',"w")
	writer = open(USER_TRAJECTORY,"w")
	users = {}
	for index,text in enumerate(open(RECORD_SORTED_USER).readlines()):
		#if index > 1000:
		#	break;
		datas = text.split(",")
		userid = datas[2]
		label = datas[3].strip()
		if not userid in users:
			users[userid] = []
		users[userid].append(label)
	print "用户总数:%d" % len(users)
	sortedUsers = sorted(users.items(),key = lambda d:len(d[1]),reverse = True)
	for index, user in enumerate(sortedUsers):
		writer.write("%s:%s\n" % (user[0], "".join(user[1])))
	writer.close()
