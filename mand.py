from PIL import ImageTk
import PIL.Image
from tkinter import *
import time
import random
# print(data)
# data.save("mand.png")
# data.show()


win = Tk()
win.geometry("750x550")
blank = PIL.Image.effect_mandelbrot((500,500), (0,0,1,1), 100)
tkimage= ImageTk.PhotoImage(blank)
label=Label(win,image=tkimage)
label.pack()


def draw(start, stop, step):
	for x in range(start, stop, step):
		d = x + 1
		data = PIL.Image.effect_mandelbrot((500,500), (0,0,.5,.5), d)
		print(data)
		tkimage= ImageTk.PhotoImage(data)
		label.configure(image=tkimage)
		label.image = tkimage
		win.update_idletasks()
		win.update()
		# time.sleep(.2)
while 1:
	draw(1,random.randrange(100),1)
	draw(random.randrange(100),1,-1)
# win.mainloop()