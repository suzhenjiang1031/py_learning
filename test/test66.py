import requests

# 替换成你自己的 API Key
API_KEY = '你的API密钥'  
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric',  # 摄氏度
        'lang': 'zh_cn'     # 中文
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"\n🌍 城市：{data['name']}")
            print(f"📍 天气：{data['weather'][0]['description']}")
            print(f"🌡️ 温度：{data['main']['temp']}°C")
            print(f"🤒 体感温度：{data['main']['feels_like']}°C")
            print(f"💨 风速：{data['wind']['speed']} m/s")
            print(f"💧 湿度：{data['main']['humidity']}%")
        else:
            print(f"\n❌ 查询失败：{data.get('message', '未知错误')}")

    except requests.RequestException as e:
        print("网络错误，请检查网络连接。")
        print(e)

def main():
    print("== 实时天气查询工具 ==")
    while True:
        city = input("\n请输入城市名称（或输入 q 退出）：")
        if city.lower() == 'q':
            print("退出天气查询工具，再见！")
            break
        get_weather(city)

if __name__ == "__main__":
    main()
