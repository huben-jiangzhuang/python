# 导入包
from moviepy.editor import *
# 加载待裁剪视频，裁剪1分10秒——1分50秒
clip = VideoFileClip("blankpink.mp4").subclip((1,10),(1,50))
# 生成一个字幕，设置字体、颜色
txt_clip = TextClip("black pink beautiful",fontsize=70,color='white')
# 在屏幕中间出现10s
txt_clip = txt_clip.set_position('center').set_duration(10)
# 将字幕和裁剪的视频组合在一起
video = CompositeVideoClip([clip,txt_clip])
# 组合视频输出
video.write_videofile("clip_txt.mp4")
# clip.write_videofile("clip.mp4")