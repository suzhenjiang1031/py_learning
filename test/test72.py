import requests
import tkinter as tk
from tkinter import messagebox

# 替换为你自己的 Key
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'https://devapi.qweather.com/v7/weather/now'
CITY_LOOKUP_URL = 'https://geoapi.qweather.com/v2/city/lookup'

def get_city_id(city_name):
    """根据城市名称获取城市ID（location）"""
    params = {
        'location': city_name,
        'key': API_KEY
    }
    response = requests.get(CITY_LOOKUP_URL, params=params)
    data = response.json()
    if data['code'] == '200' and data['location']:
        return data['location'][0]['id']
    else:
        return None

def get_weather(city_name):
    """获取并返回天气信息字符串"""
    city_id = get_city_id(city_name)
    if not city_id:
        return "城市名称无效或找不到该城市。"

    params = {
        'location': city_id,
        'key': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data['code'] == '200':
        weather = data['now']
        return f"""城市：{city_name}
天气状况：{weather['text']}
温度：{weather['temp']}°C
风向：{weather['windDir']}
风速：{weather['windSpeed']} km/h
体感温度：{weather['feelsLike']}°C
更新时间：{data['updateTime']}
"""
    else:
        return "查询失败，请稍后重试。"

def search_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("提示", "请输入城市名称")
        return
    result = get_weather(city)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)

# GUI 构建
root = tk.Tk()
root.title("天气查询小工具")
root.geometry("400x300")

tk.Label(root, text="请输入城市名称（中文）:").pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack()

tk.Button(root, text="查询天气", command=search_weather).pack(pady=10)

result_text = tk.Text(root, height=10, font=("Arial", 12))
result_text.pack()

root.mainloop()
