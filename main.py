import cv2
import pytesseract

# initialize the video capture object
cap = cv2.VideoCapture(1)

# set the tesseract OCR engine path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# loop over each frame from the video stream
while True:
    # grab the current frame
    ret, frame = cap.read()

    # convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # apply OTSU thresholding to the grayscale image
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # pass the thresholded image to Tesseract OCR to extract the text
    text = pytesseract.image_to_string(thresh)

    # display the extracted text on the frame
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # show the frame to the screen
    cv2.imshow("Frame", frame)

    # check if the 'q' key was pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# release the video capture object
cap.release()

# close all windows
cv2.destroyAllWindows()