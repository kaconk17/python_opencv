from pyzbar import pyzbar
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--mage", required=True, help="Alamat file gambar")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

barcodes = pyzbar.decode(image)

for barcode in barcodes:
    (x,y,w,h) = barcodes.rect
    cv2.rectangle(image, (x,y),(x+w,y+h),(0,0,255),2)
    barcodeData = barcode.data.decode("utf-8")
    barcodeType = barcode.type

    text = "{} ({})".format(barcodeData, barcodeType)
    cv2.putText(image, text, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2)

    print("[INFO] found {} barcode : {}".format(barcodeType, barcodeData))

cv2.imshow("hasil", image)
cv2.waitKey(0)