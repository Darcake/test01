import os
from cv2 import cv2
import numpy as np
from tqdm import tqdm


def rm_img_and_rn(dst_dir, src_dir, name, num):
    #要处理的cam_info路径
    src_cam_file = os.path.join(src_dir, name, "cam_info.txt")
    #要处理的images路径
    src_dir = os.path.join(src_dir, name, "images", f"image_{num}")
    #路径中所有图像名字组成列表
    img_lists = os.listdir(src_dir)
    #路径中图像总数
    img_num=len(img_lists)
    j = 0
    #打开要处理的cam_info文件
    f1 = open(src_cam_file, "r", encoding="utf-8")
    #创建并打开处理后的cam_info文件
    f2 = open(os.path.join(dst_dir, name, "cam_info_1.txt"), "w", encoding="utf-8")
    #处理后图像保存路径
    dst_img_dir = os.path.join(dst_dir, name, "images_1", f"image_{num}")
    if not os.path.exists(dst_img_dir):
        os.makedirs(dst_img_dir)
    print(f"正在处理{src_dir}中的图片及对应的cam_info")
    for i in tqdm(range(img_num)):
        src_img_dir = os.path.join(src_dir, img_lists[i])
        #读入一张图像并读入对应的cam_info
        img = cv2.imread(src_img_dir)
        buf = f1.readline()
        #删除图片的范围
        if (i >= 1630 and i <= 1662):
            j += 1
        else:
            cv2.imwrite(os.path.join(dst_img_dir, f"{i-j:06d}.png"), img)
            f2.write(buf)
    f1.close()
    f2.close()


def crop_img(dst_dir, src_dir, name, crop_v, crop_u, crop_h, crop_w):
    #要裁剪的images路径
    src_dir = os.path.join(src_dir, name, "images_1", "image_0")
    #裁剪后的images路径
    dst_dir = os.path.join(dst_dir, name, "images_2", "image_0")
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    img_lists = os.listdir(src_dir)
    img_num=len(img_lists)
    for i in tqdm(range(img_num)):
        img = cv2.imread(os.path.join(src_dir, img_lists[i]))
        cropped_img = img[crop_v:crop_v + crop_h, crop_u:crop_u + crop_w]
        cv2.imwrite(os.path.join(dst_dir,f"{i:06d}.png"),cropped_img)    


def img_to_video(src_dir,dst_dir,name):
    # 图片文件夹路径
    path = os.path.join(src_dir,name,"images_2","image_0")
    file_list = os.listdir(path)
    num = len(file_list)
    fps = 45
    # 需要转为视频的图片的尺寸，图片的尺寸要一致
    size = (640, 192)
    # 视频保存在当前目录下
    video = cv2.VideoWriter(os.path.join(dst_dir,name,"video.avi"), cv2.VideoWriter_fourcc(
    'I', '4', '2', '0'), fps, size)
    for i in tqdm(range(num)):
        img_path=os.path.join(path,file_list[i])
        img = cv2.imread(img_path)
        video.write(img)
    video.release()


dst_dir="D:/datates"
src_dir = "D:/datates"
#jixieguan (i>=460 and i<=512) or (i>=641 and i<=685) or (i>=897 and i<930) or (i>=1302 and i<=1338) or (i>=3029 and i<=3086)
#jixieguan2 (i>=688 and i<=704) or (i>=886 and i<=931) or (i>=1160 and i<1178) or (i>=1633 and i<=1681) or (i>=3509 and i<=3541)
#jixieguan3 (i>=647 and i<=701) or (i>=883 and i<=921) or (i>=1173 and i<1219) or (i>=1653 and i<=1706) or (i>=3430 and i<=3476)
#pengyuan2 (i>=320 and i<=365) or (i>=863 and i<=897)
#yangwangxingkong (i>=469 and i<=500) or (i>=1405 and i<=1450) or (i>=2013 and i<2059) or (i>=2310 and i<=2337) or (i>=2949 and i<=2993) or (i>=3538 and i<=3558) or (i>=3850 and i<=3896) or (i>=4425 and i<=4476)
#yangwangxingkong2 (i>=1630 and i<=1662)

#rm_img_and_rn(dst_dir, src_dir, "jixieguan", 0)
#rm_img_and_rn(dst_dir, src_dir, "jixieguan2", 0)
#rm_img_and_rn(dst_dir, src_dir, "jixieguan3", 0)
#rm_img_and_rn(dst_dir, src_dir, "pengyuan2", 0)
#rm_img_and_rn(dst_dir, src_dir, "yangwangxingkong", 0)
#rm_img_and_rn(dst_dir, src_dir, "yangwangxingkong2", 0)#最后一张图片显示损坏

#crop_img(dst_dir, src_dir, "jixieguan", 0, 152, 192, 640)

#crop_img(dst_dir, src_dir, "jixieguan2", 0, 154, 192, 640)

#crop_img(dst_dir, src_dir, "jixieguan3", 0, 152, 192, 640)

#crop_img(dst_dir, src_dir, "pengyuan", 0, 151, 192, 640)

#crop_img(dst_dir, src_dir, "pengyuan2", 0, 147, 192, 640)

#crop_img(dst_dir, src_dir, "yangwangxingkong", 0, 153, 192, 640)

#crop_img(dst_dir, src_dir, "yangwangxingkong2", 0, 158, 192, 640)

#crop_img(dst_dir, src_dir, "yangwangxingkong3", 0, 157, 192, 640)


img_to_video(src_dir, dst_dir,"jixieguan")
img_to_video(src_dir, dst_dir, "jixieguan2")
img_to_video(src_dir, dst_dir, "jixieguan3")
img_to_video(src_dir, dst_dir, "pengyuan")
img_to_video(src_dir, dst_dir, "pengyuan2")
img_to_video(src_dir, dst_dir, "yangwangxingkong")
img_to_video(src_dir, dst_dir, "yangwangxingkong2")
img_to_video(src_dir, dst_dir, "yangwangxingkong3")
