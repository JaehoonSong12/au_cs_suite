from flask import Flask, request, jsonify
import cv2
import numpy as np
import base64

app = Flask(__name__)

def apply_cartoon_filter(image):
    # 1. Apply bilateral filter to smooth colors
    color = cv2.bilateralFilter(image, 9, 300, 300)

    # 2. Convert to grayscale and apply median blur
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.medianBlur(gray, 7)

    # 3. Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 10)

    # 4. Combine edges with color image
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

@app.route("/apply-filter", methods=["POST"])
def apply_filter():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    npimg = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    # Apply the cartoon filter
    filtered_image = apply_cartoon_filter(image)

    # Convert to base64
    _, buffer = cv2.imencode(".png", filtered_image)
    filtered_image_base64 = base64.b64encode(buffer).decode("utf-8")

    return jsonify({"filtered_image": filtered_image_base64})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
