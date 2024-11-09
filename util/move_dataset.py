import os
import shutil

def flatten_images_to_destination(source_folder, destination_folder):
    """
    將來源資料夾中的所有資料夾內的圖片移動到同一個目標資料夾中。

    :param source_folder: 包含子資料夾和圖片的來源資料夾路徑
    :param destination_folder: 目標資料夾的路徑
    """
    # 確保目標資料夾存在，如果不存在則建立
    os.makedirs(destination_folder, exist_ok=True)

    # 遍歷來源資料夾內的所有子資料夾
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # 確保檔案是圖片檔案
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                # 取得檔案的完整路徑
                file_path = os.path.join(root, file)
                # 移動檔案到目標資料夾
                shutil.move(file_path, os.path.join(destination_folder, file))

    print(f"所有圖片已成功移動到目標 {destination_folder} 資料夾！")

def move_images_between_folders(source_folder, destination_folder):
    """
    將來源資料夾中的所有圖片移動到目標資料夾中。

    :param source_folder: 包含圖片的來源的資料夾路徑
    :param destination_folder: 目標資料夾的路徑
    """
    # 確保目標資料夾存在，如果不存在則建立
    os.makedirs(destination_folder, exist_ok=True)

    # 遍歷來源資料夾內的所有檔案
    for file in os.listdir(source_folder):
        # 確保檔案是圖片檔案
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            # 取得檔案的完整路徑
            file_path = os.path.join(source_folder, file)
            # 移動檔案到目標資料夾
            shutil.move(file_path, os.path.join(destination_folder, file))

    print(f"所有圖片已成功從來源 {source_folder} 資料夾移動到目標 {destination_folder} 資料夾！")


def check_folder_img_size(source_folder_path):
    """
    查看資料夾內的圖片數量
    :param source_folder_path: 圖片的來源的資料夾路徑
    :return: 圖片數量
    """
    file_list = os.listdir(source_folder_path)
    print(f"{source_folder_path} 資料夾中的圖片數量： {len(file_list)}")

def main():
    # 移動來源資料夾的照片目標資料夾
    source_folder2folder = "../datasets/original_widerface/WIDERFACE_train"  # 替換成包含所有照片的來源資料夾路徑
    destination_folder2folder = "../datasets/original_widerface/WIDERFACE_train/images"

    # 扁平化 WIDER_val 資料夾內的照片
    source_folder = "" # 替換成包含62個資料夾的來源資料夾路徑
    destination_folder = ""

    # 執行圖片移動功能
    # flatten_images_to_destination(source_folder, destination_folder)
    move_images_between_folders(source_folder2folder, destination_folder2folder)

    # 查看圖片數量
    check_folder_img_size(destination_folder2folder)

if __name__ == "__main__":
    main()

