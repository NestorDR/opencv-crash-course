# -*- coding: utf-8 -*-

# --- Third Party Libraries ---
# cv2: OpenCV library for computer vision, machine learning, and image processing.
#      It can process images and videos to identify objects, faces, or even the handwriting of a human.
import cv2
# imutils: functions to make basic image processing functions such as translation, rotation, resizing, skeletonization,
#          and displaying
from imutils import resize
# matplotlib: library for creating static, animated, and interactive visualizations
import matplotlib.pyplot as plt


def plt_show(images_: [],
             image_titles_: [],
             color_maps_: []):
    """
    Shows images using matplotlib
    :param images_: images array to show
    :param image_titles_: strings array with the title of each image
    :param color_maps_: color maps array to show each image
    """

    plt.figure(figsize=(12, 6)).tight_layout(pad=0)  # figsize=(width, height) in inches
    # plt.subplots_adjust(bottom=0., left=0, top=1., right=1)
    plt.subplots_adjust(bottom=0.0,
                        top=0.96,
                        wspace=0.1,
                        hspace=0.1)
    length_ = len(images_)
    cols_ = length_ if length_ < 5 else 5
    rows_ = int(length_ / cols_) + (0 if length_ % cols_ == 0 else 1)

    # Show the channels amd full image
    for i_ in range(len(images_)):
        # subplot(<rows><cols><ordinal position #>
        position_ = rows_ * 100 + cols_ * 10 + (i_ + 1)

        # Add image to the plot, setting color map to selected scale for proper rendering.
        plt.subplot(position_).imshow(images_[i_], cmap=color_maps_[i_])

        # Set title of the image
        image_title_ = image_titles_[i_]
        plt.title(image_title_)

        # Hide axes and borders
        plt.axis('off')

        # Report array dimensions
        print(f'{image_title_} dimensions:', images_[i_].shape)

    # Display the images
    plt.show()


def cv2_show(images_: [],
             image_titles_: [],
             fit_image_: bool = True):
    """
    Shows images using OpenCV
    :param images_: images array to show
    :param image_titles_: strings array with the title of each image
    :param fit_image_: flag to adjust the image and keep it within the screen
    """
    # Show the image and channels
    for i_ in range(len(images_)):
        # Create window
        win_name_ = image_titles_[i_]
        cv2.namedWindow(win_name_, cv2.WINDOW_AUTOSIZE)

        # Downsize image maintaining aspect ratio and show it in the window
        if fit_image_:
            cv2.imshow(win_name_, resize(images_[i_], width=300))
        else:
            cv2.imshow(win_name_, images_[i_])

        # Report array dimensions
        print(f'{win_name_} dimensions (height x width):', images_[i_].shape)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
