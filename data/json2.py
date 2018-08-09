#coding:utf-8
import json
#load和loads（解析JSON成Python的数据类型）,load和loads分别解析类文件对象和字符串格式的JSON
s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')

print s

print s.keys()

print s["name"]

print s["type"]["name"]

print s["type"]["parameter"][1]