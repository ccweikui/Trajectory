# /usr/bin/python
# -*- coding=utf8 -*-
"""
   该方法主要用来构建相应的距离矩阵,用于进行DBSCAN聚类操作
"""
import numpy as np
import math
from sklearn.cluster import DBSCAN

if __name__ == "__main__":
	MAX_LIMIT = 1
	transDiff = 0
	stretchDiff = 0
	average = 0
	count = 0
	averageList = []
	for index,text in enumerate(open("data/order_filter_result_4_200_0.4").readlines()):
		if index >= MAX_LIMIT:
			break
		datas = text.split(":")
		frequentStr = datas[0].strip()
		support = datas[1]
		#Distance Matrix
		transFilename = "npy/%s_%s_trans.npy" % (support,frequentStr)
		stretchFilename = "npy/%s_%s_stretch.npy" % (support,frequentStr)
		timeDiffTrans = np.load(transFilename)
		timeDiffStretch = np.load(stretchFilename)
		(length,length) = timeDiffTrans.shape
		print length
		for i in range(length):
			for j in range(i,length):
				if i != j:
					transDiff += timeDiffTrans[i][j]/1000
					stretchDiff += timeDiffStretch[i][j]/1000
					averageList.append(int(timeDiffTrans[i][j]/timeDiffStretch[i][j]))
					#print timeDiffTrans[i][j],timeDiffStretch[i][j],timeDiffTrans[i][j]/timeDiffStretch[i][j]
		print transDiff,stretchDiff,transDiff/stretchDiff
		listLength = len(averageList)
		print listLength
		averageList.sort()
		for i in range(9):
			print averageList[(i+1)*listLength/10]
