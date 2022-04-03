import flask
from flask import request, jsonify
from functools import partial

from app import app
from app.utils import get_port
from app.controller import controller
from image_editors import brightness_transform, colorfulness_transform, contrast_transform
from image_editors import crop_transform, grayscale_transform


@app.route('/')
def index() -> flask.Response:
    main_page: str = f"""
        <h1 width="100%" align="center">
            Backend feature-service!
            <br/>
            Started on port: {get_port(place="BACKEND")}
        </h1>
    """
    return flask.Response(main_page)


@app.route('/grayscaler/', methods=['POST'])
def grayscale_transform_view() -> flask.Response:
    value: str = str(request.data)[3:-2]
    res_file: str = controller(value, grayscale_transform)
    response: flask.Response = jsonify(res_file)

    response.headers.add("Access-Control-Allow-Origin", f"http://localhost:{get_port('FRONTEND')}")
    return response


@app.route('/cropper/', methods=['POST'])
def crop_transform_view() -> flask.Response:
    value: str = str(request.data)[3:-2]
    res_file: str = controller(value, partial(crop_transform, upper_left=(100, 100),
                                              lower_right=(200, 200)))
    response: flask.Response = jsonify(res_file)

    response.headers.add("Access-Control-Allow-Origin", f"http://localhost:{get_port('FRONTEND')}")
    return response


@app.route('/contrast_editor/', methods=['POST'])
def contrast_transform_view() -> flask.Response:
    value: str = str(request.data)[3:-2]
    res_file: str = controller(value, partial(contrast_transform, contrast_factor=1.5))
    response: flask.Response = jsonify(res_file)

    response.headers.add("Access-Control-Allow-Origin", f"http://localhost:{get_port('FRONTEND')}")
    return response


@app.route('/colorfulness_editor/', methods=['POST'])
def colorfulness_transform_view() -> flask.Response:
    value: str = str(request.data)[3:-2]
    res_file: str = controller(value, partial(colorfulness_transform, color_factor=1.5))
    response: flask.Response = jsonify(res_file)

    response.headers.add("Access-Control-Allow-Origin", f"http://localhost:{get_port('FRONTEND')}")
    return response


@app.route('/brightness_editor/', methods=['POST'])
def brightness_transform_view() -> flask.Response:
    value: str = str(request.data)[3:-2]
    res_file: str = controller(value, partial(brightness_transform, brightness_factor=1.5))
    response: flask.Response = jsonify(res_file)

    response.headers.add("Access-Control-Allow-Origin", f"http://localhost:{get_port('FRONTEND')}")
    return response
