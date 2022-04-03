from PIL import Image, ImageEnhance


def colorfulness_transform(image: Image.Image, color_factor: float) -> Image.Image:
    """
    This function changes colorfulness of the image
    :param image: image for colorfulness changing
    :param color_factor: factor takes value in [0, 2] (or [0, 200])
           If it equals to 1, then the image will not be changed
    :return: modified image
    """
    assert (0 <= color_factor <= 2) or (0 <= color_factor <= 200)

    if color_factor > 2:
        color_factor /= 100

    colorfulness_editor: ImageEnhance = ImageEnhance.Color(image)
    modified_image: Image.Image = colorfulness_editor.enhance(color_factor)
    return modified_image
