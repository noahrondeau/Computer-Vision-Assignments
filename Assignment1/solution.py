#!/usr/bin/env python3
    
#To run: python3 a1.py --image <path to your image>
#        python3 a1.py (uses default path = "pear.png")       

#Using "as" nicknames a library so you don't have to use the full name
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
    return cv2.imread(image_path, 0)

#5 marks: Save an image and return True is successful, False if not
#Input: image_to_save = 8 unsigned integer numpy array (image)
#       image_path = string path to save the image
#Output: True if image saved successfully, False otherwise
def save_image(image_to_save, image_path):
    TODO

#5 marks: Display image (you can use either cv2 or matplotlib
#Input: image_to_show = image to display
def show_image(image_to_show):
    cv2.imshow("Image", image_to_show)
    cv2.waitKey(0)

def single_clip(pixel):
    if pixel > 255.0:
        return 255.0
    elif pixel < 0.0:
        return 0.0
    else:
        return pixel

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
    impulse = np.zeros((ksize,ksize), dtype=np.float32)
    impulse[int((ksize-1)/2), int((ksize-1)/2)] = np.float32(2)
    gaussian1D = cv2.getGaussianKernel(ksize, 5,cv2.CV_32F)
    gaussian2D = np.outer(gaussian1D, gaussian1D)
    kernel = impulse - gaussian2D
    #2 Mark: Create a float32 numpy array to save the result of the convolution
    result = np.zeros(shape = img.shape, dtype = np.float32)
    #5 Marks: Apply border padding to the image
    pad_pixels = int((ksize-1)/2) # number of pixels to pad
    img_padded = cv2.copyMakeBorder(img,pad_pixels,pad_pixels,pad_pixels,pad_pixels, padding)

    #20 marks: perform the convolution
    # 5 marks : sliding window that applies the convolution
    # 5 marks : get the values in the neighbourhood
    # 5 marks : perform the convolution
    # 5 marks : save the result
    #(BONUS 10 marks): your solution can handle other filter sizes

    rows, cols = img_padded.shape
    # visit each pixel in every row
    # could probably use an iterator for this but then we would have to skip pixels in the padding
    # the classic ranged for loop will do the trick here. Not very pythonic though
    # Since the kernel is symmetric, convolution and correlation are the same, no need to flip
    for i in range(pad_pixels, rows-pad_pixels-1):
        for j in range(pad_pixels, cols-pad_pixels-1):
            # get the neighbourhood with slicing
            neighbourhood = img_padded[(i-pad_pixels):(i+pad_pixels+1), (j-pad_pixels):(j+pad_pixels+1)]
            new_pixel = np.sum(np.multiply(neighbourhood, kernel))
            result[i-pad_pixels, j-pad_pixels] = new_pixel

    #3 Marks: clip the result so that the values are in the range (0,255) and save as unsigned 8 bit integer
    npclip = np.vectorize(single_clip)
    result_clipped = np.uint8(npclip(result))
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

