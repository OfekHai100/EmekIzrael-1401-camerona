import imutils
import sys
import os
import cv2

"""
excpects:
cutVid.py input_file output_folder
"""
def main():
    data = sys.argv[1:]
    print(data)
    input_file = data[0]
    dst_path = data[1]
    i = len(os.listdir(dst_path)) + 1
    cap = cv2.VideoCapture(input_file)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        for _ in range(0,5):
            _,_ = cap.read()
        #frame = imutils.rotate(frame, 90)
        output_path = os.path.join(dst_path, str(i)+'.jpg')
        cv2.imwrite(output_path, frame)
        i+=1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
	main()