import cv2
import time
import numpy as np
from ultralytics import YOLO  # 确保 YOLOv8 安装并导入

# 加载训练好的 YOLOv8 模型
# 替换为你自己的模型路径
model=YOLO('runs/detect/256.pt')
# model = YOLO('runs/detect/512/weights/best.pt')
# 打开视频文件或摄像头，0 表示使用默认摄像头
cap = cv2.VideoCapture('test.mp4')  # 或者使用 cap = cv2.VideoCapture(0) 使用摄像头

# 检查视频是否成功打开
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# 初始化变量
fps_list = []  # 用于存储每一帧的 FPS
total_frames = 0  # 累计帧数

# 实时检测
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Finished processing video.")
        break

    # 记录处理一帧的开始时间
    frame_start_time = time.time()
    
    # 使用 YOLOv8 模型进行检测
    results = model(frame)
    
    # 对检测到的物体区域进行高斯模糊
    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()  # 获取检测框的坐标
        for box in boxes:
            x1, y1, x2, y2 = map(int, box)
            # 提取检测框区域
            roi = frame[y1:y2, x1:x2]

            # 使用高斯模糊该区域
            blurred_roi = cv2.GaussianBlur(roi, (31, 31), 0)  # (21, 21) 是模糊核大小，可以根据需求调整

            # 将模糊区域放回到原图
            frame[y1:y2, x1:x2] = blurred_roi

    # 计算单帧 FPS
    frame_end_time = time.time()
    fps = 1 / (frame_end_time - frame_start_time)
    fps_list.append(fps)
    total_frames += 1
    
    # 计算到目前为止的平均 FPS
    avg_fps = sum(fps_list) / total_frames  # 计算到目前为止的平均 FPS

    # 在图像上显示实时 FPS 和到目前为止的平均 FPS
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Avg FPS: {avg_fps:.2f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    
    # 显示检测结果
    cv2.imshow("YOLOv8 Detection with Gaussian Blurring", frame)
    
    # 按 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放视频流和关闭窗口
cap.release()
cv2.destroyAllWindows()
