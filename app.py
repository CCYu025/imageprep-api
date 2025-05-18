# 余振中 (Yu Chen Chung)
from flask import Flask, request, send_file, jsonify
# from flask_cors import CORS
from image_utils import process_image  # ← ✅ 使用模組


app = Flask(__name__)
#CORS(app)  # 跨網域支援，前端才能呼叫 API
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 最多 5MB

@app.route('/process-image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify(error='缺少圖片檔案'), 400

    file = request.files['file']
    mode = request.form.get('mode', 'grayscale')

    try:
        buf = process_image(file, mode)
    except ValueError as ve:
        return jsonify(error=str(ve)), 400

    buf.seek(0)
    # 回傳時根據 buffer 格式自動決定 mimetype
    mimetype = 'image/png' if file.filename.lower().endswith(('png', 'gif')) else 'image/jpeg'
    return send_file(buf, mimetype=mimetype)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # 提供本地測試用設定


