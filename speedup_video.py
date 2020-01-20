# from moviepy import *
from moviepy.editor import vfx
from moviepy.video.io.VideoFileClip import VideoFileClip
# from moviepy.audio.fx.audio_fadein import audio_fadein
print("🚀 🚀 🚀 🚀 Welcome to Cooper's speed up video laboratory! 🚀 🚀 🚀 🚀")
drag_n_drop_file = str(input("Drag-n-drop a video file that you want to speed up:")).replace("\\", "").strip()
source_video = VideoFileClip(drag_n_drop_file)
speed_up_video = source_video.fx(vfx.speedx, 2)
file_path_split = drag_n_drop_file.split('/')
filename_with_ending = file_path_split.pop(-1)
file_dir = '/'.join(file_path_split)
old_filename = filename_with_ending.split('.')[0]
new_filename = str("/" + "speed_up_video_" + old_filename + ".mp4")
speed_up_video.write_videofile(file_dir + new_filename)
