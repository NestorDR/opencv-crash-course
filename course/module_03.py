# -*- coding: utf-8 -*-
# Module 3: Image Annotation

# --- Third Party Libraries ---
# cv2: OpenCV library for computer vision, machine learning, and image processing.
#      It can process images and videos to identify objects, faces, or even the handwriting of a human.
import cv2

# --- App modules ---
from .constants import IMAGE_SUB_FOLDER_
from helper import show_helper, os_helper


def draw_line(image_file_: str):
    """
    Annotates an image drawing a line on it
    :param image_file_: filename of the image file to process
    """
    file_exists_, full_image_path_ = os_helper.file_exists(image_file_, *IMAGE_SUB_FOLDER_)

    if file_exists_:
        # Load image with OpenCV. Image is grayscale, but is read in color because it will be annotated in color.
        image_ = cv2.imread(full_image_path_, cv2.IMREAD_COLOR)

        # clone image to work on it
        image_line_ = image_.copy()
        
        # Draw a line on the image which starts from (200,100) and ends at (400,100), its attributes will be
        #   Color ...: YELLOW (recall: OpenCV uses BGR format)
        #   Thickness: 5px
        #   Line type: cv2.LINE_AA. Antialiasing is a sophisticated technique for rendering a line involves using
        #              partially transparent pixels along with opaque pixels, resulting in lines that the human eye
        #              perceives as more smooth.
        #              Visit https://hacksd.wordpress.com/2020/03/20/exploring-line-types-in-opencv/
        point_01_ = (200, 100)
        point_02_ = (400, 100)
        yellow_bgr_ = (0, 255, 255)
        cv2.line(image_line_, point_01_, point_02_, color=yellow_bgr_, thickness=5, lineType=cv2.LINE_AA)

        # Prepare display the images
        images_titles_ = ['Original Image', 'Annotated Image']

        # Show images with OpenCV
        images_ = [image_, image_line_]
        show_helper.cv2_show(images_, images_titles_)

    else:
        print(f'There is not file {full_image_path_}')


def draw_circle(image_file_: str):
    """
    Annotates an image drawing a circle on it
    :param image_file_: filename of the image file to process
    """
    file_exists_, full_image_path_ = os_helper.file_exists(image_file_, *IMAGE_SUB_FOLDER_)

    if file_exists_:
        # Load image with OpenCV. Image is grayscale, but is read in color because it will be annotated in color.
        image_ = cv2.imread(full_image_path_, cv2.IMREAD_COLOR)

        # clone image to work on it
        image_circle_ = image_.copy()

        # Draw a circle on the image centered on (900,500) with radius 100, its attributes will be
        #   Color ...: RED (recall: OpenCV uses BGR format)
        #   Thickness: 5px
        #   Line type: cv2.LINE_AA. Antialiasing is a sophisticated technique for rendering a line involves using
        #              partially transparent pixels along with opaque pixels, resulting in lines that the human eye
        #              perceives as more smooth.
        #              Visit https://hacksd.wordpress.com/2020/03/20/exploring-line-types-in-opencv/
        #   Thickness: of the outline if positive, but if it is negative value it will result in a filled figure.
        red_bgr_ = (0, 0, 255)
        cv2.circle(image_circle_, center=(900, 500), radius=100, color=red_bgr_, thickness=5, lineType=cv2.LINE_AA)

        # Prepare display the images
        images_titles_ = ['Original Image', 'Annotated Image']

        # Show images with OpenCV
        images_ = [image_, image_circle_]
        show_helper.cv2_show(images_, images_titles_)

    else:
        print(f'There is not file {full_image_path_}')


def draw_rectangle(image_file_: str):
    """
    Annotates an image drawing a rectangle on it
    :param image_file_: filename of the image file to process
    """
    file_exists_, full_image_path_ = os_helper.file_exists(image_file_, *IMAGE_SUB_FOLDER_)

    if file_exists_:
        # Load image with OpenCV. Image is grayscale, but is read in color because it will be annotated in color.
        image_ = cv2.imread(full_image_path_, cv2.IMREAD_COLOR)

        # clone image to work on it
        image_rectangle_ = image_.copy()

        # Draw a rectangle on the image which starts from (500,100) and ends at (700,600), its attributes will be
        #   Color ...: RED (recall: OpenCV uses BGR format)
        #   Thickness: 5px
        #   Line type: cv2.LINE_8. 8-connected pixel connectivity
        #              Visit https://hacksd.wordpress.com/2020/03/20/exploring-line-types-in-opencv/
        #   Thickness: of the outline if positive, but if it is negative value it will result in a filled figure.
        rose_bgr_ = (106, 58, 243)      # https://htmlcolorcodes.com/colors/rose/ rgb(243, 58, 106)
        cv2.rectangle(image_rectangle_, pt1=(500, 100), pt2=(700, 600), color=rose_bgr_, thickness=5,
                      lineType=cv2.LINE_8)

        # Prepare display the images
        images_titles_ = ['Original Image', 'Annotated Image']

        # Show images with OpenCV
        images_ = [image_, image_rectangle_]
        show_helper.cv2_show(images_, images_titles_)

    else:
        print(f'There is not file {full_image_path_}')


def put_text(image_file_: str):
    """
    Annotates an image adding text on it
    :param image_file_: filename of the image file to process
    """
    file_exists_, full_image_path_ = os_helper.file_exists(image_file_, *IMAGE_SUB_FOLDER_)

    if file_exists_:
        # Load image with OpenCV. Image is grayscale, but is read in color because it will be annotated in color.
        image_ = cv2.imread(full_image_path_, cv2.IMREAD_COLOR)

        # clone image to work on it
        image_text_ = image_.copy()

        # Write some text on the image, its attributes will be
        #   Text: string to be written.
        #   Origin ...: (50,700) bottom-left corner of the text string in the image
        #   Font Face : is the font type
        #   Color ....: (255, 0, 0)
        #   Font Scale: 2.1 factor that is multiplied by the font-specific base
        #   Thickness : 2
        #   Line type : cv2.LINE_AA. Antialiasing is a sophisticated technique for rendering a line involves using
        #              partially transparent pixels along with opaque pixels, resulting in lines that the human eye
        #              perceives as more smooth.
        #              Visit https://hacksd.wordpress.com/2020/03/20/exploring-line-types-in-opencv/
        #   Thickness: of the outline if positive, but if it is negative value it will result in a filled figure.
        text_ = 'Apollo 11 Saturn V Launch, July 16, 1969'
        font_face_ = cv2.FONT_HERSHEY_DUPLEX
        font_scale_ = 1.1
        white_bgr_ = (255, 255, 255)
        cv2.putText(image_text_, text_, org=(50, 700), fontFace=font_face_, fontScale=font_scale_,
                    color=white_bgr_, thickness=2, lineType=cv2.LINE_AA)

        # Prepare display the images
        images_titles_ = ['Original Image', 'Annotated Image']

        # Show images with OpenCV
        images_ = [image_, image_text_]
        show_helper.cv2_show(images_, images_titles_)

    else:
        print(f'There is not file {full_image_path_}')
