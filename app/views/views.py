import flask
import typing as tp
from functools import partial
from flask import request, jsonify, Response

from app import app
from app.utils import get_port
from app.controller import controller
from image_editors import brightness_transform, colorfulness_transform, contrast_transform
from image_editors import crop_transform, grayscale_transform


@app.route("/")
def index() -> flask.Response:
    """
    This function draws hello-page for feature service
    """
    main_page: str = f"""
        <h1 width="100%" align="center">
            Backend feature-service!
            <br/>
            Started on port: {get_port('BACKEND')}
        </h1>
    """
    return flask.Response(main_page)


@app.route("/grayscaler/", methods=["POST"])
def grayscale_transform_view() -> flask.Response:
    """
    This function processes request for image grayscale transformation
    Request structure:
    {
        "image_code": str,
        "params": None
    }
    :return: flask.Response with structure:
    {
        "image_code": str
    }
    """
    request_data: tp.Optional[tp.Any] = request.get_json()
    response: flask.Response

    if isinstance(request_data, dict) and ("image_code" in request_data.keys()):
        image_code: str = request_data["image_code"]
        try:
            result_image_code: str = controller(image_code, grayscale_transform)
            response = jsonify({"image_code": result_image_code})
        except AssertionError:
            response = Response(status=400)
    else:
        response = Response(status=400)

    response.headers.add("Access-Control-Allow-Origin", f"http://localhost:{get_port('FRONTEND')}")
    return response


@app.route("/cropper/", methods=['POST'])
def crop_transform_view() -> flask.Response:
    """
    This function processes request for image cropping
    Request structure:
    {
        "image_code": str,
        "params": {
            "upper_left": tuple[int, int],
            "lower_right": tuple[int, int]
        }
    }
    :return: flask.Response with structure:
    {
        "image_code": str
    }
    """
    request_data: tp.Optional[tp.Any] = request.get_json()
    response: flask.Response

    if isinstance(request_data, dict) and ({"image_code", "params"} <= request_data.keys()) and \
            isinstance(request_data["params"], dict) and \
            ({"left_upper", "right_lower"} <= request_data["params"].keys()):
        image_code: str = request_data["image_code"]
        try:
            result_image_code: str = controller(
                image_code,
                partial(crop_transform,
                        upper_left=tuple(map(int, request_data["params"]["left_upper"])),
                        lower_right=tuple(map(int, request_data["params"]["right_lower"]))
                )
            )
            response = jsonify({"image_code": result_image_code})
        except AssertionError:
            response = Response(status=400)
    else:
        response = Response(status=400)

    response.headers.add("Access-Control-Allow-Origin", f"http://localhost:{get_port('FRONTEND')}")
    return response


@app.route("/contrast_editor/", methods=['POST'])
def contrast_transform_view() -> flask.Response:
    """
    This function processes request for image contrast editing
    Request structure:
    {
        "image_code": str,
        "params": {
            "contrast_factor": float,
        }
    }
    :return: flask.Response with structure:
    {
        "image_code": str
    }
    """
    request_data: tp.Optional[tp.Any] = request.get_json()
    response: flask.Response

    if isinstance(request_data, dict) and ({"image_code", "params"} <= request_data.keys()) and \
            isinstance(request_data["params"], dict) and \
            ("contrast_factor" in request_data["params"]):
        image_code: str = request_data["image_code"]
        try:
            result_image_code: str = controller(
                image_code,
                partial(contrast_transform,
                        contrast_factor=float(request_data["params"]["contrast_factor"])
                )
            )
            response = jsonify({"image_code": result_image_code})
        except AssertionError:
            response = Response(status=400)
    else:
        response = Response(status=400)

    response.headers.add("Access-Control-Allow-Origin", f"http://localhost:{get_port('FRONTEND')}")
    return response


@app.route("/colorfulness_editor/", methods=['POST'])
def colorfulness_transform_view() -> flask.Response:
    """
    This function processes request for image colorfulness editing
    Request structure:
    {
        "image_code": str,
        "params": {
            "color_factor": tuple[int, int],
        }
    }
    :return: flask.Response with structure:
    {
        "image_code": str
    }
    """
    request_data: tp.Optional[tp.Any] = request.get_json()
    response: flask.Response

    if isinstance(request_data, dict) and ({"image_code", "params"} <= request_data.keys()) and \
            isinstance(request_data["params"], dict) and \
            ("colorfulness_factor" in request_data["params"].keys()):
        image_code: str = request_data["image_code"]
        try:
            result_image_code: str = controller(
                image_code,
                partial(colorfulness_transform,
                        color_factor=float(request_data["params"]["colorfulness_factor"])
                )
            )
            response = jsonify({"image_code": result_image_code})
        except AssertionError:
            response = Response(status=400)
    else:
        response = Response(status=400)

    response.headers.add("Access-Control-Allow-Origin", f"http://localhost:{get_port('FRONTEND')}")
    return response


@app.route("/brightness_editor/", methods=['POST'])
def brightness_transform_view() -> flask.Response:
    """
    This function processes request for image brightness editing
    Request structure:
    {
        "image_code": str,
        "params": {
            "brightness_factor": tuple[int, int],
        }
    }
    :return: flask.Response with structure:
    {
        "image_code": str
    }
    """
    request_data: tp.Optional[tp.Any] = request.get_json()
    response: flask.Response

    if isinstance(request_data, dict) and ({"image_code", "params"} <= request_data.keys()) and \
            isinstance(request_data["params"], dict) and \
            ("brightness_factor" in request_data["params"].keys()):
        image_code: str = request_data["image_code"]
        try:
            result_image_code: str = controller(
                image_code,
                partial(brightness_transform,
                        brightness_factor=float(request_data["params"]["brightness_factor"])
                )
            )
            response = jsonify({"image_code": result_image_code})
        except AssertionError:
            response = Response(status=400)
    else:
        response = Response(status=400)

    response.headers.add("Access-Control-Allow-Origin", f"http://localhost:{get_port('FRONTEND')}")
    return response
