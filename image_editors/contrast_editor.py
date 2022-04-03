from PIL import Image, ImageEnhance


def contrast_transform(image: Image.Image, contrast_factor: float) -> Image.Image:
    """
    This function changes contrast of the image
    :param image: image for contrast changing
    :param contrast_factor: contrast factor takes value in [0, 2] (or [0, 200]).
           If it equals to 1 (or 100), then the image will not be changed
    :return: Modified image
    """
    assert (0 <= contrast_factor <= 2) or (0 <= contrast_factor <= 200)

    if contrast_factor > 2:
        contrast_factor /= 100

    contrast_editor: ImageEnhance.Contrast = ImageEnhance.Contrast(image)
    modified_image: Image.Image = contrast_editor.enhance(contrast_factor)
    return modified_image
