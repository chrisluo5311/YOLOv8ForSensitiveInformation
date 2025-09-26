# Automated Detection and Blurring of Sensitive Information

## Introduction
This project fine-tunes YOLOv8 models to automatically detect and blur sensitive content in public imagery, focusing on faces and vehicle license plates. Training leverages curated datasets and a custom YOLOv8 configuration, while the inference pipeline applies Gaussian blurring to every detected region so that footage can be shared without exposing personal data.

## Features
- **Custom YOLOv8 detector for sensitive content** – the repository packages a tailored YOLOv8 configuration and dataset definition covering two classes (`face` and `license plate`) to fit privacy-preserving objectives.【F:yolov8.yaml†L1-L39】【F:datasets/All/data.yaml†L1-L10】
- **End-to-end video anonymization workflow** – a sample inference script loads trained weights, processes video streams frame-by-frame, and blurs detections in real time while reporting instantaneous and average FPS.【F:haopeng/test.py†L1-L66】
- **Dataset preparation utilities** – helper scripts flatten raw folders, convert WIDER FACE annotations to YOLO format, validate YAML paths, and inspect image resolutions to streamline data engineering for training.【F:util/move_dataset.py†L1-L66】【F:util/convert_WIDER_to_YOLO_format.py†L1-L63】【F:util/check_yaml_path.py†L1-L39】【F:haopeng/statics.py†L1-L37】
- **Training artifacts and benchmarks** – the `runs/detect/512` experiment demonstrates training settings (e.g., 512×512 inputs, 100 epochs) and reaches 0.90 precision, 0.75 recall, and 0.79 mAP@0.50 on the validation split, providing a baseline for future iterations.【F:runs/detect/512/args.yaml†L1-L68】【F:runs/detect/512/results.csv†L1-L102】

## Main Dependencies
- Python 3.10+
- [Ultralytics YOLO](https://docs.ultralytics.com/) (YOLOv8 models and training interface)
- OpenCV (video I/O and Gaussian blurring)
- NumPy (array operations and metrics logging)
- Pillow (image metadata and preprocessing utilities)
- PyYAML (dataset configuration validation)

## Project Report
The full methodology, experiments, and findings are summarized in the [Automated Detection and Blurring of Sensitive Information project report](Automated%20Detection%20and%20Blurring%20of%20Sensitive%20Information.pdf).
