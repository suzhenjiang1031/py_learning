# 写入文件
with open("example.txt", "w") as f:
    f.write("Hello, Python!\n这是一行测试文本。")

# 读取文件
with open("example.txt", "r") as f:
    content = f.read()
    print("文件内容如下：")
    print(content)
