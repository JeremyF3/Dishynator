import cv2
import numpy as np
from PIL import Image
import io
from typing import Tuple
import numpy.typing as npt


def load_image(image_file):
    """Load an image file and convert to OpenCV format."""
    img = Image.open(image_file)
    return np.array(img)


def mask_to_bytes(mask):
    """Convert mask array to bytes for download."""
    mask_img = Image.fromarray(mask)
    buf = io.BytesIO()
    mask_img.save(buf, format="PNG")
    return buf.getvalue()


def calculate_red_ratio(
    image: npt.NDArray[np.uint8],
) -> Tuple[float, npt.NDArray[np.uint8]]:
    """Calculate the ratio of red pixels in the image."""
    # Convert to HSV for better color detection
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    # Define red color range (HSV)
    # Red wraps around in HSV, so we need two ranges
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])

    # Create masks for red pixels
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    red_mask = mask1 + mask2

    # Calculate ratio
    total_pixels = image.shape[0] * image.shape[1]
    red_pixels = np.count_nonzero(red_mask)
    ratio = red_pixels / total_pixels

    return ratio, red_mask
