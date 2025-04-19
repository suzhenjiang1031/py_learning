from threading import Thread
import time

def task(name):
    print(f"开始任务：{name}")
    time.sleep(1)
    print(f"完成任务：{name}")

threads = []
for i in range(5):
    t = Thread(target=task, args=(f'任务{i}',))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("全部任务完成（多线程）")
