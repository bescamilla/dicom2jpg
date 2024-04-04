pip install dicom2jpg

import numpy as np

ruta= '/content/drive/MyDrive/python/MRBRAIN.DCM'

import dicom2jpg

dicom_img_01 = "/content/drive/MyDrive/python/MRBRAIN.DCM"
dicom_dir = "/content/drive/MyDrive/python"
export_location = "/content/drive/MyDrive/python/BMP_files"

# convert single DICOM file to jpg format
dicom2jpg.dicom2jpg(dicom_img_01)  

# convert all DICOM files in dicom_dir folder to png format
dicom2jpg.dicom2png(dicom_dir)  

# convert all DICOM files in dicom_dir folder to bmp, to a specified location
dicom2jpg.dicom2bmp(dicom_dir, target_root=export_location) 

# convert single DICOM file to numpy.ndarray for further use
img_data = dicom2jpg.dicom2img(dicom_img_01)

# convert DICOM ByteIO to numpy.ndarray
#img_data = dicom2jpg.io2img(dicomIO)