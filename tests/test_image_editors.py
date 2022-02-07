import pytest
from PIL import Image
from image_editors import grayscale_transform, crop_transform


def test_grayscaler() -> None:
    image: Image.Image = Image.open("./img.png")
    result: Image.Image = grayscale_transform(image)

    assert result.size == image.size


def test_cropper() -> None:
    image: Image.Image = Image.open("./img.png")
    result = crop_transform(image, (100, 100), (500, 500))

    assert result.size == (400, 400)


def test_cropper_fail() -> None:
    image: Image.Image = Image.open("./img.png")

    with pytest.raises(AssertionError):
        crop_transform(image, (600, 400), (500, 500))

    with pytest.raises(AssertionError):
        crop_transform(image, (500, 400), (500, 500))

    with pytest.raises(AssertionError):
        crop_transform(image, (300, 500), (500, 500))
