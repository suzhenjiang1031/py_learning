import asyncio

async def task(name):
    print(f"开始任务：{name}")
    await asyncio.sleep(1)
    print(f"完成任务：{name}")

async def main():
    tasks = [task(f'任务{i}') for i in range(5)]
    await asyncio.gather(*tasks)

asyncio.run(main())
print("全部任务完成（协程）")
