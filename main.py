import cv2
import numpy as np


CHAR_LIST = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
#print(len(CHAR_LIST))

img = cv2.imread('thuytiennn.jpg', 0)

col_num = 200
height, width = img.shape
cell_width = width / col_num
cell_height = cell_width*2
row_num = int(height / cell_height)

print("So cot: ", row_num)


# print("Image: \n", img)
# print('Image_size: ', img.shape)
# cv2.imshow('Ngoc Son', img[0:300, :])
# cv2.waitKey(0)
output_file = open("image.txt", "w")

for i in range(row_num):
    for j in range(col_num):
        sub_image = img[int(i*cell_height): int((i+1)*cell_height), int(j*cell_width): int((j+1)*cell_width)]
        #cv2.imwrite("{}_{}.jpg".format(i, j), sub_image)
        #print("Cell {} {}: {}".format(i, j, np.mean(sub_image)))
        average_ = np.mean(sub_image)/255*len(CHAR_LIST)
        #print(CHAR_LIST[int(index)])
        index_ = int(average_)
        output_file.write(CHAR_LIST[index_])
    output_file.write("\n")
output_file.close()