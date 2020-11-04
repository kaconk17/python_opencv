import pyqrcode
from PIL import Image
import json


print('==================================================================')
print('==================Aplikasi generate QR Code.======================')
print('==================================================================')
print('Masukkan Nama')
nama = input('Nama :')
nik = input('nik :')

x = {
    "appid":"017",
    "nama":nama,
    "nik":nik,
    "mode":"IN"
}

y = {
    "appid":"017",
    "nama":nama,
    "nik":nik,
    "mode":"OUT"
}

xin = json.dumps(x)
xout = json.dumps(y)


def generateCode(data):
    detail = json.loads(data)
    img = pyqrcode.create(data)
    img.png('qrcode/generated/'+detail['nik']+detail["mode"]+'.png', scale=10)
    im = Image.open('qrcode/generated/'+detail['nik']+detail["mode"]+'.png')
    im = im.convert("RGBA")
    if detail["mode"] == "IN":
        logo = Image.open('qrcode/in.png')
    else:
        logo = Image.open('qrcode/out.png')

    width, height = im.size
    logo_size = 100

    xmin = ymin = int((width / 2)-(logo_size / 2))
    xmax = ymax = int((width / 2)+(logo_size / 2))

    logo = logo.resize((xmax - xmin, ymax - ymin))
    im.paste(logo, (xmin,ymin,xmax,ymax))
    im.save('qrcode/generated/'+detail['nik']+detail["mode"]+'.png')
    im.show()

generateCode(xin)
generateCode(xout)
