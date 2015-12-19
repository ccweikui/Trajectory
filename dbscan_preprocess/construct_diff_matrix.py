# /usr/bin/python
# -*- coding=utf8 -*-
"""
   该方法主要用来构建相应的距离矩阵,用于进行DBSCAN聚类操作
"""
import numpy as np
import math
import thread
import time

def getTimeStampArray(timeStr):
	timeStr = timeStr[1:len(timeStr)-1]
	timeArray = timeStr.split("),")
	return [int(timestamp.strip()[7:17]) for timestamp in timeArray]

def computeEachDiff(listA,listB):
	diffTrans = 0
	diffStretch = 0
	for index in range(len(listA)-1):
		firstStampA = listA[index]
		nextStampA = listA[index+1]
		firstStampB = listB[index]
		nextStampB = listB[index+1]
		diffTrans += math.pow(firstStampA-firstStampB,2)
		diffStretch += math.pow(nextStampA-firstStampA-nextStampB+firstStampB,2)
	diffTrans += math.pow(listA[-1]-listB[-1],2)
	return (diffTrans,diffStretch)

def process(fileName):
	multiStampArray = []
	frequentStr = ""
	support = 0
	for index,text in enumerate(open(fileName).readlines()):
		if index == 0:
			frequentStr = text.split(":")[0]
			support = text.split(":")[1].strip("\n")
			continue
		datas = text.split(":")
		timeStr = datas[1].strip('\n')
		multiStampArray.append(getTimeStampArray(timeStr))
	length =  len(multiStampArray)
	print frequentStr,support,length
	#Distance Matrix
	timeDiffTrans = np.zeros((length,length))
	timeDiffStretch = np.zeros((length,length))
	for i in range(length):
		for j in range(i,length):
			if i != j:
				(diffTrans,diffStretch) = computeEachDiff(multiStampArray[i],multiStampArray[j])
				timeDiffTrans[j][i] = timeDiffTrans[i][j] = diffTrans
				timeDiffStretch[j][i] = timeDiffStretch[i][j] = diffStretch
	transFilename = "npy/%s_%s_trans.npy" % (support,frequentStr)
	stretchFilename = "npy/%s_%s_stretch.npy" % (support,frequentStr)
	np.save(transFilename,timeDiffTrans)
	np.save(stretchFilename,timeDiffStretch)

if __name__ == "__main__":
	MAX_LIMIT = 10
	for index,text in enumerate(open("data/order_filter_result_4_200_0.4").readlines()):
		if index > MAX_LIMIT:
			break
		datas = text.split(":")
		frequentStr = datas[0].strip()
		support = datas[1]
		outputFilename = "output/result/%s_%s.txt" % (support,frequentStr) 
		print outputFilename
		process(outputFilename)
		#thread.start_new_thread(process,(outputFilename,))
		#time.sleep(30)
