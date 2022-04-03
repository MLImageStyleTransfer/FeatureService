from app import app
from app.utils import get_port
from app.views import (index, grayscale_transform_view, crop_transform_view,  # noqa: F401
                       contrast_transform_view, colorfulness_transform_view,
                       brightness_transform_view)

if __name__ == "__main__":
    app.run(debug=True, port=get_port())
