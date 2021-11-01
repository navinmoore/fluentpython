# -*- coding:utf-8 -*-
# @Filename: main1.py
# @Date....: 2021-10-21 15:49
# @Author: yairs
from concurrent.futures import ProcessPoolExecutor, as_completed
from threading import Thread, enumerate

import asyncio
import time
import os
def func1(name):
    print("hello")
    time.sleep(10)
    print(name)
    return

async def func(name):
    print("hello")
    await asyncio.sleep(10)
    print(name)


# async def main():
#     """这个是顺序运行"""
#     f1 = func("1")
#     f2 = func("2")
#     f3 = func("3")
#     await f1
#     await f2
#     await f3
#
#
async def main():
    f1 = func("1")
    f2 = func("2")
    await asyncio.gather(*[f1, f2])


def sth():
    asyncio.run(main())
    return

# async def main():
#     tasks = [asyncio.create_task(func(name)) for name in ["1", "2", "3"]]
#     for task in tasks:
#         await task


# if __name__ == '__main__':
#     """协程 一个线程跑2个"""
#     start = time.perf_counter()
#     sth()
#     print(time.perf_counter() - start)

if __name__ == '__main__':
    """多进程 2个进程， 每个进程中跑一个线程的协程"""
    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=2) as executor:
        tasks = [executor.submit(sth) for _ in range(2)]
        as_completed(tasks)
    print(time.perf_counter() - start)
