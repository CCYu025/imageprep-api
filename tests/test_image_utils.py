# 余振中 (Yu Chen Chung)
# tests/test_image_utils.py

import os, io, pytest
from image_utils import process_image

# 由 __file__ 推回到根目錄，再載入 sample.jpg
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SAMPLE_JPG = os.path.join(ROOT, 'sample.jpg')


def load_sample_file():
    with open(SAMPLE_JPG, 'rb') as f:
        return io.BytesIO(f.read())

def test_process_image_grayscale():
    file = load_sample_file()
    result = process_image(file, mode="grayscale")
    assert isinstance(result, io.BytesIO)

def test_process_image_edge():
    file = load_sample_file()
    result = process_image(file, mode="edge")
    assert isinstance(result, io.BytesIO)

def test_process_image_blur():
    file = load_sample_file()
    result = process_image(file, mode="blur")
    assert isinstance(result, io.BytesIO)
    assert result.getbuffer().nbytes > 0

def test_process_image_sharpen():
    file = load_sample_file()
    result = process_image(file, mode="sharpen")
    assert isinstance(result, io.BytesIO)
    assert result.getbuffer().nbytes > 0

def test_process_image_rotate():
    file = load_sample_file()
    result = process_image(file, mode="rotate")
    assert isinstance(result, io.BytesIO)

def test_process_image_flip_horizontal():
    file = load_sample_file()
    result = process_image(file, mode="flip_horizontal")
    assert isinstance(result, io.BytesIO)

def test_process_image_flip_vertical():
    file = load_sample_file()
    result = process_image(file, mode="flip_vertical")
    assert isinstance(result, io.BytesIO)

def test_process_image_invert_colors():
    file = load_sample_file()
    result = process_image(file, mode="invert_colors")
    assert isinstance(result, io.BytesIO)

def test_invalid_mode_raises_value_error():
    file = load_sample_file()
    with pytest.raises(ValueError) as exc:
        process_image(file, mode="invalid_mode")
    assert "不支援的處理模式" in str(exc.value)

def test_process_image_empty_file():
    empty_file = io.BytesIO()
    with pytest.raises(ValueError) as exc:
        process_image(empty_file)
    assert "上傳的檔案為空" in str(exc.value)

def test_invalid_image_format():
    fake_file = io.BytesIO(b"This is not an image")
    with pytest.raises(ValueError) as exc:
        process_image(fake_file)
    assert "無法解析圖片" in str(exc.value)