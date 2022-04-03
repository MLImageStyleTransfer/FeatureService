import pytest
import typing as tp

from PIL import Image
from image_editors import grayscale_transform, crop_transform, contrast_transform
from image_editors import brightness_transform, colorfulness_transform


@pytest.fixture(scope="module")
def image() -> tp.Generator[Image.Image, None, None]:
    with Image.open("./img.png") as image:
        yield image


def test_grayscaler(image: Image.Image) -> None:
    result: Image.Image = grayscale_transform(image)
    assert result.size == image.size


@pytest.mark.parametrize("upper_left, lower_right", [((100, 100), (500, 500)),
                                                     ((100, 200), (200, 210)),
                                                     ((0, 50), (150, 51))])
def test_cropper(image: Image.Image, upper_left: tuple[int, int],
                 lower_right: tuple[int, int]) -> None:
    result: Image.Image = crop_transform(image, upper_left, lower_right)
    assert result.size == (lower_right[0] - upper_left[0], lower_right[1] - upper_left[1])


@pytest.mark.parametrize("upper_left, lower_right", [((600, 400), (500, 500)),
                                                     ((500, 400), (500, 500)),
                                                     ((300, 500), (500, 500))])
def test_cropper_fail(image: Image.Image, upper_left: tuple[int, int],
                      lower_right: tuple[int, int]) -> None:
    with pytest.raises(AssertionError):
        crop_transform(image, upper_left, lower_right)


def check_result_equality(image: Image.Image, first_image: Image.Image, second_image: Image.Image,
                          change_factor: float) -> None:
    if change_factor == 1:
        assert (first_image.size == image.size) and (second_image.size == image.size)
        assert list(first_image.getdata()) == list(image.getdata())
        assert list(second_image.getdata()) == list(image.getdata())
    else:
        assert (first_image.size == second_image.size)
        assert list(first_image.getdata()) == list(second_image.getdata())


@pytest.mark.parametrize("contrast_factor", [0, 0.5, 1, 1.5, 2])
def test_contrast_editor(image: Image.Image, contrast_factor: float) -> None:
    image = crop_transform(image, (100, 100), (150, 150))
    result1: Image.Image = contrast_transform(image, contrast_factor)
    result2: Image.Image = contrast_transform(image, contrast_factor * 100)

    check_result_equality(image, result1, result2, contrast_factor)


@pytest.mark.parametrize("contrast_factor", [-5, -1, -0.5, -0.01, 201, 250])
def test_contrast_editor_fail(image: Image.Image, contrast_factor: float) -> None:
    with pytest.raises(AssertionError):
        contrast_transform(image, contrast_factor)


@pytest.mark.parametrize("brightness_factor", [0, 0.5, 1, 1.5, 2])
def test_brightness_editor(image: Image.Image, brightness_factor: float) -> None:
    image = crop_transform(image, (400, 400), (450, 450))
    result1: Image.Image = brightness_transform(image, brightness_factor)
    result2: Image.Image = brightness_transform(image, brightness_factor * 100)

    check_result_equality(image, result1, result2, brightness_factor)


@pytest.mark.parametrize("brightness_factor", [-5, -1, -0.1, 201, 250])
def test_brightness_editor_fail(image: Image.Image, brightness_factor: float) -> None:
    with pytest.raises(AssertionError):
        brightness_transform(image, brightness_factor)


@pytest.mark.parametrize("color_factor", [0, 0.5, 1, 1.5, 2])
def test_colorfulness_editor(image: Image.Image, color_factor: float) -> None:
    image = crop_transform(image, (300, 300), (310, 310))
    result1: Image.Image = colorfulness_transform(image, color_factor)
    result2: Image.Image = colorfulness_transform(image, color_factor * 100)

    check_result_equality(image, result1, result2, color_factor)


@pytest.mark.parametrize("color_factor", [-5, -1, -0.1, 201, 250])
def test_colorfulness_editor_fail(image: Image.Image, color_factor: float) -> None:
    with pytest.raises(AssertionError):
        colorfulness_transform(image, color_factor)
    with pytest.raises(AssertionError):
        colorfulness_transform(image, color_factor * 100)
