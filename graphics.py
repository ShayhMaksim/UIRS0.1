from tkinter import *


import matplotlib
from car import car
from road import road
from NeuralNetwork import NeuralNetwork
import numpy
import math
import random

#процедура выреза из матрицы дороги участка 51х51
def slice(x, y, angle) :
    SliceArr = []
    # вырез, если машина смотрит направо
    if angle <= math.pi/4 or  angle >= 7*math.pi/4:
        for j in range(51) :
            #SliceArr.append([])
            for i in range(51):
                SliceArr.append((road1.PictureArr[x-25+i][y-25+j])*1./255)
    # если машина смотрит вниз
    elif 5*math.pi/4 < angle <= 7*math.pi/4:
        for i in range(51):
            # SliceArr.append([])
            for j in range(51):
                SliceArr.append((road1.PictureArr[x + 25 - i][y - 25 + j])*1./255) #0.99/255+0.01
    # если машина смотрит влево
    elif 3*math.pi/4 < angle <= 5*math.pi/4:
        for j in range(51):
            # SliceArr.append([])
            for i in range(51):
                SliceArr.append((road1.PictureArr[x + 25 - i][y + 25 - j])*1./255)
    #если машина смотрит вверх
    elif math.pi/4 < angle <= 3*math.pi/4:
        for i in range(51):
            # SliceArr.append([])
            for j in range(51):
                SliceArr.append((road1.PictureArr[x - 25 + i][y + 25 - j])*1./255)

    return SliceArr
#обучение машины
def trainCar():
    #итерация цикла - одна машина
    for i in range(4):
        isLive = True
        newCar.respawn(250, 100, 0)
      #  t = 0
     #   print("111")
        X = [] # массивы координат машинки для обучения на n последних снимков
        Y = [] #
        Angle = []
        while isLive:
          #  t += 1
            #print(t)
            #Arr = []
            #i = 1
            X.append(newCar.x)
            Y.append(newCar.y)
            Angle.append(newCar.angle)
            Arr = slice(round(newCar.x), round(newCar.y), newCar.angle)
            outputs = n.query(Arr)
            label = numpy.argmax(outputs)
            #label = int(input())
            print(label)
            if label == 0:
                newCar.turnleft()
            elif label == 1:
                newCar.turnright()
            updatecar()
            #sliceCheck()
            print(newCar.angle/(2*math.pi)*360)
            canvas.update()
            if not 10000 < pow(newCar.x - 250, 2) + pow(newCar.y - 250, 2) < 40000:
                isLive = False
            if isLive :
                result = label
            elif pow(newCar.x - 250, 2) + pow(newCar.y - 250, 2) > 40000:
                result = 1
            elif 10000 > pow(newCar.x - 250, 2) + pow(newCar.y - 250, 2):
                result = 0
            #else:
               # result = random.randrange(1,2,1)
        #Arr1 = slice(round(X[len(X)-2]),round(Y[len(Y)-2]), Angle[len(Angle)-2])
        #Arr2 = slice(round(X[len(X) - 3]), round(Y[len(Y) - 3]), Angle[len(Angle)-3])
        #Arr3 = slice(round(X[len(X) - 4]), round(Y[len(Y) - 4]), Angle[len(Angle)-4])
        #Arr4 = slice(round(X[len(X) - 5]), round(Y[len(Y) - 5]), Angle[len(Angle)-5])
        #Arr5 = slice(round(X[len(X) - 6]), round(Y[len(Y) - 6]), Angle[len(Angle)-6])
        #Arr6 = slice(round(X[len(X) - 7]), round(Y[len(Y) - 6]), Angle[len(Angle) - 7])
        #Arr7 = slice(round(X[len(X) - 8]), round(Y[len(Y) - 6]), Angle[len(Angle) - 8])
        #Arr8 = slice(round(X[len(X) - 9]), round(Y[len(Y) - 6]), Angle[len(Angle) - 9])
        #Arr9 = slice(round(X[len(X) - 10]), round(Y[len(Y) - 6]), Angle[len(Angle) - 10])
        print('result')
        print(result)
        n.train(Arr, result)
        #n.train(Arr1, result)
        #n.train(Arr2, result)
        #n.train(Arr3, result)
        #n.train(Arr4, result)
        #n.train(Arr5, result)
        #n.train(Arr6, result)
        #n.train(Arr7, result)
        #n.train(Arr8, result)
        #n.train(Arr9, result)
      #  print("222")


def sliceCheck():
    Ar = slice(round(newCar.x), round(newCar.y), newCar.angle)
    for j in range(51):
        for i in range(51):
            if Ar[i+j*51] > 100:
                canvas.create_rectangle(500+i, 500+j, 500+i, 500+j, outline="#f50", fill="#f50")
            else:
                canvas.create_rectangle(500 + i, 500 + j, 500 + i, 500 + j, outline="#ffffff", fill="#ffffff")

def updatecar():
    canvas.create_rectangle(newCar.x-5, newCar.y-5, newCar.x+5, newCar.y+5, outline="#ffffff", fill="#ffffff")
    newCar.move(0.1)
    canvas.create_rectangle(newCar.x - 5, newCar.y - 5, newCar.x + 5, newCar.y + 5, outline="#f50", fill="#f50")

root = Tk()
canvas = Canvas(root, width=700, height=700)
canvas.pack()

newCar = car(250, 100, 50, 0)
road1 = road()

input_nodes = 2601
hidden_nodes = 900
output_nodes = 2
learning_rate = 0.1
n = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)



#for k in range(51):
 #   print(Arr[k:])

for i in range(500):
    for j in range(500):
        if 10000 < pow(i - 250, 2) + pow(j - 250, 2) < 40000:
            canvas.create_rectangle(i, j, i, j, outline="#ffffff", fill="#ffffff")
        else:
            canvas.create_rectangle(i, j, i, j)



trainCar()

# label to test
label = 0
# create the output signals for this label
targets = numpy.zeros(output_nodes) + 0.01
# all_values[0] is the target label for this record
targets[label] = 0.99
print(targets)
# get image data
image_data = n.backquery(targets)
# plot image data
matplotlib.pyplot.imshow(image_data.reshape(51, 51), cmap='Greys', interpolation='None')


canvas.mainloop()
