import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import time

# 禁用 matplotlib 中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def fetch_douban_top250():
    """爬取豆瓣电影 Top250"""
    all_movies = []
    for start in range(0, 250, 25):
        url = f'https://movie.douban.com/top250?start={start}'
        headers = {
            'User-Agent': 'Mozilla/5.0'
        }
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        items = soup.select('div.item')
        for item in items:
            title = item.select_one('span.title').text
            rating = item.select_one('span.rating_num').text
            quote = item.select_one('span.inq')
            quote_text = quote.text if quote else "无"
            all_movies.append({
                '电影名称': title,
                '评分': float(rating),
                '短评': quote_text
            })
        print(f"已抓取 {start + 25} 条电影信息")
        time.sleep(1)  # 避免访问过快被封

    return all_movies

def save_to_csv(data, filename='douban_top250.csv'):
    """保存数据到 CSV 文件"""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"保存至文件：{filename}")

def plot_rating_distribution(data):
    """绘制评分分布图"""
    df = pd.DataFrame(data)
    plt.figure(figsize=(10,6))
    plt.hist(df['评分'], bins=10, edgecolor='black', color='skyblue')
    plt.title('豆瓣Top250电影评分分布')
    plt.xlabel('评分')
    plt.ylabel('电影数量')
    plt.grid(True)
    plt.savefig('rating_distribution.png')
    print("评分分布图已保存为 rating_distribution.png")
    plt.show()

if __name__ == '__main__':
    print("开始爬取豆瓣Top250电影数据...")
    movies = fetch_douban_top250()
    save_to_csv(movies)
    plot_rating_distribution(movies)
