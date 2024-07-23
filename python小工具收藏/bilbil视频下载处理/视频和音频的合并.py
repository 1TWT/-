import os

print("合并视音频")
mp3_f=r"D:\基础\pythonDemo\测试\bilbil\download\ly.aac"
mp4_f=r"D:\基础\pythonDemo\测试\bilbil\download\sp.mp4"
n_mp4_f = r"D:\基础\pythonDemo\测试\bilbil\download\mew.mp4"

os.system(fr'ffmpeg -i "{mp4_f}" -i "{mp3_f}" -vcodec copy -acodec copy "{n_mp4_f}"')
