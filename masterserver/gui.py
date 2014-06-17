
import Tkinter as tk
from Tkinter import *
from bluetooth import *
import tkMessageBox
import random

canvas_width = 700
canvas_height = 700

x = 10
y = 10

#Listen to bluetooth connection boolean
listen = 0;

server_sock=BluetoothSocket(RFCOMM)
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "SampleServer",
                    service_id = uuid,
                    service_classes = [ uuid, SERIAL_PORT_CLASS ],
                    profiles = [ SERIAL_PORT_PROFILE ],
#                   protocols = [ OBEX_UUID ] 
                    )



def listenBluetooth():
    try:
        data = client_sock.recv(1024)
        if len(data) == 0: pass
        print("received [%s]" % data)
    except IOError:
        pass

def handler():
	if tkMessageBox.askokcancel("Quit?", "Are you sure you want to quit?"):
		root.quit()

def connect():
    print "Waiting for connection"
    client_sock, client_info = server_sock.accept()
    print("Accepted connection from ", client_info)
    listen = 1;     

def draw(self,x,y,size):
    	drawQR(self,x,y,size)

def drawQR(self,x,y,size):
		dsize = size/4
		nextx = x
		nexty = y
		for i in range(4):
			nextx = nextx+dsize
			for j in range(4):
				if(random.randint(0,1)==1):
					color ="black"
				else:
					color="white"
				nexty = nexty+dsize
		 		figure=self.canvas.create_rectangle(nextx,nexty,nextx+dsize,nexty+dsize, fill=color)
		 	nexty = y

def drawRobot(self,x,y,size,direction,xco,yco):
	x *= xco
	y *= yco
	x += size/8
	y+= size/8
	figure=self.canvas.create_rectangle(x,y,x+size/4,y+size/4, fill="yellow")




class Gui():
    def __init__(self, root):
        self.root=root
        self.entry = tk.Entry(root)
        stvar=tk.StringVar()
        stvar.set("one")

        self.canvas=tk.Canvas(root, width=canvas_width, height=canvas_height, background='grey')
        self.canvas.grid(row=0,column=1,padx=10)

        frame = Frame(self.root)
        frame.grid(row=0,column=0, sticky="n")
        label1=Label(frame, text="Grid size").grid(row=0,column=0, sticky="nw")
        label2=Label(frame, text="X").grid(row=1,column=0, sticky="w")
        # self.option.grid(row=0,column=1,sticky="nwe")
        e = Entry(root).grid(row = 1,column = 1,sticky = E+ W)
        e.get(0, "a default value")
        Button1=Button(frame,text="Connect",command=connect).grid(row = 3,column = 1, sticky = "we")

        for i in range(x):
        	for j in range(y):
        		dx = canvas_width/x
        		dy = canvas_height/y
        		draw(self,dx*i,dy*j,dx/2)
        # Grid.columnconfigure(self.root,1,weight=1, size=200)
        drawRobot(self,dx,dy,50,1,1,2)
        drawRobot(self,dx,dy,50,1,5,4)



if __name__== '__main__':
    root=tk.Tk()
    root.resizable(width=FALSE, height=FALSE)
    gui=Gui(root)
    root.protocol("WM_DELETE_WINDOW", handler)
    root.mainloop()
    while True:
        if (listen):
            listenBluetooth()
        
    print("disconnected");

    client_sock.close()
    server_sock.close()
    print("all done")




