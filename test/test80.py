from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def create_meme(image_path, text, output_path="output_meme.jpg"):
    # 打开图片
    image = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(image)

    # 设置字体（Windows系统）可替换为其他字体
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except:
        font = ImageFont.load_default()

    # 自动换行
    wrapped_text = textwrap.fill(text, width=15)

    # 文本位置：底部 or 顶部
    W, H = image.size
    text_size = draw.textsize(wrapped_text, font=font)
    x = (W - text_size[0]) // 2
    y = H - text_size[1] - 20  # 底部偏上

    # 添加黑色文字背景边框（更清晰）
    draw.text((x-1, y-1), wrapped_text, font=font, fill="black")
    draw.text((x+1, y-1), wrapped_text, font=font, fill="black")
    draw.text((x-1, y+1), wrapped_text, font=font, fill="black")
    draw.text((x+1, y+1), wrapped_text, font=font, fill="black")

    # 文字
    draw.text((x, y), wrapped_text, font=font, fill="white")

    # 保存图片
    image.save(output_path)
    print(f"表情包已保存为：{output_path}")

# 示例用法
if __name__ == "__main__":
    img_path = "cat.jpg"  # 替换为你自己的图像路径
    meme_text = "不想上班了😤"
    create_meme(img_path, meme_text)
