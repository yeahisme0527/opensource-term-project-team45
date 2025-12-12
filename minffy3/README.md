## 이민서의 오픈소스 프로젝트 - OpenCV 기반 QR 코드 생성 및 인식 프로그램

▷ 프로젝트 개요

이 프로젝트는 문자열 데이터를 QR 코드 이미지로 생성하고,
생성된 QR 코드 이미지를 다시 인식하여 원본 문자열을 복원하는
파이썬 기반 QR 코드 생성 및 인식 프로그램입니다.

OpenCV와 qrcode 라이브러리를 활용하여 QR 코드 생성 및 디코딩 기능을
간단하게 구현하였습니다.

항목 | 내용
--- | ---
사용 라이브러리 | qrcode, opencv-python, pillow
입력 | 문자열 (텍스트 또는 URL)
출력 | QR 코드 이미지(my_qr.png) 및 디코딩된 문자열
실행 환경 | Python 3.x

▷ 기능

✔ 문자열을 QR 코드 이미지로 생성
✔ 생성된 QR 코드 파일 저장
✔ OpenCV를 이용한 QR 코드 인식
✔ QR 코드에 저장된 원본 문자열 출력

▷ 코드 동작

[QR 코드 생성 - generate_qr.py]

    import qrcode
    import os

    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "my_qr.png")

    data = "https://github.com/yeahisme0527"
    img = qrcode.make(data)
    img.save(output_path)

    print("QR 코드 생성 완료:", output_path)

[QR 코드 인식 - read_qr.py]

    import cv2
    import os

    base_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(base_dir, "my_qr.png")

    detector = cv2.QRCodeDetector()
    img = cv2.imread(image_path)

    if img is None:
        print("QR 이미지 파일을 찾을 수 없습니다.")
    else:
        data, _, _ = detector.detectAndDecode(img)
        print("디코딩 결과:", data)

▷ 실행 방법

1. 필요한 라이브러리 설치
   pip install qrcode opencv-python pillow

2. 파일이 위치한 폴더로 이동
   cd minffy3

3. QR 코드 생성
   python generate_qr.py

4. QR 코드 인식
   python read_qr.py

▷ 개인 프로젝트 주제

이민서 : OpenCV 기반 QR 코드 생성 및 인식 프로그램

▷ 참고 자료
- https://pypi.org/project/qrcode/
- https://docs.opencv.org/

- https://pypi.org/project/qrcode/
- https://docs.opencv.org/
