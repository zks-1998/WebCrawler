import asyncio


async def func1():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '返回值'


async def func2():
    print(3)
    await asyncio.sleep(2)
    print(4)
    return '返回值'


async def main():
    print('main开始')
    task_list = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2())
    ]

    await asyncio.wait(task_list, timeout=None)


asyncio.run(main())
