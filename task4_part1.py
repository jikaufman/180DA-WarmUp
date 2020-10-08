# Resources used:
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#converting-colorspaces
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html#contour-features
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#thresholding
# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html

import numpy as np
import cv2


def main():
	cap = cv2.VideoCapture(0)

	while(True):
	    # Capture frame-by-frame
	    _, frame = cap.read()

	    # Our operations on the frame come here
	    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	    lower_blue = np.array([100,50,50])
	    upper_blue = np.array([130,255,255])

	    mask = cv2.inRange(hsv, lower_blue, upper_blue)

	    contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	    if (len(contours)):
	    	area = max(contours, key=cv2.contourArea)
	    	rect = cv2.minAreaRect(area)
	    	box = cv2.boxPoints(rect)
	    	box = [np.int0(box)]
	    	frame = cv2.drawContours(frame, box, 0, (0,0,255), 2)

	    # Display the resulting frame
	    cv2.imshow('frame',frame)
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break

	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()