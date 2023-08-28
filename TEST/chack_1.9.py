import os
import shutil
import tkinter as tk
from tkinter import filedialog

def move_files(source_folder, dest_folder, size_limit):
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path) and os.path.getsize(file_path) > size_limit:
            shutil.move(file_path, os.path.join(dest_folder, filename))

def select_source_folder():
    folder_path = filedialog.askdirectory()
    source_folder.set(folder_path)

def select_dest_folder():
    folder_path = filedialog.askdirectory()
    dest_folder.set(folder_path)

def process_files():
    source_path = source_folder.get()
    dest_path = dest_folder.get()
    size_limit = 1.9 * 1024 * 1024 * 1024  # 1.9GB換算成位元組

    move_files(source_path, dest_path, size_limit)
    result_label.config(text="檔案處理完成並移動！")

# 建立GUI視窗
root = tk.Tk()
root.title("檔案整理程式")

# 建立變數以存儲資料夾路徑
source_folder = tk.StringVar()
dest_folder = tk.StringVar()

# 建立GUI元件
source_label = tk.Label(root, text="來源資料夾:")
source_label.pack()

source_entry = tk.Entry(root, textvariable=source_folder)
source_entry.pack()

source_button = tk.Button(root, text="選擇來源資料夾", command=select_source_folder)
source_button.pack()

dest_label = tk.Label(root, text="目標資料夾:")
dest_label.pack()

dest_entry = tk.Entry(root, textvariable=dest_folder)
dest_entry.pack()

dest_button = tk.Button(root, text="選擇目標資料夾", command=select_dest_folder)
dest_button.pack()

process_button = tk.Button(root, text="處理檔案", command=process_files)
process_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# 啟動GUI事件迴圈
root.mainloop()
