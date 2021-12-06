import aiohttp
import asyncio

urls = [
    'https://img0.baidu.com/it/u=3247748179,4003876134&fm=26&fmt=auto&gp=0.jpg',
    'https://img1.baidu.com/it/u=1281293928,751127167&fm=26&fmt=auto&gp=0.jpg',
    'https://img1.baidu.com/it/u=3126771798,881592574&fm=26&fmt=auto&gp=0.jpg'
]


async def download(url):
    name = url.rsplit('/', 1)[1]
    img_path = './aiohttp/' + name
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(img_path, 'wb') as fp:
                fp.write(await response.content.read())


async def main():
    task = []
    for url in urls:
        task.append(asyncio.create_task(download(url)))
        await asyncio.wait(task, timeout=None)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
