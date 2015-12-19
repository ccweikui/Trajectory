# /usr/bin/python
# -*- coding=utf8 -*-
"""
   该方法主要用来构建相应的距离矩阵,用于进行DBSCAN聚类操作
"""
import numpy as np
import math
from sklearn.cluster import DBSCAN

FIRST_PARA = 0.5
SECOND_PARA = 0.5
EPS_VALUE = 400
MIN_SAMPLE = 100

if __name__ == "__main__":
	MAX_LIMIT = 2
	for index,text in enumerate(open("data/order_filter_result_4_200_0.4").readlines()):
		if index > MAX_LIMIT:
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
		timeDiff = np.zeros((length,length))
		for i in range(length):
			for j in range(i,length):
				if i == j:
					timeDiff[i][j] = 0
				else:
					timeDiff[j][i] = timeDiff[i][j] = math.sqrt(timeDiffTrans[i][j] * FIRST_PARA + timeDiffStretch[i][j] * SECOND_PARA)/len(frequentStr)
		clusters = DBSCAN(eps=EPS_VALUE, min_samples=MIN_SAMPLE,metric="precomputed").fit(timeDiff)
		clusterSupport = {}
		for index in clusters.labels_:
			indexStr = "%s_%s_%s" % (support,frequentStr,index)
			if not indexStr in clusterSupport:
				clusterSupport[indexStr] = 0
			clusterSupport[indexStr] += 1
		print clusterSupport
		#print clusters.core_sample_indices_
