import os

def rename_images(folder_path, prefix="img"):
    files = os.listdir(folder_path)
    for index, filename in enumerate(files):
        ext = os.path.splitext(filename)[1]
        new_name = f"{prefix}_{index+1}{ext}"
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
    print("文件已重命名完毕")

# 示例：rename_images("D:/Pictures", "holiday")
