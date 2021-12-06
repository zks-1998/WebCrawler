import requests

urls = [
    'https://www.taobao.com/?spm=a2e0b.20350158.1581860521.1.7a86468a31XzZ1&pid=mm_26632258_3504122_32538762&union_lens=recoveryid%3A201_11.92.48.12_813575_1628819388821%3Bprepvid%3A201_11.92.48.12_813575_1628819388821&clk1=a816034ee7c939eaadaade2a1f22c3c3?spm=a2e0b.20350158.1581860521.1.7a86468a31XzZ1&pid=mm_26632258_3504122_32538762&union_lens=recoveryid%3A201_11.92.48.12_813575_1628819388821%3Bprepvid%3A201_11.92.48.12_813575_1628819388821&clk1=a816034ee7c939eaadaade2a1f22c3c3',
    'https://union-click.jd.com/sem.php?source=baidu-pinzhuan&unionId=288551095&siteId=baidupinzhuan_0f3d30c8dba7459bb52f2eb5eba8ac7d&to=https%3a%2f%2fwww.jd.com',
    'https://www.tencent.com/zh-cn'
]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36 '
}


def get_text(url):
    print("正在爬取", url)
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.text


def get_len(text):
    print("长度为：", len(text))


for url in urls:
    response = get_text(url)
    get_len(response)
