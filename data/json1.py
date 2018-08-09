#coding:utf-8
# import json
# dic = {
#          'str': 'this is a string',
#          'list': [1, 2, 'a', 'b'],
#          'sub_dic': {
#                        'sub_str': 'this is sub str',
#                        'sub_list': [1, 2, 3]
#                      },
#          'end': 'end'
#        }
# #dump和dumps（从Python生成JSON）,dump会生成一个类文件对象，dumps会生成字符串
# e=json.dumps(dic)
# print e
import json
print([ i for i in dir(json) if not i.startswith('_')]) # 打印出这个json模块下面的方法
['JSONDecoder', 'JSONEncoder', 'decoder', 'dump', 'dumps', 'encoder', 'load', 'loads', 'scanner']
a = '{"name":"Seal","age":99}' #显然这是一个字符串
x = json.loads(a) # 使用json.loads 格式化为json数据或者叫转成字典
print x
print type(x)


b = {"name":"Seal","age":99}
y = json.dumps(b) # 使用json.dumps 把一个json格式数据或者叫字典转为字符串
print y
print type(y)


#c = "{'name':'Seal','age':99}" #显然这是一个字符串
#x = json.loads(c) # 我们再次使用json模块的loads方法,就会出现下面的错误
'''
ValueError                                Traceback (most recent call last)
<ipython-input-23-6bb448117314> in <module>()
----> 1 x = json.loads(a)

/usr/lib64/python2.7/json/__init__.pyc in loads(s, encoding, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kw)
    336             parse_int is None and parse_float is None and
    337             parse_constant is None and object_pairs_hook is None and not kw):
--> 338         return _default_decoder.decode(s)
    339     if cls is None:
    340         cls = JSONDecoder
/usr/lib64/python2.7/json/decoder.pyc in decode(self, s, _w)
    363
    364         """
--> 365         obj, end = self.raw_decode(s, idx=_w(s, 0).end())
    366         end = _w(s, end).end()
    367         if end != len(s):
/usr/lib64/python2.7/json/decoder.pyc in raw_decode(self, s, idx)
    379         """
    380         try:
--> 381             obj, end = self.scan_once(s, idx)
    382         except StopIteration:
    383             raise ValueError("No JSON object could be decoded")
ValueError: Expecting property name: line 1 column 2 (char 1)
 No JSON object could be decoded
 这说明的很明白,没有找到JSON的对象，因为用了单引号 并不是json格式数据了，当然就不能使用json的这个方法了
'''
'''
这时候eval出场了,eval是一个把你输入的字符串进行表达的函数，且还有2个参数是global 和local 全局是局部的属性
说简单点你输入是什么就返回的什么,比如 a="1+2" eval(a) 输出不是"1+2" 而是3,
eval()表达了1+2.在python中1+2 是数学运算所以输出是3，None和布尔是不能用eval()来表达了,
当然比如 a=' ' ,或者 a= '\n' 这种也同样不能被表达,
eval()能做的还有很多，这里不做展开了.有兴趣可以自己度娘一下 "eval()不安全"
'''

d = "{'name':'Seal','age':99}"
y = eval(d)
print type(y)