# -*- coding=utf8 -*-
import sys
import urllib2
import json
from config import *

class BaiduToGoogle:
	"""
	将百度坐标转换成谷歌坐标
	"""
	def __init__(self):
		self.stations = {}
		self.uniq_station = []

	def getHouseList(self):
		writer = open("weibiao_new.txt","w")
		for index, text in enumerate(open("weibiao.txt")):
			if index == 0:
				continue
			records = text.split()
			longitude = records[3]
			latitude = records[4]
			if (longitude, latitude) not in self.stations:
				self.stations[(longitude,latitude)] = {}
				self.uniq_station.append(text)

		for text in self.uniq_station:
			records = text.split()
			longitude = records[3]
			latitude = records[4]
			glongitude,glatitude = self.toGoogle(longitude,latitude)
			url = "new BMap.Point(" + str(glongitude) + "," + str(glatitude )+ "),"
			writer.write("%s\t%s\t%s\t%s\n" % (text.strip(), glongitude, glatitude, url))

	def toGoogle(self,longitude,latitude):
		"""
		使用地址服务将百度坐标转换成Google坐标
		"""
		requestUrl = DecodeUrl + "lng=" + str(longitude) + "&lat=" + str(latitude)
		content = self.sendRequest(requestUrl)
		originContent = content.decode('gb2312','ignore').encode('utf-8')
		originContent = json.loads(originContent)
		
		print originContent
		if ('State' in originContent):
			status = originContent['State']
			if (status):
				longitude = originContent['Lng']
				latitude = originContent['Lat']
			else:
				longitude = Longitute 
				latitude = Latitude
		else:
			longitude = Longitute 
			latitude = Latitude
		return (longitude,latitude)

	def sendRequest(self,requestUrl):
		"""
		使用百度地图接口获取经纬度信息
		发送请求并处理超时情况
		"""
		print requestUrl
		count = 0
		timeOut = True
		content = "{}"
		while (count < RetryCount and timeOut):
			count += 1
			print count
			try:
				request = urllib2.Request(requestUrl)
				content = urllib2.urlopen(request,timeout=10).read()
				timeOut = False
			except urllib2.URLError, e:  
				print e
			except Exception ,e:
				print e
			if timeOut:
				time.sleep(2 * count)
		return content

if __name__ == '__main__':
	baiduToGoogle = BaiduToGoogle()
	baiduToGoogle.getHouseList()
