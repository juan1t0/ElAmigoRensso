import cv2
import numpy as np
from matplotlib import pyplot as plt

imagen = 0
matrix = 0
#cont =0

##################################################################
########################## FUNCTIONS #############################
##################################################################

def checkEdge ( edges ):
 #   print('chek')
    equis = []
    yes = []
    for i,j in edges:
        equis.append(str(i))
        yes.append(str(j))
    equis.sort(key=int)
    yes.sort(key=int)

    for i in range (len(equis)-1):
        aux = equis.count(equis[i])
        if(aux % 2 == 0):
            continue
        else :
            return False

    return True
        
'''    global matrix
    maxx = 0
    maxy = 0
    minx = 10000
    miny = 10000
    for i,j in edges:
        if (maxx <= i):
            maxx = i
        if (maxy <= j):
            maxy = j
        if (minx >= i):
            minx = i
        if (miny >= y):
            miny = j
    xx = maxx - minx
    yy = maxy - miny
    my_x =0
    my_y =0
    matrix = np.zeros((yy,xx),dtype = bool)
    for i,j in edges:
        matrix[i-xx][j-yy] = True
        my_x = i-xx
        my_y = j-yy

    aux = False
    for i in range ( xx):
        for j in range (yy):
            if (matrix[i][j] == True):
                
'''        

        
def Isdentro(x,y):
    global imagen

#    temp = imagen
  #  print(str(x),' ',str(y))
    if(imagen[x][y] == 255):
        return False
    
    queue = []
    cont = 0
    queue.append((x,y))
    edge = []
    while(len(queue) != 0):
        i,j = queue.pop()
#        print(str(i),' ',str(j),' white')
        try :
            if(imagen[i][j] == 255):
 #               print('aqui')
                edge.append((i,j))
                continue
            if(imagen[i][j] == 0):
                imagen[i][j] = 10
                queue.append((i-1,j))
                queue.append((i+1,j))
                queue.append((i,j-1))
                queue.append((i,j+1))
        except:
            cont = cont+1
  #          print('err')
    return checkEdge(edge)


def TruePaint ( x ,y):
#    print('pint')
    global imagen
    global matrix
 #   global cont
#    print(x,' , ',y)
    cont =0
    queue = []
    queue.append((x,y))
    while(len(queue) != 0):
        i,j = queue.pop()
        try :
            if(imagen[i][j] == 255):
                continue
            if(imagen[i][j] == 0):
                imagen[i][j] = 125
#                print(str(i),' ',str(j),' white')
                queue.append((i-1,j))
                queue.append((i+1,j))
                queue.append((i,j-1))
                queue.append((i,j+1))
        except:
            cont = cont+1

#    print('hecho',str(cont))
        
def pintar():
    global imagen
    global matrix
    hei , wei = imagen.shape
    punto = 0
    strr = ''
#    for i in range(hei):
 #       for j in range(wei):
  #          if(Isdentro(i,j)):
   #             TruePaint(i,j)
            
##    TruePaint (150,150)
    TruePaint (60,60)
#    return rsp


##################################################################
############################ MAIN ################################
##################################################################


#img = cv2.imread('prueba.png',0)
imagen = cv2.Canny(cv2.imread('batidibujo.jpg'),500,00)
#paintin = pintar(Contornos)


plt.subplot(121),plt.imshow(imagen,cmap = 'gray')
plt.title('Contornos de la imagen'), plt.xticks([]), plt.yticks([])
pintar()
plt.subplot(122),plt.imshow(imagen,cmap = 'gray')
plt.title('Final Imagen'), plt.xticks([]), plt.yticks([])


plt.show()
