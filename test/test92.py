import tkinter as tk
from tkinter import messagebox

# 创建主窗口
window = tk.Tk()
window.title("简单 GUI 示例")
window.geometry("300x100")

# 定义按钮点击事件
def show_message():
    messagebox.showinfo("消息", "你点击了按钮！")

# 创建按钮
button = tk.Button(window, text="点击我", command=show_message)
button.pack(pady=20)

# 运行主循环
window.mainloop()