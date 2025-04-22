import asyncio
import aiohttp
from multiprocessing import Process
from threading import Thread
import time

URLS = [
    "https://example.com",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/uuid",
    "https://httpbin.org/get",
]

async def fetch(session, url):
    print(f"开始请求：{url}")
    async with session.get(url) as response:
        result = await response.text()
        print(f"完成请求：{url}，响应长度：{len(result)}")
        return result

async def run_coroutines(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)

def thread_worker(thread_id, urls):
    print(f"[线程 {thread_id}] 启动")
    asyncio.run(run_coroutines(urls))
    print(f"[线程 {thread_id}] 结束")

def process_worker(process_id):
    print(f"=== 进程 {process_id} 启动 ===")
    threads = []
    urls_per_thread = len(URLS) // 2

    for i in range(2): 
        t_urls = URLS[i * urls_per_thread : (i + 1) * urls_per_thread]
        t = Thread(target=thread_worker, args=(f"{process_id}-线程{i}", t_urls))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"=== 进程 {process_id} 结束 ===")

if __name__ == '__main__':
    start = time.time()
    processes = []

    for i in range(2): 
        p = Process(target=process_worker, args=(f"P{i}",))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    end = time.time()
    print(f"所有任务完成，总耗时：{end - start:.2f} 秒")
