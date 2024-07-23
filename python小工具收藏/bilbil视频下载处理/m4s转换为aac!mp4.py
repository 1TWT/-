from ffmpy import FFmpeg

# 将m4s转换为MP4，aac
from os import system
# 在system里放入需要执行的命令即可 这里我写的是ipconfig命令
o=r"D:\基础\pythonDemo\测试\bilbil\download\ly"
ok = system("ffmpeg -i "+o+".m4s -strict -2 "+o+".aac")
# 函数执行后如果没有错误则返回0 否则返回1
print(ok)