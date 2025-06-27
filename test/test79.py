import tkinter as tk
from PIL import Image, ImageDraw
import numpy as np
from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier

# 加载数据训练 KNN 模型
digits = load_digits()
X = digits.data
y = digits.target
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# GUI 界面
class DigitRecognizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("手写数字识别")
        self.canvas = tk.Canvas(root, width=200, height=200, bg='white')
        self.canvas.pack()
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()
        tk.Button(self.button_frame, text='识别', command=self.recognize).pack(side='left')
        tk.Button(self.button_frame, text='清除', command=self.clear).pack(side='left')

        self.image = Image.new('L', (200, 200), color=255)
        self.draw = ImageDraw.Draw(self.image)
        self.canvas.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        x, y = event.x, event.y
        r = 8
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill='black')
        self.draw.ellipse([x-r, y-r, x+r, y+r], fill=0)

    def clear(self):
        self.canvas.delete("all")
        self.image = Image.new('L', (200, 200), color=255)
        self.draw = ImageDraw.Draw(self.image)

    def recognize(self):
        img = self.image.resize((8, 8)).resize((64, 64))  # 先压缩再放大，平滑化
        data = np.array(img)
        data = 16 - (data / 16).astype(int)  # MNIST数据是 0-16
        flat = data.flatten().reshape(1, -1)
        prediction = knn.predict(flat)[0]
        tk.messagebox.showinfo("识别结果", f"我猜这个数字是：{prediction}")

if __name__ == "__main__":
    import tkinter.messagebox
    root = tk.Tk()
    app = DigitRecognizerApp(root)
    root.mainloop()
