# /usr/bin/python
# -*- coding=utf8 -*-
"""
   该方法主要用来构建相应的距离矩阵,用于进行DBSCAN聚类操作
"""
import numpy as np
import math
from sklearn.cluster import DBSCAN

MAX_LIMIT = 10
EPS_VALUE = 220
MIN_SAMPLE = 100
K_VALUE = 1300

FIRST_RANGE_START = 1
FIRST_RANGE_END = 11
FIRST_RANGE_STEP = 1
SECOND_RANGE_START = 5
SECOND_RANGE_END = 6
SECOND_RANGE_STEP = 1

if __name__ == "__main__":
	for firstPara in range(FIRST_RANGE_START,FIRST_RANGE_END,FIRST_RANGE_STEP):
		for secondPara in range(SECOND_RANGE_START,SECOND_RANGE_END,SECOND_RANGE_STEP):
			#clusterResultFile = "cluster_result/%s_%s_%s_%s.txt" % (firstPara,secondPara,EPS_VALUE,MIN_SAMPLE)
			clusterResultFile = "cluster_result/%s_%s_%s_%s_%s.txt" % (EPS_VALUE,MIN_SAMPLE,K_VALUE,firstPara,secondPara)
			print clusterResultFile
			writer = open(clusterResultFile,"w")
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
				timeDiff = np.zeros((length,length))
				for i in range(length):
					for j in range(i,length):
						if i == j:
							timeDiff[i][j] = 0
						else:
							timeDiff[j][i] = timeDiff[i][j] = math.sqrt((timeDiffTrans[i][j] * firstPara + timeDiffStretch[i][j] * secondPara * K_VALUE)/10)/len(frequentStr)
				clusters = DBSCAN(eps=EPS_VALUE, min_samples=MIN_SAMPLE,metric="precomputed").fit(timeDiff)
				clusterSupport = {}
				for index in clusters.labels_:
					indexStr = "%s_%s_%s" % (support,frequentStr,index)
					if not indexStr in clusterSupport:
						clusterSupport[indexStr] = 0
					clusterSupport[indexStr] += 1
				writer.write("%s\n" % clusterSupport)
			writer.close()
		#print clusters.core_sample_indices_
