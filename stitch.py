from panorama import Stitcher
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True)
ap.add_argument("-s", "--second", required=True)
args = vars(ap.parse_args())

imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])
imageA = imutils.resize(imageA, width=600)
imageB = imutils.resize(imageB, width=600)

stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

cv2.imshow("ImageA", imageA)
cv2.imshow("ImageB", imageB)
cv2.imshow("Keypoints Matches", vis)
cv2.imshow("result", result)
cv2.waitKey(0)
