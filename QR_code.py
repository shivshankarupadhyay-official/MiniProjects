import qrcode

text = input("ENTER TEXT or URL: ")

qr = qrcode.make(text)

filename = "qrcode.png"

qr.save(filename)

print("QR code saved as", filename)