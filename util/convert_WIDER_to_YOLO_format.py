import os
from PIL import Image

def convert_widerface_to_yolo(widerface_label_path, image_dir, output_dir):
    """
    Converts WIDER FACE annotations to YOLO format.
    Parameters:
    - widerface_label_path: Path to the WIDER FACE annotation file.
    - image_dir: Directory containing the images.
    - output_dir: Directory to save the YOLO-formatted annotations.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(widerface_label_path, 'r') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line and not line.isdigit():
            print(line)
            image_name = os.path.basename(line)
            image_path = os.path.join(image_dir, image_name)
            image_name_without_ext = os.path.splitext(image_name)[0]
            label_file_path = os.path.join(output_dir, f"{image_name_without_ext}.txt")

            # Skip to next line and read num_faces
            i += 1
            num_faces = int(lines[i].strip())

            # If num_faces is 0, skip this image
            if num_faces == 0:
                i += 2  # Move to the next image entry
                continue

            # Skip file if label file already exists
            if os.path.exists(label_file_path):
                i += num_faces+1  # Skip the current faces data
                continue

            # Open image to get dimensions
            with Image.open(image_path) as img:
                image_width, image_height = img.size

            with open(label_file_path, 'w') as label_file:
                for _ in range(num_faces):
                    i += 1
                    bbox = list(map(int, lines[i].strip().split()[:4]))  # Only take x1, y1, w, h
                    x_min, y_min, width, height = bbox

                    # Convert to YOLO format
                    x_center = (x_min + width / 2) / image_width
                    y_center = (y_min + height / 2) / image_height
                    norm_width = width / image_width
                    norm_height = height / image_height

                    # Write in YOLO format with class_id as 0 for face
                    label_file.write(f"0 {x_center:.6f} {y_center:.6f} {norm_width:.6f} {norm_height:.6f}\n")
        i += 1

if __name__ == "__main__":
    # train
    WIDERFACE_train_label_path = "../datasets/original_widerface/train_label/wider_face_train_bbx_gt.txt"
    image_train_dir = "../datasets/original_widerface/train"
    output_train_dir = "../datasets/YOLO_format_widerface/train_label"

    # val
    WIDERFACE_val_label_path = "../datasets/original_widerface/val_label/wider_face_val_bbx_gt.txt"
    image_val_dir = "../datasets/original_widerface/val"
    output_val_dir = "../datasets/YOLO_format_widerface/val_label"

    # convert widerface format to yolo format
    convert_widerface_to_yolo(WIDERFACE_val_label_path, image_val_dir, output_val_dir)