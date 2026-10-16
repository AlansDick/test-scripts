import os
import shutil

RULES = {
    ".jpg": "图片",
    ".jpeg": "图片",
    ".png": "图片",
    ".gif": "图片",
    ".pdf": "文档",
    ".docx": "文档",
    ".doc": "文档",
    ".txt": "文档",
    ".mp4": "视频",
    ".mp3": "音频",
    ".zip": "压缩包",
    ".rar": "压缩包",
}

def organize(folder_path):
    if not os.path.exists(folder_path):
        print(f"错误：找不到文件夹 {folder_path}")
        return

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if os.path.isdir(full_path):
            continue

        ext = os.path.splitext(filename)[1].lower()
        target_folder_name = RULES.get(ext)

        if target_folder_name is None:
            print(f"跳过：{filename}（未知类型）")
            continue

        target_folder = os.path.join(folder_path, target_folder_name)

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        shutil.move(full_path, os.path.join(target_folder, filename))
        print(f"移动：{filename} -> {target_folder_name}/")

if __name__ == "__main__":
    target = input("请输入要整理的文件夹路径：")
    organize(target)
