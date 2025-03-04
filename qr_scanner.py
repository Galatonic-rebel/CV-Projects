#Importing libraries
import cv2
import time
from pyzbar.pyzbar import decode

#Initializes the video cam using the default cam
cap = cv2.VideoCapture(0)

#Getting frame from cam
while True:
  ret, frame= cap.read()
  if not ret:
    print("not working")
    break

  #Convert frame to grayscale to improve decoding accuracy
  gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  #Detect and decode QR code
  qr_codes = decode(gray_frame)

  for qr in qr_codes:
    qr_data = qr.data.decode('utf-8') #Get the decoded text
    qr_rect = qr.rect #Get QR bounding box

    #Draw rectangle around the QR Code
    #arg -> image, start_point, end_point, color, thickness
    cv2.rectangle(frame,(qr_rect.left, qr_rect.top),
                  (qr_rect.left + qr_rect.width, qr_rect.top + qr_rect.height),
                  (0,255,0),3)
    #Display the decoded text on the frame
    cv2.putText(frame, qr_data, (qr_rect.left, qr_rect.top-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0),2)

    print("QR Code Detected:", qr_data)

  #Show output frame
  cv2.imshow("QR Code Scanner", frame)

  #Exit when 'q' is pressed
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break


cap.release()
cv2.destroyAllWindows()

