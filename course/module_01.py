# -*- coding: utf-8 -*-
# Module 1: Getting Started with Images

# --- Third Party Libraries ---
# cv2: OpenCV library for computer vision, machine learning, and image processing.
#      It can process images and videos to identify objects, faces, or even the handwriting of a human.
import cv2

# --- App modules ---
from .constants import IMAGE_SUB_FOLDER_
from helper import show_helper, os_helper


def plot_image(image_file_: str,
               cv2_flag_: int,
               plot_color_map_: str = "",
               print_it_: bool = False):
    """
    Read and plot image file
    :param image_file_: filename of the image file to process
    :param cv2_flag_: to read image with open cv
    :param plot_color_map_: color map to display image with matplotlib
    :param print_it_: flag to print or not the image
    """
    file_exists_, full_image_path_ = os_helper.file_exists(image_file_, *IMAGE_SUB_FOLDER_)

    if file_exists_:
        # Load image with OpenCV
        image_ = cv2.imread(full_image_path_, cv2_flag_)

        # Display image attributes
        print('Image dimensions:', image_.shape)
        print('Image data type :', image_.dtype)

        if print_it_:
            # Display image in Jupyter NB with: IPython.display.Image(filename=full_image_path_)

            # Print the image data (pixel values), if the image was read like:
            #  - cv2.IMREAD_GRAYSCALE is a 2D numpy array, each pixel has 8-bits (0,255)
            #  - cv2.IMREAD_COLOR is a 3D numpy array, each pixel has another array with its color channel (BGR format)
            print(image_)

        if plot_color_map_ == '':
            # Set the colormap to use in matplotlib, from the OpenCV flag used to open the file
            if cv2_flag_ == cv2.IMREAD_COLOR:
                plot_color_map_ = None
            else:
                plot_color_map_ = 'gray'

        if cv2_flag_ == cv2.IMREAD_COLOR:
            # matplotlib expects the image in RGB format while OpenCV stores images in BGR format.
            # Therefore, for a correct display, it will be necessary to invert the image channels.
            # image_ = image_[:, :, ::-1]  # ..-1 is used to revert / invert  order

            # Another way could be
            image_ = cv2.cvtColor(image_, cv2.COLOR_BGR2RGB)

        # Show image
        show_helper.plt_show([image_], [image_file_], [plot_color_map_])

    else:
        print(f'There is not file {full_image_path_}')


def split_image(image_file_: str):
    """
    Splits the image into the B,G,R components
    :param image_file_: filename of the image file to process
    """
    file_exists_, full_image_path_ = os_helper.file_exists(image_file_, *IMAGE_SUB_FOLDER_)

    if file_exists_:
        # Load image with OpenCV in default mode
        image_ = cv2.imread(full_image_path_)

        # Split the image into the B,G,R components
        b_channel_, g_channel_, r_channel_ = cv2.split(image_)

        # Merge the individual channels into a BGR image
        image_ = cv2.merge((b_channel_, g_channel_, r_channel_))

        # Prepare display the image and channels
        images_titles_ = ['Red channel', 'Green channel', 'Blue channel', 'Full Merged Image']
        color_maps_ = ['Reds', 'Greens', 'Blues', None]

        # Show images with matplotlib
        # Invert the image channels for a correct display with matplotlib
        images_ = [b_channel_, g_channel_, r_channel_, image_[:, :, ::-1]]
        show_helper.plt_show(images_, images_titles_, color_maps_)

        # Show images with OpenCV
        # images_ = [b_channel_, g_channel_, r_channel_, image_]
        # cv2_show(images_, images_titles_)

    else:
        print(f'There is not file {full_image_path_}')


def convert_color_space(image_file_: str):
    """
    Converts color space of the image to HSV and split it into the Hue,Saturation,Value components
    :param image_file_: filename of the image file to process
    """
    file_exists_, full_image_path_ = os_helper.file_exists(image_file_, *IMAGE_SUB_FOLDER_)

    if file_exists_:
        # Load image with OpenCV in default mode
        image_ = cv2.imread(full_image_path_)

        # Convert an image from one color space (BGR) to another (HSV)
        hsv_image_ = cv2.cvtColor(image_, cv2.COLOR_BGR2HSV)

        # Split the image into the H,S,V components
        # hue (matiz): represents the color of the image
        # saturation: represents the intensity of the color, it can be thought as pure red versus dull (apagado) red
        # value: represents the bright (brillo/luminosidad), how light or dark is irrespective of the color itself
        hue_channel_, saturation_channel_, value_channel_ = cv2.split(hsv_image_)

        # Prepare display the image and channels
        images_titles_ = ['Hue channel', 'Saturation channel', 'Value channel', 'HSV Image', 'Original Image']
        color_maps_ = ['gray', 'gray', 'gray', None, None]

        # Show images with matplotlib
        # Invert the image channels for a correct display with matplotlib
        images_ = [hue_channel_, saturation_channel_, value_channel_, hsv_image_[:, :, ::-1], image_[:, :, ::-1]]
        show_helper.plt_show(images_, images_titles_, color_maps_)

    else:
        print(f'There is not file {full_image_path_}')


def modify_hue_channel(image_file_: str,
                       increment_: int,
                       save_: bool = False):
    """
    Converts color space of the image to HSV and modifies Hue channel
    :param image_file_: filename of the image file to process
    :param increment_: to modify hue channel
    :param save_: flag to save or not the new gotten image
    """
    file_exists_, full_image_path_ = os_helper.file_exists(image_file_, *IMAGE_SUB_FOLDER_)

    if file_exists_:
        # Load image with OpenCV in default mode
        image_ = cv2.imread(full_image_path_)

        # Convert an image from one color space (BGR) to another (HSV)
        hsv_image_ = cv2.cvtColor(image_, cv2.COLOR_BGR2HSV)

        # Split the image into the H,S,V components
        hue_channel_, saturation_channel_, value_channel_ = cv2.split(hsv_image_)

        # Modify hue channel shifting the color spectrum
        new_hue_channel_ = hue_channel_ + increment_
        print(hue_channel_[:1, :10], '\t', new_hue_channel_[:1, :10])

        # Merge new HSV image
        new_hsv_image_ = cv2.merge((new_hue_channel_, saturation_channel_, value_channel_))

        # Convert to BGR color space
        new_image_ = cv2.cvtColor(new_hsv_image_, cv2.COLOR_HSV2BGR)

        # Prepare display the image and channels
        images_titles_ = ['Hue channel', 'New Hue channel', 'HSV Image', 'New HSV Image', 'Original Image', 'New image']
        color_maps_ = ['gray', 'gray', None, None, None, None]

        # Show images with matplotlib
        # Invert the image channels for a correct display with matplotlib
        images_ = [hue_channel_, new_hue_channel_,
                   hsv_image_[:, :, ::-1], new_hsv_image_[:, :, ::-1],
                   image_[:, :, ::-1], new_image_[:, :, ::-1]]
        show_helper.plt_show(images_, images_titles_, color_maps_)

        # Show images with OpenCV
        # images_ = [hue_channel_, new_hue_channel_, hsv_image_, new_hsv_image_, image_, new_image_]
        # show_helper.cv2_show(images_, images_titles_)

        # Save the image, but not save
        if save_:
            cv2.imwrite(full_image_path_.replace(image_file_, f'new_{image_file_}'), new_image_)

    else:
        print(f'There is not file {full_image_path_}')
