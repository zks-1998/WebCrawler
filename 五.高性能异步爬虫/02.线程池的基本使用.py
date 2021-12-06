import time
# 导入线程池模块对应的类
from multiprocessing.dummy import Pool

start_time = time.time()

name_list = ['kun', 'song']


def get_name(str):
    print("正在下载", str)
    time.sleep(2)
    print("下载完成", str)


pool = Pool(4)
pool.map(get_name, name_list)
end_time = time.time()

print(end_time - start_time)
