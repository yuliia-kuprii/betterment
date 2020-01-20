from tkinter import *
from tkinter import filedialog
from moviepy.editor import vfx
from moviepy.video.io.VideoFileClip import VideoFileClip
from tkinter import ttk
from tkinter.ttk import *

# import os
# import math

'''pyinstaller --onefile --windowed --noconfirm --icon "tortuga_icon.icns" --add-data "tortuga_bg.gif:." gui_speedapp.py'''

# MAX_FILE_SIZE_IN_BYTES = 9000000

plain_window = Tk()
plain_window.geometry("450x300+350+250")
plain_window.resizable(0, 0)
plain_window.title("Tortuga Rápida")

style = Style()
style.theme_use('alt')
foreground_color="#24211d"
background_color_text="Test.TLabel"
style.configure(
    'Test.TLabel',
    foreground=foreground_color,
    background="#ffffff"
)
style.configure(
    'Lol.TButton',
    foreground=foreground_color,
    width=20,
    font=('Courier', '16', 'bold')
)

photo1 = PhotoImage(file="./tortuga_bg.gif")
label1 = Label(plain_window, image=photo1)
label1.pack()

welcome_header = ttk.Label(
    plain_window,
    text="Speed up your video",
    font="Courier 20 bold",
    style=background_color_text
)
welcome_header.place(
    relx=0.5,
    rely=0.05,
    anchor=CENTER)

step1 = ttk.Label(
    plain_window,
    text="Step 1:",
    font="Courier 16 bold",
    style=background_color_text
)
step1.place(
    relx=0.5,
    rely=0.15,
    anchor=CENTER)

speed_title = ttk.Label(
    plain_window,
    text="Select speed:",
    font="Courier 13 bold",
    style=background_color_text
    )
speed_title.place(
    relx=0.5,
    rely=0.22,
    anchor=CENTER)


speed_select = IntVar()

drop_down = OptionMenu(plain_window, speed_select, -1, 1, 2, 3, 4)
drop_down.config(
    width=3,

)
speed_select.set(2)

drop_down.place(
    relx=0.5,
    rely=0.3,
    anchor=CENTER
)

message = ttk.Label(
    plain_window,
    text="Process completed successfully!",
    foreground="#4e6376",
    font="Courier 17 bold",
    style=background_color_text
)
progress_bar = ttk.Progressbar(
    plain_window,
    orient="horizontal",
    length=150,
)
progress_bar.config(mode="determinate", maximum=100)

step2 = ttk.Label(
    plain_window,
    text="Step 2:",
    font="Courier 16 bold",
    style=background_color_text
)
step2.place(
    relx=0.5,
    rely=0.7,
    anchor=CENTER
)


def handle_open_file_btn_click():
    # Clean progress bar, message
    message.place_forget()
    progress_bar.place(
        relx=0.5,
        rely=0.52,
        anchor=CENTER
    )
    progress_bar.stop()

    # choose file
    file_types = ("*.MOV", "*.MP4", ".WEBM", ".MPG", ".MP2", ".MPEG", ".MPE", ".MPV", ".OGG", ".M4P", ".M4V", ".AVI", ".WMV", ".QT", ".FLV", ".F4V", ".SWF", ".AVCHD", ".SVI", ".GIF", ".3GP")
    plain_window.filename = filedialog.askopenfilename(filetypes=[("video files", file_types)])
    if not plain_window.filename:
        return progress_bar.place_forget()

    # process file
    file_path = plain_window.filename
    source_video = VideoFileClip(file_path)
    speed_up_video = source_video.fx(vfx.speedx, speed_select.get())

    file_path_split = file_path.split('/')
    filename_with_ending = file_path_split.pop(-1)
    file_dir = '/'.join(file_path_split)
    old_filename = filename_with_ending.split('.')[0]
    new_filename = str("/" + "speed_up_video_" + old_filename + ".mp4")

    # show progress bar, message
    progress_bar.step(99.99)
    new_video_file_path = file_dir + new_filename
    speed_up_video.write_videofile(new_video_file_path)
    message.place(
        relx=0.5,
        rely=0.60,
        anchor=CENTER
    )



    # file_resolution = source_video.size
    # print('!!!!!! before ', file_resolution)
    #
    #
    # new_file_size = os.path.getsize(new_video_file_path)
    # print('new_file_size BEFORE: ', new_file_size)
    # times = new_file_size / MAX_FILE_SIZE_IN_BYTES
    # if times <= 1:
    #     return None
    #
    # print('!!!!!! times ', times)
    # diff = 1 / times
    # side_diff = math.sqrt(diff)
    # print('!!!!!! side_diff ', side_diff)
    #
    # target_resolution = []
    # for side_resolution in file_resolution:
    #     target_resolution.insert(0, (int(side_resolution * side_diff)))
    # print('!!!!!! target_resolution ', target_resolution)
    #
    # source_video = VideoFileClip(new_video_file_path, target_resolution=target_resolution)
    # print('!!!!!! after ', source_video.size)
    # source_video.write_videofile(new_video_file_path)


open_file_btn = ttk.Button(
    plain_window,
    text="Choose video file",
    style="Lol.TButton",
    width=20,
    command=handle_open_file_btn_click
)
open_file_btn.place(
    relx=0.5,
    rely=0.8,
    anchor=CENTER
)

sign = ttk.Label(
    plain_window,
    text="Created by Yuliia Kuprii",
    foreground="snow4",
    font="Courier 12 italic",
    style=background_color_text
)
sign.place(
    relx=0.60,
    rely=0.94,
    anchor=NW
)

plain_window.mainloop()
