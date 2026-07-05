import qrcode

text = input("Enter text or URL: ")
img = qrcode.make(text)
img.save("qrcode.png")

print("QR Code saved as qrcode.png")
