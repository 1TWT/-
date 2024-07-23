from PIL import Image
import os
import sys

file = 0
for arg in sys.argv:
    # 输出路径
    file = arg

gifFileName = file
if file[-3:] == "gif":

    # 使用Image模块的open()方法打开gif动态图像时，默认是第一帧
    im = Image.open(gifFileName)
    pngDir = gifFileName[:-4]
    # 创建存放每帧图片的文件夹(文件夹名与图片名称相同)
    os.mkdir(pngDir)
    a = 1
    t = 17
    try:
        while True:
            # 保存当前帧图片
            current = im.tell()
            if current % a == 0 or current == t:
                im.save(pngDir + '/'+file[-7:-4] + str(current) + '.png')
            # 获取下一帧图
            im.seek(current + 1)


    except EOFError:
        pass
