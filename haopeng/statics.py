from PIL import Image
import os
import numpy as np

def get_image_resolution(image_path):
    with Image.open(image_path) as img:
        return img.size  # 返回 (width, height)

def calculate_resolution_statistics(images_dir):
    resolutions = []

    # 遍历文件夹中的所有图片
    for img_file in os.listdir(images_dir):
        if img_file.endswith((".jpg", ".jpeg", ".png")):  # 过滤图片格式
            img_path = os.path.join(images_dir, img_file)
            width, height = get_image_resolution(img_path)
            resolutions.append((width, height))

    # 将分辨率数据分解为宽度和高度的列表
    widths = np.array([res[0] for res in resolutions])
    heights = np.array([res[1] for res in resolutions])

    # 计算宽度和高度的四分位数和中位数
    width_q1, width_median, width_q3 = np.percentile(widths, [25, 50, 75])
    height_q1, height_median, height_q3 = np.percentile(heights, [25, 50, 75])

    # 生成三种代表性尺寸
    size_q1 = (int(width_q1), int(height_q1))
    size_median = (int(width_median), int(height_median))
    size_q3 = (int(width_q3), int(height_q3))

    return size_q1, size_median, size_q3

# 设置图片文件夹路径
images_dir = "datasets/All/train/images"  # 替换为你的训练集图片路径
size_q1, size_median, size_q3 = calculate_resolution_statistics(images_dir)

# 输出代表性尺寸
print(f"1st Quartile Size (Q1): {size_q1}")
print(f"Median Size: {size_median}")
print(f"3rd Quartile Size (Q3): {size_q3}")
