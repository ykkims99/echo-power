
# ⚡ Echo-Power: AI-Assisted Voltage Abnormality Detection for Medical-Grade Transformers

![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-RPi%20%7C%20STM32%20%7C%20ESP32-blue)

## 🌍 Project Summary

**Echo-Power** is an open-source AI-powered detection system for identifying abnormal voltage conditions in miniature constant-voltage transformers used in **medical devices**, especially for **low-resource environments**.

> Developed with real-time 1D-CNN model inference optimized for **Raspberry Pi CM4**, **STM32**, and **ESP32**.

## 📁 Directory Structure

```
echo-power/
├── echo_power/                 # Python package
│   ├── detector.py             # TFLite model loader and inference
│   ├── preprocessor.py         # Signal normalization
│   ├── relay_control.py        # GPIO relay activation
│   ├── config.yaml             # Threshold configuration
│   └── example_run.py          # End-to-end inference demo
├── hardware/
│   ├── Echo-Power_Hardware_Design_Guide.docx     # Full schematic
│   ├── echo_power_hardware_schematic.png         # PCB layout
│   └── Echo-Power_BOM_List.xlsx                  # Bill of materials
├── LICENSE
└── README.md
```

## 🚀 How to Use

1. Clone this repository:
```bash
git clone https://github.com/ykkims99/echo-power.git
cd echo-power
```

2. Prepare Raspberry Pi GPIO and copy your TFLite model to `model/echo_power.tflite`.

3. Run demo:
```bash
python3 echo_power/example_run.py
```

## 📦 Model Details

- **Input**: Normalized voltage & current sequences (1000 samples)
- **Output**: Anomaly classification probabilities (e.g., normal, surge, undervoltage)
- **Size**: < 128KB TFLite
- **Latency**: ~20ms on CM4

## 📜 License

This project is licensed under the **MIT License**.

## ✉️ Citation

```
Kim, Y.K. (2025). Echo-Power: AI-Assisted Voltage Abnormality Detection for Medical Transformers. In submission to Scientific African.
```

---
Maintained with ❤️ by [@ykkims99](https://github.com/ykkims99)
