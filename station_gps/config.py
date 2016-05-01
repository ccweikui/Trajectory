# -*- coding=utf8 -*-

#百度乐居学区方的根URL
RootUrl = "http://esf.baidu.com/bj/house/a100-m6-k5-n"

#获取学区房ID时的URL前缀
PrefixURL = "http://esf.baidu.com/bj/detail/"

#总计页数
TotalPage = 5

#百度地址转换的url
GeoCoding = "http://api.map.baidu.com/geocoder/v2/?output=json&ak=m96zoqEc8tqcWhg3ZkHxqKm5&address="

#百度坐标转Google坐标的URL
DecodeUrl = "http://ditujiupian.com/service/api.ashx?key=263b97a6839f4cea8ab0bd106aaf5d12&type=wgs2bd&"

#失败时的经度
Longitute = 0
Latitude = 0

#设置超时重试次数
RetryCount = 5

#设置获取每页信息休眠时间
PagePerTime = 1

#链家每页暂停时间
HM_PagePerTime =  3

#地址转换成坐标时每次处理数据量
PageNumber = 20
