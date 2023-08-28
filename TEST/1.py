import os
import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip, concatenate_videoclips

class VideoMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("影片合併程式")

        self.file_list = []
        self.clips = []

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.select_button = tk.Button(self.frame, text="選擇影片", command=self.select_files)
        self.select_button.pack()

        self.merge_button = tk.Button(self.frame, text="合併影片", command=self.merge_videos)
        self.merge_button.pack()

    def select_files(self):
        files = filedialog.askopenfilenames(title="選擇影片", filetypes=[("影片文件", "*.mp4 *.avi *.mkv")])
        self.file_list = list(files)
        print("選擇的影片文件:", self.file_list)

    def merge_videos(self):
        if len(self.file_list) == 0:
            print("請先選擇影片文件")
            return

        for file_path in self.file_list:
            clip = VideoFileClip(file_path)
            self.clips.append(clip)

        final_clip = concatenate_videoclips(self.clips, method="compose")
        
        output_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 文件", "*.mp4")])
        if output_path:
            final_clip.write_videofile(output_path, codec="libx264")
            print("影片合併完成，輸出至:", output_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoMergerApp(root)
    root.mainloop()
