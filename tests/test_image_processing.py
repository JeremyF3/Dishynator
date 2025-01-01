import pytest
import numpy as np
from src.image_processing import calculate_red_ratio


def test_calculate_red_ratio():
    """Test the red pixel ratio calculation."""
    # Create a test image with known red pixels
    test_image = np.zeros((100, 100, 3), dtype=np.uint8)
    test_image[0:50, 0:50] = [255, 0, 0]  # Red square
    
    ratio, mask = calculate_red_ratio(test_image)
    assert ratio == pytest.approx(0.25, rel=1e-2)
    assert mask.shape == (100, 100)  # Check mask dimensions 