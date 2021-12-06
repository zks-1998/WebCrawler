import re

# findall:匹配字符串中所有的符合正则的内容 返回一个列表
lst = re.findall(r"\d+", "我的QQ1355776458，我的电话17852422531")
print(lst)   # ['1355776458', '17852422531']

# finditer: 匹配字符串中所有的符合正则的内容，返回的是迭代器
it = re.finditer(r"\d+", "我的QQ1355776458，我的电话17852422531")
for i in it:
    print(i.group())

# match是从头开始匹配一个符合的返回
sm = re.match(r"\d+", "10086,123")
print(sm.group())

# search找到一个就返回 不一定从头开始
ss = re.search(r"\d+", "song1355776458")
print(ss.group())

# compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用
pattern = re.compile(r"\d+")
sc = pattern.match("123456")
print(sc.group())
