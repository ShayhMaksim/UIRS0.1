
import numpy as np
from tkinter import *
from PIL import Image
import road
import cv2

#img=Image.open("C:\\Users\\Maksim\\PycharmProjects\\next.jpg")
#image=cv2.imread("C:\\Users\\Maksim\\PycharmProjects\\next.jpg")

#arr=np.asarray(img,int)
#width=img.size[0]
#height=img.size[1]
#(h,w)=image.shape[:2]
#center=(w/2,h/2)



#M=cv2.getRotationMatrix2D(center,45,1)
#rotated=cv2.warpAffine(image,M,(w,h))
#cv2.imshow("rotated image",rotated)
#cv2.waitKey(0)

#print(arr)

#arr.shape
#print(arr.shape)

#arr1=np.array((30,30,4),int)
#print(arr1.shape)



root=Tk()
#canvas = Canvas(root, width=555, height=555)
#canvas.pack()

PictureArr = []
A=np.zeros((500,500))

for i in range(500):
    PictureArr.append([])
    for j in range(500):
            if 10000 < pow(i-250, 2)+pow(j-250, 2) < 40000:
                PictureArr[i].append(255)
            else:
                PictureArr[i].append(0)

for i in range(500):
    for j in range(500):
            if 10000 < pow(i-250, 2)+pow(j-250, 2) < 40000:
                A[i,j]=255
            else:
                A[i,j]=0

#for i in range(500):
 #   for j in range(500):
  #      if 10000 < pow(i - 250, 2) + pow(j - 250, 2) < 40000:
   #         canvas.create_rectangle(i, j, i, j, outline="#ffffff", fill="#ffffff")
    #    else:
     #       canvas.create_rectangle(i, j, i, j)


Data=np.array(PictureArr)



img=Image.fromarray(Data,'RGB')
img.save('my.jpg')
img.show()

image=cv2.imread('my.jpg')


(h,w)=image.shape[:2]
center=(w/2,h/2)

M=cv2.getRotationMatrix2D(center,45,1)
rotated=cv2.warpAffine(image,M,(w,h))
cv2.imshow("rotated image",rotated)
cv2.waitKey(0)



#for i in range(width):
#for j in range(height):
 #           if (arr[j,i,1]==255):
 #              canvas.create_rectangle(i, j, i, j,outline="#ffffff", fill="#ffffff")
  #          else:
    #            canvas.create_rectangle(i, j, i, j)

#canvas.mainloop()