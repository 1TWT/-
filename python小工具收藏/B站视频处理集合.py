import os
import sys
import time
# 将m4s转换为MP4，aac
from os import system

file = 0  # 文件；路径  C:\Users\田涛\Desktop\01.md

for arg in sys.argv:  # 拖入执行
    # 输出路径
    file = arg

# gifFileName = file  # 获取拽入文件路径   C:\Users\田涛\Desktop\01.md

fn = file.split("\\")

FName = fn[len(fn) - 1]  # 获取文件名称带后缀 01.md
FName2 = FName.split(".")[0]  # 不带后缀 01
FName3 = file.split(".")[0]  # C:\Users\田涛\Desktop\01
file2 = file.strip(FName) + "s" + FName  # C:\Users\田涛\Desktop\s01.md


def m4sToMp4(filel, newFile):
    # 将文件转换
    # filel ：旧文件路径
    # newFile ：新文件路径
    ok = system("ffmpeg -i " + filel + " -strict -2 " + newFile)
    # 函数执行后如果没有错误则返回0 否则返回1
    print(ok)
    print(newFile)


def getV(fileMp4l, fileAacl):
    # 将文件合成： 视频和音频

    os.system(fr'ffmpeg -i "{fileMp4l}" -i "{fileAacl}" -vcodec copy -acodec copy "{FName3}"s.mp4')
    time.sleep(4)


if __name__ == '__main__':

    fileMp4 = FName3 + ".mp4"  # 视频新文件
    fileAac = file2.split(".")[0] + ".aac"  # 音频新文件
    if FName2.isnumeric():  # 只包含数字的视频
        m4sToMp4(file, fileMp4)
        m4sToMp4(file2, fileAac)
    else:
        m4sToMp4(file2, fileAac)
    getV(fileMp4, fileAac)
    # 移除旧文件与新文件只剩合成文件
    os.remove(file2)
    os.remove(file)
    os.remove(fileAac)
    os.remove(fileMp4)
