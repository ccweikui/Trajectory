# /usr/bin/python
# -*- coding=utf8 -*-
"""
   对生成的序列按照长度进行排序
"""
MIN_RATIO = 0.4
MIN_LENGTH = 10

def getStringLen(text):
	charNum = {}
	for c in text:
		if not c in charNum:
			charNum[c] = 0
		charNum[c] += 1
	return len(charNum)

if __name__ == "__main__":
	sequences = []
	#writer = open('output/trajectorybyuser_test',"w")
	writer = open('output/order_filter_sequence_20100923_0.4_10',"w")
	#for text in open("data/format_trajectory_20100923.txt").readlines():
	for text in open("output/char_trajectory_20100916.txt").readlines():
	#for text in open("data/testfile").readlines():
		charText = text.split(":")[0]
		strCharLen = getStringLen(charText)
		if strCharLen >= MIN_LENGTH and (strCharLen*1.0/len(charText)) >= MIN_RATIO :
			sequences.append(text)
	sortedSequence = sorted(sequences,key=lambda x:len(x),reverse=True)
	for index,sequence in enumerate(sortedSequence):
		writer.write("%s:%s" % (index,sequence))
	writer.close()
