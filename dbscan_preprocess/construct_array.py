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

if __name__ == "__main__":
	for text in open("output/result_test.txt").readlines():
		if len(text) > 20:
			continue
		frequentStr = text.split(":")[1].strip("\n")
		#Distance Matrix
		transFilename = "npy/%s_trans.npy" % (frequentStr)
		stretchFilename = "npy/%s_stretch.npy" % (frequentStr)
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
					timeDiff[j][i] = timeDiff[i][j] = math.sqrt(timeDiffTrans[i][j] * FIRST_PARA + timeDiffStretch[i][j] * SECOND_PARA)
		clusters = DBSCAN(eps=4000, min_samples=100,metric="precomputed").fit(timeDiff)
		print clusters.labels_
		print clusters.core_sample_indices_
