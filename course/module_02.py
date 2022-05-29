# -*- coding: utf-8 -*-
# Module 2: Basic Image Manipulation

# --- Third Party Libraries ---
# cv2: OpenCV library for computer vision, machine learning, and image processing.
#      It can process images and videos to identify objects, faces, or even the handwriting of a human.
import cv2

# --- App modules ---
from .constants import IMAGE_SUB_FOLDER_
from helper import show_helper, os_helper


def modify_pixels(image_file_: str):
    """
    Accesses a pixel in a numpy matrix, using
             - matrix notation  np_matrix[row_number, col_number], or
             - slicing notation np_matrix[from_row_number:to_row_number+1, from_col_number:to_col_number+1]
    :param image_file_: filename of the image file to process
    """
    file_exists_, full_image_path_ = os_helper.file_exists(image_file_, *IMAGE_SUB_FOLDER_)

    if file_exists_:
        # Load image with OpenCV
        image_ = cv2.imread(full_image_path_, cv2.IMREAD_GRAYSCALE)

        # Copy image
        image_copy_ = image_.copy()

        # Modify cells [2,2], [2,3], [3,2], [3,3]
        image_copy_[2:4, 2:4] = 200
        print(image_copy_)

        # Prepare display the image and channels
        images_titles_ = ['Original Image', 'Image Copy']

        # Show images with OpenCV
        images_ = [image_, image_copy_]
        show_helper.cv2_show(images_, images_titles_)
    else:
        print(f'There is not file {full_image_path_}')


def crop_image(image_file_: str,
               top_cut_percentage_: float,
               bottom_cut_percentage_: float,
               left_cut_percentage_: float,
               cut_right_percentage_: float):
    """
    Crops an image selecting a specific (pixel) region of the image
    :param image_file_: filename of the image file to process
    :param top_cut_percentage_: top side cut percentage, value between 0 and 1
    :param bottom_cut_percentage_: bottom side cut percentage, value between 0 and 1
    :param left_cut_percentage_: left side cut percentage, value between 0 and 1
    :param cut_right_percentage_: right side cut percentage, value between 0 and 1
    """
    file_exists_, full_image_path_ = os_helper.file_exists(image_file_, *IMAGE_SUB_FOLDER_)

    if file_exists_:
        if top_cut_percentage_ < 0 or bottom_cut_percentage_ < 0 \
                or left_cut_percentage_ < 0 or cut_right_percentage_ < 0:
            print('Check the cut percentages, because they must be greater than 0.')
        elif top_cut_percentage_ + bottom_cut_percentage_ > 1:
            print('Check the top and bottom percentages, because their addition is greater than 1.')
            return
        elif left_cut_percentage_ + cut_right_percentage_ > 1:
            print('Check the left and right percentages, because their addition is greater than 1.')
            return

        # Load image with OpenCV
        image_ = cv2.imread(full_image_path_, cv2.IMREAD_COLOR)

        # Identify dimensions
        height_, width_, _ = image_.shape

        # Set cutting edges
        top = int(height_ * top_cut_percentage_)
        bottom = int(height_ * (1 - bottom_cut_percentage_))
        left_ = int(width_ * left_cut_percentage_)
        right_ = int(width_ * (1 - cut_right_percentage_))

        # Crop
        cropped_image_ = image_[top:bottom, left_:right_]

        # Prepare display the image and channels
        images_titles_ = ['Original Image', 'Cropped Image']

        # Show images with OpenCV
        images_ = [image_, cropped_image_]
        show_helper.cv2_show(images_, images_titles_)
    else:
        print(f'There is not file {full_image_path_}')


def resize_image(image_file_: str,
                 resize_factor_:  float):
    """
    Resizes image depending on the resize factor
    :param image_file_: filename of the image file to process
    :param resize_factor_: percentage factor to reduce and increase the size of the image maintaining the aspect ratio,
                           its value must be between 0 and 1
    """
    file_exists_, full_image_path_ = os_helper.file_exists(image_file_, *IMAGE_SUB_FOLDER_)

    if file_exists_:
        if not (0 < resize_factor_ < 1):
            print("Check the resize factor, because it must be between 0 and 1.")
            return

        # Load image with OpenCV
        image_ = cv2.imread(full_image_path_, cv2.IMREAD_COLOR)

        # Resize image reducing it, maintaining aspect ratio and using the scale factors parameters
        #   x (horizontal) and y (vertical)
        # To shrink an image, it will generally look best with INTER_AREA interpolation
        reduced_image_ = cv2.resize(image_, dsize=None, fx=resize_factor_, fy=resize_factor_,
                                    interpolation=cv2.INTER_AREA)

        # Get a new bigger size maintaining aspect ratio
        aspect_ratio_factor_ = 1 + resize_factor_
        desired_height_ = int(image_.shape[0] * aspect_ratio_factor_)
        desired_width_ = int(image_.shape[1] * aspect_ratio_factor_)
        desired_size_ = (desired_width_, desired_height_)
        # Resize image increasing it. maintaining aspect ratio and using desired size parameter (dsize)
        # To enlarge an image, it will generally look best with INTER_CUBIC interpolation
        #  (slow) or #INTER_LINEAR (faster but still looks OK)
        increased_image_ = cv2.resize(image_, dsize=desired_size_, interpolation=cv2.INTER_CUBIC)

        # Prepare display the image and channels
        images_titles_ = ['Original Image', 'Reduced Image', 'Increased Image']

        # Show images with OpenCV
        images_ = [image_, reduced_image_, increased_image_]
        show_helper.cv2_show(images_, images_titles_, False)
    else:
        print(f'There is not file {full_image_path_}')


def flip_image(image_file_: str):
    """
    Flips image in the three directions
    :param image_file_: filename of the image file to process
    """
    file_exists_, full_image_path_ = os_helper.file_exists(image_file_, *IMAGE_SUB_FOLDER_)

    if file_exists_:
        # Load image with OpenCV
        image_ = cv2.imread(full_image_path_, cv2.IMREAD_COLOR)

        # flipCode`: a flag to specify how to flip the array:
        #   0 means flipping around the x-axis,
        #   1 or positive value  means flipping around y-axis,
        #  -1 or negative value means flipping around both axes.

        image_flipped_horizontally_ = cv2.flip(image_, 1)
        image_flipped_vertically_ = cv2.flip(image_, 0)
        image_flipped_both = cv2.flip(image_, -1)

        # Prepare display the image and channels
        images_titles_ = ['Original Image', 'Image Flipped Horizontally', 'Image Flipped Vertically',
                          'Image Flipped Fully']

        # Show images with OpenCV
        images_ = [image_, image_flipped_horizontally_, image_flipped_vertically_, image_flipped_both]
        show_helper.cv2_show(images_, images_titles_)

    else:
        print(f'There is not file {full_image_path_}')
