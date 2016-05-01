# /usr/bin/python
# -*- coding=utf8 -*-
"""
   对生成的序列按照长度进行排序
"""
if __name__ == "__main__":
	sequences = []
	#writer = open('output/trajectorybyuser_test',"w")
	writer = open('output/ordersequence_20100916',"w")
	#for text in open("data/format_trajectory_20100923.txt").readlines():
	for text in open("output/char_trajectory_20100916.txt").readlines():
	#for text in open("data/testfile").readlines():
		sequences.append(text)
	sortedSequence = sorted(sequences,key=lambda x:len(x),reverse=True)
	for sequence in sortedSequence:
		writer.write("%s" % sequence)
		print len(sequence)
	writer.close()
