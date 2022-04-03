import typing as tp
from PIL import Image

from app.utils import image_base64_encode, image_base64_decode


ImageEditor: tp.TypeAlias = tp.Callable[[Image.Image], Image.Image]


def controller(base64_encoded_image: str, callback: ImageEditor) -> str:
    """
    Controller takes image, encoded with base64, applies on of the image editors
    using callback, encodes it back into base64 and returns
    :param base64_encoded_image: input image for modifying
    :param callback: one of the image editors: cropper, grayscaler, brightness,
           colorfulness or contrast editor
    :return: modified image
    """
    image: Image.Image = image_base64_decode(base64_encoded_image)
    result: Image.Image = callback(image)
    return image_base64_encode(result)
