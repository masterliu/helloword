# -*- coding: utf-8 -*-
# version：0.1
# note:该即用API接口只能查询当天天气信息，并且通过城市拼音输入进行城市参数传递
import urllib.request
import json
import collections

url = "http://apistore.baidu.com/microservice/weather?citypinyin="

city = input("输入你想查询城市的名称拼音:")

url = url + city  # 完整的URL
result = urllib.request.urlopen(url).read().decode("utf-8")
info = json.loads(result, object_pairs_hook=collections.OrderedDict)  # json格式转换为python格式，并指定为有序字典

if (info['errNum'] == -1):  # 查找失败
	print(info['errMsg'])
else:  # 输出天气相关信息
	print("你查询的当地天气信息如下：")
	print("地点：", info['retData']['city'])
	print("经度：", info['retData']['longitude'])
	print("纬度：", info['retData']['latitude'])
	print("查询日期：", info['retData']['date'])
	print("最新预报时间：", info['retData']['time'])
	print("天气：", info['retData']['weather'])
	print("海拔：", info['retData']['altitude'])
	print("最低气温：", info['retData']['temp'])
	print("最低气温：", info['retData']['l_tmp'])
	print("最高气温：", info['retData']['h_tmp'])
	print("风向：", info['retData']['WD'])
	print("风力：", info['retData']['WS'])
	print("日出时间：", info['retData']['sunrise'])
	print("日落时间：", info['retData']['sunset'])