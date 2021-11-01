# -*- coding:utf-8 -*-
# Author: your name
# Date: 2021-10-21 10:19:01
# LastEditTime: 2021-10-21 11:30:27
# LastEditors: Please set LastEditors
# Description: In User Settings Edit
# FilePath: /fluentpython/main.py
# 
import time
import os
from multiprocessing.dummy import Pool 
import asyncio

async def func(msg):
    print("input:{}".format(msg))
    await asyncio.sleep(5)
    print('end')
    return 


# async def main():
#     """顺序执行"""
#     f1 = func('msg1') 
#     f2 = func('msg2') 
#     f3 = func('msg3') 
#     f4 = func('msg4') 
#     await f1 
#     await f2
#     await f3 
#     await f4

async def main():
    """并发执行"""
    f1 = asyncio.create_task(func('msg1'))
    f2 = asyncio.create_task(func('msg2'))
    f3 = asyncio.create_task(func('msg3') )
    f4 = asyncio.create_task(func('msg4') )
    await f1 
    await f2
    await f3 
    await f4
   
    

if __name__ == '__main__':
    # pool = Pool(processes=3)

    # pool.apply_async(func, args=('msg1',))
    # pool.apply_async(func, args=('msg2',))
    # pool.apply_async(func, args=('msg3',))
    # pool.apply_async(func, args=('msg4',))
    # start = time.perf_counter()
    # pool.close()
    # pool.join()
    # print(time.perf_counter()-start)
    start = time.perf_counter()
    asyncio.run(main())
    print(time.perf_counter()-start)
