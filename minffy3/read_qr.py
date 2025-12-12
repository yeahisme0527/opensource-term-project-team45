import cv2
import os

# 이 파일(read_qr.py)이 있는 폴더 경로
base_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_dir, "my_qr.png")

detector = cv2.QRCodeDetector()
img = cv2.imread(image_path)

if img is None:
    print("QR 이미지 파일을 찾을 수 없습니다.")
else:
    data, _, _ = detector.detectAndDecode(img)
    print("디코딩 결과:", data)
