import asyncio
from multiprocessing import Process
from threading import Thread
import time

async def async_task(coroutine_id):
    print(f"[协程] 开始任务 {coroutine_id}")
    await asyncio.sleep(1) 
    print(f"[协程] 完成任务 {coroutine_id}")

def thread_worker(thread_id):
    print(f"[线程-{thread_id}] 启动")
    async def run_coroutines():
        tasks = [async_task(f"{thread_id}-协程{i}") for i in range(3)]
        await asyncio.gather(*tasks)

    asyncio.run(run_coroutines())
    print(f"[线程-{thread_id}] 结束")

def process_worker(process_id):
    print(f"--- 进程 {process_id} 启动 ---")
    threads = []
    for i in range(2): 
        t = Thread(target=thread_worker, args=(f"{process_id}-线程{i}",))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"--- 进程 {process_id} 结束 ---")

if __name__ == '__main__':
    start = time.time()
    processes = []

    for i in range(2):  # 启动两个进程
        p = Process(target=process_worker, args=(f"P{i}",))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    end = time.time()
    print(f"所有任务完成！总耗时：{end - start:.2f} 秒")
