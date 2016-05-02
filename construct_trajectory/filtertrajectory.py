# /usr/bin/python
# -*- coding=utf8 -*-
"""
   对生成的序列按照长度进行排序
"""
import sys
sys.path.append("../")
from config import *

MIN_RATIO = 0.2
MIN_LENGTH = 5

def getStringLen(text):
	charNum = {}
	for c in text:
		if not c in charNum:
			charNum[c] = 0
		charNum[c] += 1
	return len(charNum)

if __name__ == "__main__":
	sequences = []
	writer = open(FILTER_TRAJETORY,"w")
	t_number = 0
	for index, text in enumerate(open(USER_TRAJECTORY).readlines()):
		charText = text.split(":")[1]
		strCharLen = getStringLen(charText)
		if strCharLen >= MIN_LENGTH and (strCharLen*1.0/len(charText)) >= MIN_RATIO :
			writer.write("%d:%s" % (t_number, text))
			t_number += 1
	writer.close()
