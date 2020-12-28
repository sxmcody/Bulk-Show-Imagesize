# -*- coding: UTF-8 -*-
# 批量显示指定位置图片的尺寸以及物理尺寸

import os
#导入Pillow的Image类
from PIL import Image

#指定图片位置，形如：C:\Users\xxx\Pictures
imgdir=input("请输入图片文件夹地址:")
allfiles=os.listdir(imgdir)
#用filter()函数过滤仅保留图片格式文件，留下的进入列表
def file_filter(f):
    if f[-4:] in ['.jpg','.png','.bmp']:
        return True
    else:
        return False
images = list(filter(file_filter,allfiles))

#用for循环，依次打开所有图片文件夹路径的图片
for img in images:
    #输入的路径+图片文件名得到实际图片路径
    imgopen=Image.open(imgdir+"\\"+img)
    #用max()和min()函数分别获得图片长边和短边大小
    lpx=max(imgopen.size)
    spx=min(imgopen.size)
    #用pillow内置的info获取图片dpi信息，因部分图片不含有dpi，所以先判断是否含有dpi
    #dict内置的get()方法，如果key存在，则返回其value,否则返回None
    if imgopen.info.get('dpi')!=None:
        #获取dpi
        dpi=max(imgopen.info.get('dpi'))
        #厘米和像素转换公式为 px/dpi*2.54，用round函数保留两位小数
        lcm=round(lpx/dpi*2.54,2)
        scm=round(spx/dpi*2.54,2)
        print(img,str(lpx)+"X"+str(spx)+"px",str(dpi)+"dpi"+" 物理尺寸："+str(lcm)+"X"+str(scm)+"cm")
    else:
        print(img,str(lpx)+"X"+str(spx)+"px")
    
    
