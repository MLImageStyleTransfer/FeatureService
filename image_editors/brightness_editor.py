from PIL import Image, ImageEnhance


def brightness_transform(image: Image.Image, brightness_factor: float) -> Image.Image:
    """
    This function changes the brightness of the image
    :param image: image for brightness changing
    :param brightness_factor: factor takes value in [0, 2] (or [0, 200]).
           If it equals to 1, then the image will not be changed
    :return: Modified image
    """
    assert (0 <= brightness_factor <= 2) or (0 <= brightness_factor <= 200)

    if brightness_factor > 2:
        brightness_factor /= 100

    brightness_editor: ImageEnhance = ImageEnhance.Brightness(image)
    modified_image: Image.Image = brightness_editor.enhance(brightness_factor)
    return modified_image
