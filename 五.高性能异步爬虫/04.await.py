import asyncio


async def others():
    print('start')
    await asyncio.sleep(2)
    print('end')
    return '返回值'


async def func():
    print('执行内部代码开始')
    response = await others()  # await必须要收到返回值才能继续执行代码
    print('IO结果为', response)


asyncio.run(func())
