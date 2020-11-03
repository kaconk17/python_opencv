import cv2
from pyzbar import pyzbar

cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()
    #image = cv2.resize(image, (640, 480))
    imgs = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(imgs)

    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        if barcodeData == 'kanaya':
            print('hasil OK')

    cv2.imshow("barcode", image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

print("Cleaning...")
cap.release()
cv2.destroyAllWindows()
