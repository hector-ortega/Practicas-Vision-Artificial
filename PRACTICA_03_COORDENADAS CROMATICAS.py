import cv2
import numpy as np
imagen = cv2.imread("mano.jpg")
imagenc = imagen.copy()
imageno1 = imagen.copy()
imageno2 = imagen.copy()
# imageno3 = cv2.imread("mano_o3.png")

m,n,c = imagen.shape



imagen = imagen.astype(np.float32)
#imagenc = imagenc.astype(np.float32)
imageno1 = imageno1.astype(np.float32)
imageno2 = imageno2.astype(np.float32)
# imageno3 = imageno3.astype(np.float32)

def clasificador (imagen):
    m,n,c = imagen.shape
    imagen_b=np.zeros((m,n))
    for x in range (m):
        for y in range (n):
            if 50<imagen[x,y,0]<232 and imagen[x,y,1]<232 and imagen[x,y,2]<232:
                imagen_b[x,y]=255
                    
    #cv2.imwrite("imagen_b1.jpg",imagen_b)
    cv2.imshow("mano binaria",imagen_b)
    cv2.waitKey(0)
    return imagen_b

def cromatico(imagenc,s,crom):
    imagen = cv2.imread(s)
    m,n,c = imagen.shape
    imagenc = imagen.copy()
    imagenc = imagenc.astype(np.float32)
    imagen = imagen.astype(np.float32)
    for x in range(m):
        for y in range (n):
            imagenc[x,y,0] = imagen[x,y,0]/(imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2])
            imagenc[x,y,1] = imagen[x,y,1]/(imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2])
            imagenc[x,y,2] = imagen[x,y,2]/(imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2])

    cv2.imshow(crom,imagenc)
    cv2.waitKey(0)
    imagenc = cv2.normalize(imagenc, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    cv2.imwrite(crom+".png",imagenc)
    return imagenc

#-----------SE CREAN LAS IMAGENES CON DIFERENTE OPACIDAD-----------
imagen = cv2.imread("mano.jpg")
cv2.imshow("mano OG",imagen)
cv2.waitKey(0)#espera a aque se presione la X
cv2.destroyAllWindows() #se cierra la ventana al presionar la X

imageno1 = imagen*0.7 #se multiplica por un fator para modificar su nitidez o exposicion
imageno1 = imageno1.astype(np.uint8) #Al multiplicar por el numero flotante se convierte en flotante
cv2.imshow("mano obscura 1",imageno1) #Se muestra la nueva imagen oscura
cv2.waitKey(0)#espera a aque se presione la X
cv2.destroyAllWindows() #se cierra la ventana al presionar la X
cv2.imwrite("mano_o1.png",imageno1)

imageno2 = imagen*0.3
imageno2 = imageno2.astype(np.uint8)
cv2.imshow("mano obscura 2",imageno2) #Se muestra la nueva imagen oscura
cv2.waitKey(0)#espera a aque se presione la X
cv2.destroyAllWindows() #se cierra la ventana al presionar la X
cv2.imwrite("mano_o2.png",imageno2)


#imagen = cv2.imread("mano.jpg") #se guarda la imagen en la variable imagen

imagenc = cromatico(imagenc,"mano.jpg","imagen_cromatica01")
imageno1 = cromatico(imageno1,"mano_o1.png","imagen_cromatica02")
imageno2 = cromatico(imageno2, "mano_o2.png","imagen_cromatica03")

imagenc = cv2.imread("imagen_cromatica01.png")
imageno1 = cv2.imread("imagen_cromatica02.png")
imageno2 = cv2.imread("imagen_cromatica03.png")

imagenc = clasificador(imagenc)
imageno1 = clasificador(imageno1)
imageno2 = clasificador(imageno2)

#espera a aque se presione la X
cv2.destroyAllWindows()



#-----------SE CREAN LAS IMAGENES CON DIFERENTE OPACIDAD-----------

# imageno1 = imagen*0.3 #se multiplica por un fator para modificar su nitidez o exposicion
# imageno1 = imageno1.astype(np.uint8) #Al multiplicar por el numero flotante se convierte en flotante
# cv2.imshow("mano obscura",imageno1) #Se muestra la nueva imagen oscura
# cv2.waitKey(0)#espera a aque se presione la X
# cv2.destroyAllWindows() #se cierra la ventana al presionar la X
# cv2.imwrite("mano_o1.png",imageno1)

# imageno2 = imagen*0.5
# imageno2 = imageno2.astype(np.uint8)
# cv2.imshow("mano obscura 2",imageno2) #Se muestra la nueva imagen oscura
# cv2.waitKey(0)#espera a aque se presione la X
# cv2.destroyAllWindows() #se cierra la ventana al presionar la X
# cv2.imwrite("mano_o2.png",imageno2)

# imageno3 = imagen*0.8
# imageno3 = imageno3.astype(np.uint8)
# cv2.imshow("mano obscura 3",imageno3) #Se muestra la nueva imagen oscura
# cv2.waitKey(0)#espera a aque se presione la X
# cv2.destroyAllWindows() #se cierra la ventana al presionar la X
# cv2.imwrite("mano_o3.png",imageno3)

# cv2.waitKey(0)#espera a aque se presione la X
# cv2.destroyAllWindows() #se cierra la ventana al presionar la X