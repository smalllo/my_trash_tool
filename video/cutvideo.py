import tkinter as tk
from tkinter import filedialog
from moviepy.video.io.VideoFileClip import VideoFileClip
import os

class VideoCutterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Cutter App")

        self.source_file = ""
        self.output_folder = ""

        self.label_source = tk.Label(root, text="選擇影片来源:")
        self.label_source.pack()

        self.label_source_path = tk.Label(root, text="")
        self.label_source_path.pack()

        self.button_select_source = tk.Button(root, text="選擇影片", command=self.select_source)
        self.button_select_source.pack()

        self.label_output = tk.Label(root, text="選擇输出資料夾:")
        self.label_output.pack()

        self.label_output_path = tk.Label(root, text="")
        self.label_output_path.pack()
        
        self.button_select_output = tk.Button(root, text="選擇資料夾", command=self.select_output)
        self.button_select_output.pack()

        self.label_duration = tk.Label(root, text="輸入分割時長（秒）:")
        self.label_duration.pack()

        self.duration_entry = tk.Entry(root)
        self.duration_entry.pack()

        self.button_cut = tk.Button(root, text="剪辑影片", command=self.cut_video)
        self.button_cut.pack()

    def select_source(self):
        self.source_file = filedialog.askopenfilename(filetypes=[("影片文件", "*.mp4 *.avi")])
    def select_output(self):
        self.output_folder = filedialog.askdirectory()
    def select_source(self):
        self.source_file = filedialog.askopenfilename(filetypes=[("影片文件", "*.mp4 *.avi")])
        if self.source_file:
            self.label_source_path.config(text="以選擇影片: " + self.source_file)
        else:
            self.label_source_path.config(text="")

    def select_output(self):
        self.output_folder = filedialog.askdirectory()
        if self.output_folder:
            self.label_output_path.config(text="以選擇資料夾: " + self.output_folder)
        else:
            self.label_output_path.config(text="")

    def cut_video(self):
        if not self.source_file or not self.output_folder:
            tk.messagebox.showerror("錯誤", "選擇影片或者資料夾")
            return

        duration = int(self.duration_entry.get())

        video_clip = VideoFileClip(self.source_file)  

        total_duration = int(video_clip.duration)
        
        output_base = os.path.splitext(os.path.basename(self.source_file))[0]

        start_time = 0
        clip_index = 1
        while start_time < total_duration:
            end_time = min(start_time + duration, total_duration)

            output_file = os.path.join(self.output_folder, f"{output_base}_part{clip_index}.mp4")

            trimmed_clip = video_clip.subclip(start_time, end_time)
            trimmed_clip.write_videofile(output_file, codec="libx264")

            start_time += duration
            clip_index += 1

        tk.messagebox.showinfo("完成", "影片剪辑完成！")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x200")
    app = VideoCutterApp(root)
    root.mainloop()
