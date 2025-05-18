# 余振中 (Yu Chen Chung)
import cv2
import numpy as np
import io

def process_image(file, mode='grayscale'):
    """
    接收一張圖片與處理模式，使用 OpenCV 執行對應圖像處理。
    回傳處理後的 BytesIO 圖像檔案。
    """
    img_bytes = file.read()
    if not img_bytes:
        raise ValueError("上傳的檔案為空，請確認圖片檔案是否正確")

    # 解析圖像
    np_img = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("無法解析圖片，請確認格式與內容")

    # 處理模式
    if mode == 'grayscale':  # 將彩色圖像 img 轉換為灰度圖像
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif mode == 'resize':  # 將圖像 img 調整大小為 200x200 像素
        img = cv2.resize(img, (200, 200))
    elif mode == 'edge':  # 圖像進行 Canny 邊緣檢測，檢測的閾值分別設定為 100 和 200
        img = cv2.Canny(img, 100, 200)
    elif mode == 'blur':  #  # 模糊化圖片
        img = cv2.GaussianBlur(img, (15, 15), 0)
    elif mode == 'sharpen':  # 銳化圖片
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        img = cv2.filter2D(img, -1, kernel)

    elif mode == 'rotate':  # 圖片旋轉（例如 90 度）
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    elif mode == 'flip_horizontal':  # 左右翻轉
        img = cv2.flip(img, 1)

    elif mode == 'flip_vertical':  # 上下翻轉
        img = cv2.flip(img, 0)

    elif mode == 'invert_colors':  # 顏色反轉
        img = cv2.bitwise_not(img)

    else:
        raise ValueError(f"不支援的處理模式：{mode}")

    # 根據上傳副檔名決定輸出格式
    ext = file.filename.rsplit('.', 1)[-1].lower() if hasattr(file, 'filename') else 'jpg'
    fmt = 'png' if ext in ['png', 'gif'] else 'jpg'
    success, img_encoded = cv2.imencode(f'.{fmt}', img)
    if not success:
        raise ValueError("影像編碼失敗")
    return io.BytesIO(img_encoded.tobytes())
