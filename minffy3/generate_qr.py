import qrcode

data = "https://github.com/yeahisme0527"
img = qrcode.make(data)
img.save("my_qr.png")

print("QR 코드 생성 완료!")
