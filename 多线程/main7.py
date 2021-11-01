# -*- coding:utf-8 -*-
# @Filename: main7
# @Date....: 2021-10-21 17:41
# @Author: yairs
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed


def test(name):
    print("test:{0}\n".format(name))
    time.sleep(10)
    print("test:{0} end\n".format(name))


def td(tdname):
    with ThreadPoolExecutor(3) as tpool:
        t_tasks = [tpool.submit(test, name="{}".format(i)) for i in ["a", "b", "c"]]
        as_completed(t_tasks)
    print("{}.ending".format(tdname))


if __name__ == '__main__':
    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=2) as p:
        p_tasks = [p.submit(td, tdname=i) for i in ["p1", "p2"]]
        as_completed(p_tasks)

    print("main", time.perf_counter() - start)

