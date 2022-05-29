# -*- coding: utf-8 -*-

# --- Third Party Libraries ---
# cv2: OpenCV library for computer vision, machine learning, and image processing.
#      It can process images and videos to identify objects, faces, or even the handwriting of a human.
import cv2

# --- Python modules ---
# sys: module which provides access to variables used or maintained by the interpreter and to functions that
#      interact strongly with the interpreter
import sys

# --- App modules ---
import course


# Use of __name__ & __main__
# When the Python interpreter reads a code file, it completely executes the code in it.
# For example, in a file my_module.py, when executed as the main program, the __name__ attribute will be '__main__',
# however if it is used importing it from another module: import my_module, the __name__ attribute will be 'my_module'.
if __name__ == '__main__':
    # Module 1: Getting Started with Images
    """ Show images with matplotlib, after seeing them close the windows to continue """
    course.module_01.plot_image('checkerboard_18x18.png', cv2.IMREAD_GRAYSCALE, 'gray')
    course.module_01.plot_image('checkerboard_fuzzy_18x18.jpg', cv2.IMREAD_GRAYSCALE)
    course.module_01.plot_image('coca-cola-logo.png', cv2.IMREAD_COLOR)
    course.module_01.plot_image('bicycle.jpg', cv2.IMREAD_COLOR)
    course.module_01.split_image('bicycle.jpg')
    course.module_01.convert_color_space('mafalda.jpg')
    course.module_01.modify_hue_channel('mafalda.jpg', 10, save_=False)

    # Module 2: Basic Image Manipulation
    """ Shows images with OpenCV, , after seeing them press any key to continue """
    course.module_02.modify_pixels('checkerboard_18x18.png')
    course.module_02.crop_image('bicycle.jpg', 0.30, 0.30, 0.05, 0.02)
    course.module_02.resize_image('mafalda.jpg', 0.50)
    course.module_02.flip_image('coca-cola-logo.png')

    # TODO Module 3: Image Annotation

    # TODO Module 4: Image Enhancement
    # TODO Module 5: Accessing the Camera
    # TODO Module 6: Read and Write Videos
    # TODO Module 7: Image Filtering and Edge Detection
    # TODO Module 8: Image Features and Image Alignment
    # TODO Module 9: Image Stitching and Creating Panoramas
    # TODO Module 10: High Dynamic Range Imaging (HDR)
    # TODO Module 11: Object Tracking
    # TODO Module 12: Face Detection
    # TODO Module 13: Object Detection
    # TODO Module 14: Pose Estimation using OpenPose

    # Terminate normally
    sys.exit(0)
