import requests

url = 'https://bkimg.cdn.bcebos.com/pic/42166d224f4a20a4aa594a339b529822730ed0fb?x-bce-process=image/resize,m_lfit,w_268,limit_1/format,f_jpg'
# text字符串 content二进制 json()对象
img_data = requests.get(url=url).content

with open('./subingtian.jpg', 'wb') as fp:
    fp.write(img_data)


