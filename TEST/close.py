import cv2
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class ImageToVideoConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("图片合成视频工具")

        self.frame_rate_label = ttk.Label(root, text="帧率 (Frames per Second):")
        self.frame_rate_label.grid(row=0, column=0)
        self.frame_rate_entry = ttk.Entry(root)
        self.frame_rate_entry.grid(row=0, column=1)

        self.input_folder_label = ttk.Label(root, text="输入文件夹:")
        self.input_folder_label.grid(row=1, column=0)
        self.input_folder_entry = ttk.Entry(root)
        self.input_folder_entry.grid(row=1, column=1)
        self.input_folder_button = ttk.Button(root, text="浏览", command=self.browse_input_folder)
        self.input_folder_button.grid(row=1, column=2)

        self.output_folder_label = ttk.Label(root, text="输出文件夹:")
        self.output_folder_label.grid(row=2, column=0)
        self.output_folder_entry = ttk.Entry(root)
        self.output_folder_entry.grid(row=2, column=1)
        self.output_folder_button = ttk.Button(root, text="浏览", command=self.browse_output_folder)
        self.output_folder_button.grid(row=2, column=2)

        self.output_video_label = ttk.Label(root, text="输出视频文件名 (Output Video Filename):")
        self.output_video_label.grid(row=3, column=0)
        self.output_video_entry = ttk.Entry(root)
        self.output_video_entry.grid(row=3, column=1)

        self.convert_button = ttk.Button(root, text="合成视频 (Convert to Video)", command=self.convert_to_video)
        self.convert_button.grid(row=4, column=1)

    def browse_input_folder(self):
        input_folder = filedialog.askdirectory()
        self.input_folder_entry.delete(0, tk.END)
        self.input_folder_entry.insert(0, input_folder)

    def browse_output_folder(self):
        output_folder = filedialog.askdirectory()
        self.output_folder_entry.delete(0, tk.END)
        self.output_folder_entry.insert(0, output_folder)

    def convert_to_video(self):
        frame_rate = int(self.frame_rate_entry.get())
        input_folder = self.input_folder_entry.get()
        output_folder = self.output_folder_entry.get()
        output_video = self.output_video_entry.get()

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        image_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith(".jpg") or f.endswith(".png")]
        if not image_files:
            print("指定文件夹中未找到图片文件 (.jpg 或 .png).")
            return

        first_image = cv2.imread(image_files[0])
        height, width, layers = first_image.shape

        output_video_path = os.path.join(output_folder, output_video)

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用MP4编解码器
        video_writer = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (width, height))

        for image_file in image_files:
            frame = cv2.imread(image_file)
            video_writer.write(frame)

        video_writer.release()
        print(f"视频已生成为 {output_video_path}")


if __name__ == '__main__':
    root = tk.Tk()
    app = ImageToVideoConverterApp(root)
    root.mainloop()
