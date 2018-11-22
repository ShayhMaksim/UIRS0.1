from road import road
import matplotlib.pyplot
import tkinter

road1 = road();

matplotlib.pyplot.imshow(road1.PictureArr, cmap='Greys', interpolation='None')
#for number in range(500) :
#    print(road1.PictureArr[number:])
