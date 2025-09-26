# Automated Detection and Blurring of Sensitive Information

## Introduction
This project fine-tunes YOLOv8 models to automatically detect and blur sensitive content in public imagery, focusing on faces and vehicle license plates. Training leverages curated datasets and a custom YOLOv8 configuration, while the inference pipeline applies Gaussian blurring to every detected region so that footage can be shared without exposing personal data.

## Features
| Feature | Summary |
|---|---|
| Custom YOLOv8 detector for sensitive content | Tailored YOLOv8 configuration and dataset definition covering two classes (`face` and `license plate`) to fit privacy-preserving objectives. |
| End-to-end video anonymization workflow | Sample inference script loads trained weights, processes video streams frame-by-frame, and blurs detections in real time while reporting instantaneous and average FPS. |
| Dataset preparation utilities | Helper scripts flatten raw folders, convert WIDER FACE annotations to YOLO format, validate YAML paths, and inspect image resolutions to streamline data engineering for training. |
| Training artifacts and benchmarks | The `runs/detect/512` experiment demonstrates training settings (e.g., 512×512 inputs, 100 epochs) and reaches 0.90 precision, 0.75 recall, and 0.79 mAP@0.50 on the validation split, providing a baseline for future iterations. |

## Main Dependencies
- Python 3.10+
- [Ultralytics YOLO](https://docs.ultralytics.com/) (YOLOv8 models and training interface)
- OpenCV (video I/O and Gaussian blurring)
- NumPy (array operations and metrics logging)
- Pillow (image metadata and preprocessing utilities)
- PyYAML (dataset configuration validation)

## Project Report
The full methodology, experiments, and findings are summarized in the [Automated Detection and Blurring of Sensitive Information project report](Automated%20Detection%20and%20Blurring%20of%20Sensitive%20Information.pdf).
