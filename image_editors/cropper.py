from PIL import Image


def crop_transform(image: Image.Image, upper_left: tuple[int, int],
                   lower_right: tuple[int, int]) -> Image.Image:
    """
    This function crops the image.
    :param image: image for cropping.
    :param upper_left: left upper corner for cropping.
    :param lower_right: right down corner for cropping.
    :return:
    """
    assert (upper_left[0] < lower_right[0]) and \
           (upper_left[1] < lower_right[1])
    return image.crop(
        (upper_left[0], upper_left[1], lower_right[0], lower_right[1])
    )
