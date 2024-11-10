import os

def count_files_in_folder(folder_path):
    try:
        # List all items in the directory
        items = os.listdir(folder_path)
        # Filter out directories, keeping only files
        files = [item for item in items if os.path.isfile(os.path.join(folder_path, item))]
        # Count the number of files
        num_files = len(files)
        return num_files
    except FileNotFoundError:
        print(f"The folder '{folder_path}' does not exist.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

if __name__ == "__main__":
    # train
    check_train_labels_folder_path = '../datasets/YOLO_format_widerface/train/labels'
    check_train_images_folder_path = '../datasets/YOLO_format_widerface/train/images'
    train_labels_file_count = count_files_in_folder(check_train_labels_folder_path)
    train_image_file_count = count_files_in_folder(check_train_images_folder_path)

    print(f"There are {train_labels_file_count} files in the folder '{check_train_labels_folder_path}'.")
    print(f"There are {train_image_file_count} files in the folder '{check_train_images_folder_path}'.")
    print("")
    # val
    check_val_labels_folder_path = '../datasets/YOLO_format_widerface/val/labels'
    check_val_images_folder_path = '../datasets/YOLO_format_widerface/val/images'
    va_labels_file_count = count_files_in_folder(check_val_labels_folder_path)
    val_image_file_count = count_files_in_folder(check_val_images_folder_path)

    print(f"There are {va_labels_file_count} files in the folder '{check_val_labels_folder_path}'.")
    print(f"There are {val_image_file_count} files in the folder '{check_val_images_folder_path}'.")