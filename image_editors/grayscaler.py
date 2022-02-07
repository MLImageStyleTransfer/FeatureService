from PIL import Image, ImageEnhance


def grayscale_transform(colour_image: Image.Image) -> Image.Image:
    """
    This function transforms the image into gray shades
    :param colour_image: image for transformation
    :return: grayscale image
    """
    grayscaler: ImageEnhance.Color = ImageEnhance.Color(colour_image)
    grayscale_image = grayscaler.enhance(0)
    return grayscale_image
