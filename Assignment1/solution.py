#!/usr/bin/env python3
    
#To run: python3 a1.py --image <path to your image>
#        python3 a1.py (uses default path = "pear.png")       

#Using "as" nicknames a library so you don't have to use the full name
import matplotlib.pyplot as plt
import numpy as np
import cv2
import argparse as ap

#Prevents python3 from failing
TODO = None

#----------------Basic Image Handling (15 marks)---------------------
#5 marks: Read an image and return a grayscale image
#Input: image_path = string path to the image
#Output: HxWx1 numpy array containing the image
def read_image(image_path):
    TODO

#5 marks: Save an image and return True is successful, False if not
#Input: image_to_save = 8 unsigned integer numpy array (image)
#       image_path = string path to save the image
#Output: True if image saved successfully, False otherwise
def save_image(image_to_save, image_path):
    TODO

#5 marks: Display image (you can use either cv2 or matplotlib
#Input: image_to_show = image to display
def show_image(image_to_show):
    TODO

#----------------Image Processing (35 marks)-------------------------
"""
Input: img = input HxWx1 grayscale image
       ksize = size of the kernel (default=use 11x11 kernel)
       padding = what kind of padding around the image do we want to use
Output: return unsigned 8b integer image
"""
def imfilter2d(img,ksize=9,padding=cv2.BORDER_REFLECT):
    #5 Mark: Create sharpen filter with a 9x9 Gaussian kernel with sigma 5, and unit
    #        impulse of 2 
    kernel = TODO

    #2 Mark: Create a float32 numpy array to save the result of the convolution
    result = TODO

    #5 Marks: Apply border padding to the image
    img_padded = TODO

    #20 marks: perform the convolution
    # 5 marks : sliding window that applies the convolution
    # 5 marks : get the values in the neighbourhood
    # 5 marks : perform the convolution
    # 5 marks : save the result
    #(BONUS 10 marks): your solution can handle other filter sizes 
    result = TODO

    #3 Marks: clip the result so that the values are in the range (0,255) and save as unsigned 8 bit integer
    result_clipped = TODO
    return result_clipped 


if __name__ == "__main__":
    #This library handles argument parsing.  You don't need to worry about this for this assignment.
    parser = ap.ArgumentParser()
    parser.add_argument("-i", "--image", help="Path to image", default="pear.png") 
    args = parser.parse_args()
    
    #Get the grayscale image
    img = read_image(args.image)
    #Show the image
    show_image(img)
    #Sharpen the image and return the result
    res = imfilter2d(img)
    #Show the sharpened image
    show_image(res)
    #Save the sharpened image as "sharpened.png"
    save_image(res, "sharpened.png")

