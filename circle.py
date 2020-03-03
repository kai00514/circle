import numpy
import os 
import cv2
import sys
import glob

def usage():
    print(sys.argv[0],"<input_dir > <output_dir>")





if __name__ == "__main__":

	if len(sys.argv) < 3:
		usage()
		quit(-1)
	else:
		f = sys.argv[1]
		output_path = sys.argv[2]
		print(output_path)
	if not os.path.exists(output_path):
		os.mkdir(output_path)
	else:
		print("output_path already exist")


	j = os.path.join(f,"*.png")
	fname = glob.glob(j)


	for f2 in fname:
		print(f2)
		img = cv2.imread(f2)
		h = img.shape[0]
		w = img.shape[1]
		#center = h // 2, w //2 
		center = img[0:2] + img[2:4] / 2
		radius = 1

		color = (0,0,154)

		basename = os.path.basename(f2)
		joing_out = os.path.join(output_path,basename)

		out = glob.glob(joing_out)
		print(type(center))
		print(type(radius))
		#print(type(color))
		#cv2.circle(img, center, radius, color, thickness=1, lineType=cv2.LINE_8, shift=0)
		cv2.circle(img, center, radius, (255, 255, 255), thickness=-1)
		cv2.imwrite(out,img)
	#	cv2.circle(path_jo, (190, 35), 15, (255, 255, 255), thickness=-1)
	#	cv2.circle(path_jo, (240, 35), 20, (0, 0, 0), thickness=3, lineType=cv2.LINE_AA)
