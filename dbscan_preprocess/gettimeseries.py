# /usr/bin/python
# -*- coding=utf8 -*-
"""
   该方法主要用来从获取频繁模式对应的时间戳
"""
def getIndexList(text):
	text = text[1:len(text)-1]
	return [x.strip() for x in text.split(",")]

def getUserRecord(records):
	record = ""
	for x in records:
		record=record+x[0]
	return record

if __name__ == "__main__":
	locations = {}
	users = {}
	convertMap = {}
	for text in open("data/order_filter_sequence_20100923_0.4_10").readlines():
		datas = text.split(":")
		userid = datas[2].strip('\n')
		index = datas[0]
		convertMap[userid] = index
	for text in open("data/trajectorybyuser_20100923").readlines():
		#if index > 100:
		#	break;
		datas = text.split()
		timeStamp = datas[2]
		userid = str(datas[3])
		if userid in convertMap:
			indexId = convertMap[userid]
			locationId = datas[4].strip('\n')
			if not indexId in users:
				users[indexId] = []
			users[indexId].append((locationId,timeStamp))
	for text in open("data/order_filter_result_4_200_0.4").readlines():
		datas = text.split(":")
		frequentStr = datas[0].strip()
		support = datas[1]
		outputFilename = "output/result/%s_%s.txt" % (support,frequentStr) 
		writer = open(outputFilename,"w")
		indexSet = getIndexList(datas[2].strip('\n'))
		writer.write("%s:%s\n" % (frequentStr,support))
		for indexId in indexSet:
			userRecord = getUserRecord(users[indexId])
			startIndex = userRecord.index(frequentStr)
			endIndex = startIndex + len(frequentStr)
			writer.write("%s:%s\n" % (indexId,users[indexId][startIndex:endIndex]))
		writer.close()
