# /usr/bin/python
# -*- coding=utf8 -*-
"""
	用字母表对基站进行编号
	此方法主要统计每个经纬度基站位置上的位置进行编号
"""
if __name__ == "__main__":
	alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
			"q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G",
			"H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X",
			"Y","Z","0","1","2","3","4","5","6","7","8","9"]
	locationmarks = {}
	locations = {}
	writer = open('output/result_location_mark_char',"w")
	for index,text in enumerate(open("../data/weibiao.txt").readlines()):
		if index == 0:
			continue
		datas = text.split()
		name = datas[0]
		lac = datas[1]
		ci = datas[2]
		longitude = datas[3]
		latitude = datas[4]
		if (not (longitude,latitude) in locations):
			locations[(longitude,latitude)] = []
		locations[(longitude,latitude)].append((lac,ci))

	for index,text in enumerate(open("output/result_location").readlines()):
		if index == 0:
			continue
		if index > len(alphabet):
			break
		datas = text.split()
		longitude = datas[0]
		latitude = datas[1]
		locationmarks[(longitude,latitude)] = alphabet[index-1]

	writer.write("lac\tci\t编号\t经度\t纬度\n")
	for index,location in enumerate(locations):
		if location in locationmarks:
			print locationmarks[location],location[0],location[1]
			for (lac,ci) in locations[location]:
				writer.write("%s\t%s\t%s\t%s\t%s\n" % (lac,ci,locationmarks[location],location[0],location[1]))
