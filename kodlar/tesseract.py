import cv2
from PIL import Image
import pytesseract
import argparse
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cap=cv2.VideoCapture(0)

while 1 :
    ret,frame=cap.read()


    img = Image.open(frame)
    print(img)
    text = pytesseract.image_to_string(img)
    print (text)
