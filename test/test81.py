import psutil
import time
import pyttsx3
from datetime import datetime
import csv

# 设置监控的目标应用（大小写不敏感）
TARGET_APPS = ['chrome.exe', 'LeagueClient.exe', 'douyin.exe']  # 可修改
REMIND_INTERVAL = 60 * 10  # 每隔 10 分钟提醒一次
MAX_RUNTIME = 60 * 30      # 运行超过 30 分钟触发提醒

# 初始化语音引擎
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print(f"[语音提示] {text}")
    engine.say(text)
    engine.runAndWait()

def log_usage(app_name, duration):
    with open("usage_log.csv", "a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), app_name, round(duration / 60, 2)])

def monitor_apps():
    print("开始监控应用运行时间（Ctrl+C 退出）")
    app_start_time = {}

    while True:
        time.sleep(5)
        running_apps = [p.info['name'] for p in psutil.process_iter(['name']) if p.info['name']]

        for app in TARGET_APPS:
            if app in running_apps:
                if app not in app_start_time:
                    app_start_time[app] = time.time()
                else:
                    duration = time.time() - app_start_time[app]
                    if duration > MAX_RUNTIME and int(duration) % REMIND_INTERVAL < 5:
                        speak(f"你已经使用 {app} 超过半小时了，建议休息一下。")
                        log_usage(app, duration)
            else:
                if app in app_start_time:
                    total_time = time.time() - app_start_time[app]
                    log_usage(app, total_time)
                    print(f"{app} 使用结束，共用时 {round(total_time / 60, 2)} 分钟")
                    del app_start_time[app]

if __name__ == '__main__':
    try:
        monitor_apps()
    except KeyboardInterrupt:
        print("\n已退出程序")
