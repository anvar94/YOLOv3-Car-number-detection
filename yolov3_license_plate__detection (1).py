
from google.colab import drive
drive.mount('/content/drive')

!nvidia-smi

!ls '/content/drive/My Drive/yolo_custom_model_Training'

#!unzip '/content/drive/My Drive/yolo_custom_model_Training/custom_data.zip' -d '/content/drive/My Drive/yolo_custom_model_Training'

#!git clone 'https://github.com/AlexeyAB/darknet.git' '/content/drive/My Drive/yolo_custom_model_Training/darknet'

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/My Drive/yolo_custom_model_Training/darknet

!ls

!make

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/My Drive/yolo_custom_model_Training

!darknet/darknet

!python custom_data/creating-files-data-and-name.py

!python custom_data/creating-train-and-test-txt-files.py

!darknet/darknet detector train custom_data/labelled_data.data darknet/cfg/yolov3_custom.cfg custom_weight/darknet53.conv.74 -dont_show

