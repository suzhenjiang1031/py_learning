from multiprocessing import Process
import time

def task(name):
    print(f"开始任务：{name}")
    time.sleep(1)
    print(f"完成任务：{name}")

if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = Process(target=task, args=(f'任务{i}',))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print("全部任务完成（多进程）")
