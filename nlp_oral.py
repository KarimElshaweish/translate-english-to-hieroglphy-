#!/usr/bin/env python
from pylab import *
from matplotlib.pyplot import imshow
from PIL import ImageChops
from tkinter import *
hiero_dict=dict()
hiero_dict['A']='/home/karim/Desktop/hiero/A.png'
hiero_dict['B']='/home/karim/Desktop/hiero/B.png'
hiero_dict['C']='/home/karim/Desktop/hiero/C.png'
hiero_dict['D']='/home/karim/Desktop/hiero/D.png'
hiero_dict['E']='/home/karim/Desktop/hiero/E.png'
hiero_dict['F']='/home/karim/Desktop/hiero/F.png'
hiero_dict['G']='/home/karim/Desktop/hiero/G.png'
hiero_dict['H']='/home/karim/Desktop/hiero/H.png'
hiero_dict['I']='/home/karim/Desktop/hiero/I.png'
hiero_dict['J']='/home/karim/Desktop/hiero/J.png'
hiero_dict['K']='/home/karim/Desktop/hiero/K.png'
hiero_dict['L']='/home/karim/Desktop/hiero/L.png'
hiero_dict['M']='/home/karim/Desktop/hiero/M.png'
hiero_dict['N']='/home/karim/Desktop/hiero/N.png'
hiero_dict['O']='/home/karim/Desktop/hiero/O.png'
hiero_dict['P']='/home/karim/Desktop/hiero/P.png'
hiero_dict['Q']='/homse/karim/Desktop/hiero/Q.png'
hiero_dict['R']='/home/karim/Desktop/hiero/R.png'
hiero_dict['S']='/home/karim/Desktop/hiero/S.png'
hiero_dict['T']='/home/karim/Desktop/hiero/T.png'
hiero_dict['U']='/home/karim/Desktop/hiero/U.png'
hiero_dict['V']='/home/karim/Desktop/hiero/V.png'
hiero_dict['W']='/home/karim/Desktop/hiero/W.png'
hiero_dict['X']='/home/karim/Desktop/hiero/X.png'
hiero_dict['Y']='/home/karim/Desktop/hiero/Y.png'
hiero_dict['Z']='/home/karim/Desktop/hiero/Z.png'
hiero_dict['sun']='/home/karim/Desktop/hiero/sun.png'
hiero_dict['home']='/home/karim/Destop/hiero/home.png'
hiero_dict['tomb']='/home/karim/Desktop/hiero/tomb.png'
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
word=(pytesseract.image_to_string(Image.open('/home/karim/Desktop/test.jpg')))
word=word.split(' ')
print(word)
#gui
root=Tk()
#word='karim'
#word=word[0]
word=word[2]
see=word
photo=[]
for i in range(100):
    photo.append(0)
if(word is 'sun' or word is 'tomb' or word is 'home'):
    pi=PhotoImage(file=hiero_dict[word])
    label=Label(root,image=pi)
    label.pack()
else:
    for w in range(len(word)):
        photo[w] = PhotoImage(file=hiero_dict[word[w].upper()])
        label=Label(root, image=photo[w])
        label.pack()
label=Label(root,text=see)
label.pack()
root.mainloop()