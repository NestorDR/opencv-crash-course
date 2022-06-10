# -*- coding: utf-8 -*-
# Module 4: Image Enhancement

# --- Third Party Libraries ---
# cv2: OpenCV library for computer vision, machine learning, and image processing.
#      It can process images and videos to identify objects, faces, or even the handwriting of a human.
import cv2
# numpy: library for array processing for numbers, strings, records, and objects.
import numpy as np

# --- Python modules ---
# textwrap: provides formatting of text by adjusting the line breaks in the input paragraph.
import textwrap

# --- App modules ---
from .constants import IMAGE_SUB_FOLDER_
from helper import show_helper, os_helper


def add_subtract_brightness(image_file_: str):
    """
    Add/Subtract the intensity values of each pixel by the same amount to in/decreasing Brightness
    :param image_file_: filename of the image file to process
    """
    file_exists_, full_image_path_ = os_helper.file_exists(image_file_, *IMAGE_SUB_FOLDER_)

    if file_exists_:
        # Load image with OpenCV. Image is grayscale, but is read in color because it will be annotated in color.
        image_ = cv2.imread(full_image_path_, cv2.IMREAD_COLOR)

        # In/Decreasing the intensity values of each pixel by the same amount will result
        #  in a global in/decrease in the brightness.
        matrix = np.ones(image_.shape, dtype="uint8") * 50

        # Use add & subtract functions, to add & subtract the matrix from de original image, to in/decrease brightness.
        image_brighter_ = cv2.add(image_, matrix)
        image_darker_ = cv2.subtract(image_, matrix)

        # Prepare display the images
        images_titles_ = ['Original Image', 'Image Brighter', 'Image Darker']

        # Show images with OpenCV
        images_ = [image_, image_brighter_, image_darker_]
        show_helper.cv2_show(images_, images_titles_)
    else:
        print(f'There is not file {full_image_path_}')


def multiply_contrast(image_file_: str):
    """
    Multiply the intensity values with a constant to in/decrease the Contrast of the image, which is the difference in
      the intensity values of the pixels of an image.
    If factor > 1 the difference is larger, so more contrast. But if factor < 1 the difference is smaller, so less
      contrast.
    :param image_file_: filename of the image file to process
    """
    file_exists_, full_image_path_ = os_helper.file_exists(image_file_, *IMAGE_SUB_FOLDER_)

    if file_exists_:
        # Load image with OpenCV. Image is grayscale, but is read in color because it will be annotated in color.
        image_ = cv2.imread(full_image_path_, cv2.IMREAD_COLOR)

        # In/Decreasing the difference in the intensity values of the pixels of an image will result
        #  in a global in/decrease in the contrast
        dark_matrix_ = np.ones(image_.shape) * 0.5          # to decrease contrast
        bright_matrix_ = np.ones(image_.shape) * 1.2        # to increase contrast

        # Use multiply functions, to in/decrease contrast the matrix from de original image,
        image_darker_ = np.uint8(cv2.multiply(np.float64(image_), dark_matrix_))
        image_brighter_ = np.uint8(cv2.multiply(np.float64(image_), bright_matrix_))            # with overflow issue

        # Add multiline observation about overflow issue. Wraps the text with textwrap.wrap
        text_ = 'The values which are already high, are becoming greater than 255. Thus, the overflow issue.'
        wrapped_text_ = textwrap.wrap(text_, width=int(len(text_) * 0.60))
        font_face_ = cv2.FONT_HERSHEY_DUPLEX
        font_scale_ = 0.8
        font_thickness_ = 1
        bgr_color_ = (0, 255, 255)            # Yellow rgb(255, 255, 0)
        # Calculate the interlinear gap
        text_size_ = cv2.getTextSize(wrapped_text_[0], font_face_, font_scale_, font_thickness_)[0]
        gap_ = text_size_[1] + 5
        # Initialize the position of the text in the image
        left_margin_, top_margin_ = 180, 280
        # Add lines of text
        for line_ in wrapped_text_:
            # Add a line of text
            cv2.putText(image_brighter_, line_, org=(left_margin_, top_margin_), fontFace=font_face_,
                        fontScale=font_scale_, color=bgr_color_, thickness=font_thickness_,
                        lineType=cv2.LINE_AA)
            # Calculate top margin for the next line
            top_margin_ += gap_

        # Prepare display the images
        images_titles_ = ['Original Image', 'Lower Contrast', 'Higher Contrast with Overflow',
                          'Higher Contrast with Adjusted Overflow']

        # Handling Overflow using np.clip
        image_brighter_handled = np.uint8(np.clip(cv2.multiply(np.float64(image_), bright_matrix_), 0, 255))

        # Show images with OpenCV
        images_ = [image_, image_darker_, image_brighter_, image_brighter_handled]
        show_helper.cv2_show(images_, images_titles_)
    else:
        print(f'There is not file {full_image_path_}')
