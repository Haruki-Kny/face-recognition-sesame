# Face Recogniton and Sesame by Python3

This project focuses on Face Recognition and Sesame(Smart lock) by Python3.

- Python3
- OpenCV
- pysesame3

## Usage

### Requirements 
```
pip install -r requirements.txt
```

### 1. Prepare Datasets
At first, please enter `1` and `1`.
```
python 01_dataset.py
```

### 2. Train
```
python 02_train.py
```

### 3. Recognition
```
python 03_recog.py
``` 
---
## If you have an opencv error
For example, ` AttributeError: module 'cv2' has no attribute 'face' `
try the code below
```
pip install opencv-contrib-python --upgrade
```
if it doesn't work
```
pip install opencv-contrib-python --user
```


