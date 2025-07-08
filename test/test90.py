import requests
from wordcloud import WordCloud
import jieba

# 假设你已经拿到了弹幕文本
text = "今天天气真好 真好 真不错 牛啊 这操作太帅了"

# 分词
wordlist = jieba.cut(text)
wordstr = " ".join(wordlist)

# 生成词云
wc = WordCloud(font_path='simhei.ttf', width=800, height=600, background_color='white').generate(wordstr)
wc.to_file('barrage_wordcloud.png')
