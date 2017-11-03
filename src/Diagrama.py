from Tkinter import *
from PIL import ImageTk, Image
import io

class Diagrama(Frame):

    """
    Constructor de la clase
    Crea el tablero 
    Se colocan los botones
    Se ponen las piezas que se pueden colocar en el tablero
    Se inicializan los eventos posibles
    """
    def __init__(self,parent):
        self.contador = 0
        self.im = None
        Frame.__init__(self,parent)
        self.pack(fill=BOTH,expand=True)
        self.creaTablero()
        self.creaBotones()
        self.cargaPiezas()
        self.acciones()


    """
    Crea un canvas para poder dibujar el tablero de ajedrez
    """    
    def creaTablero(self):
                
        self.col = 8
        self.ren = 8
        self.tam = 32
        self.color1 = "white"
        self.color2 = "black"
        self.piezas = {}

        ancho = self.col * self.tam
        alto = self.ren * self.tam

        self.var = self.canvas = Canvas(self,borderwidth=0,highlightthickness=0,width=300,height=300,background="bisque")
        self.canvas.place(x=10,y=10)
        self.canvas.bind("<Configure>",self.dibujaRect)

    """
    Dibuja los cuadrados del tablero 
    """    
    def dibujaRect(self,evento):
        x = int((evento.width-1)/self.col)
        y = int((evento.height-1)/self.ren)
        self.tam = min(x,y)
        #self.canvas.delete("square")
        color = self.color2
        for col in range(self.col):
            color = self.color1 if color == self.color2 else self.color2
            for ren in range(self.ren):
                x1 = (col * self.tam)
                y1 = (ren * self.tam)
                x2 = x1 + self.tam
                y2 = y1 + self.tam
                self.canvas.create_rectangle(x1,y1,x2,y2,outline="black",fill=color,tags="square")
                color = self.color1 if color == self.color2 else self.color2

    """
    Coloca las piezas que se pueden poner en el tablero
    """
    def cargaPiezas(self):
        label = Label(text="Escoge las piezas que quieras\n colocar en el diagrama")
        label.place(x=320,y=10)
        
        tam = (40,40)

        self.pb = self.canvasPeonB = Canvas(self,width=40,height=40)
        self.canvasPeonB.place(x=370,y=50)
        peonB = Image.open("piezas/peonB.jpg")
        peonB = peonB.resize(tam)
        imagePeonB = ImageTk.PhotoImage(peonB)
        self.canvasPeonB.image = imagePeonB
        self.canvasPeonB.create_image(imagePeonB.width()/2,imagePeonB.height()/2,ancho=CENTER,image=imagePeonB,tags="piezas")
        
        self.pw = self.canvasPeonW = Canvas(self,width=40,height=40)
        self.canvasPeonW.place(x=420,y=50)
        peonW = Image.open("piezas/peonW.jpg")
        peonW = peonW.resize(tam)
        imagePeonW = ImageTk.PhotoImage(peonW)
        self.canvasPeonW.image = imagePeonW
        self.canvasPeonW.create_image(imagePeonW.width()/2,imagePeonW.height()/2,ancho=CENTER,image=imagePeonW,tags="piezas")

        self.ab = self.canvasAlfilB = Canvas(self,width=40,height=40)
        self.canvasAlfilB.place(x=370,y=95)
        alfilB = Image.open("piezas/alfilB.jpg")
        alfilB = alfilB.resize(tam)
        imageAlfilB = ImageTk.PhotoImage(alfilB)
        self.canvasAlfilB.image = imageAlfilB
        self.canvasAlfilB.create_image(imageAlfilB.width()/2,imageAlfilB.height()/2,ancho=CENTER,image=imageAlfilB,tags="piezas")

        self.aw = self.canvasAlfilW = Canvas(self,width=40,height=40)
        self.canvasAlfilW.place(x=420,y=95)
        alfilW = Image.open("piezas/alfilW.jpg")
        alfilW = alfilW.resize(tam)
        imageAlfilW = ImageTk.PhotoImage(alfilW)
        self.canvasAlfilW.image = imageAlfilW
        self.canvasAlfilW.create_image(imageAlfilW.width()/2,imageAlfilW.height()/2,ancho=CENTER,image=imageAlfilW,tags="piezas")

        self.cb = self.canvasCaballoB = Canvas(self,width=40,height=40)
        self.canvasCaballoB.place(x=370,y=140)
        caballoB = Image.open("piezas/caballoB.jpg")
        caballoB = caballoB.resize(tam)
        imageCaballoB = ImageTk.PhotoImage(caballoB)
        self.canvasCaballoB.image = imageCaballoB
        self.canvasCaballoB.create_image(imageCaballoB.width()/2,imageCaballoB.height()/2,ancho=CENTER,image=imageCaballoB,tags="piezas")

        self.cw = self.canvasCaballoW = Canvas(self,width=40,height=40)
        self.canvasCaballoW.place(x=420,y=140)
        caballoW = Image.open("piezas/caballoW.jpg")
        caballoW = caballoW.resize(tam)
        imageCaballoW = ImageTk.PhotoImage(caballoW)
        self.canvasCaballoW.image = imageCaballoW
        self.canvasCaballoW.create_image(imageCaballoW.width()/2,imageCaballoW.height()/2,ancho=CENTER,image=imageCaballoW,tags="piezas")
        
        self.rab = self.canvasReinaB = Canvas(self,width=40,height=40)
        self.canvasReinaB.place(x=370,y=185)
        reinaB = Image.open("piezas/reinaB.jpg")
        reinaB = reinaB.resize(tam)
        imageReinaB = ImageTk.PhotoImage(reinaB)
        self.canvasReinaB.image = imageReinaB
        self.canvasReinaB.create_image(imageReinaB.width()/2,imageReinaB.height()/2,ancho=CENTER,image=imageReinaB,tags="piezas")

        self.raw = self.canvasReinaW = Canvas(self,width=40,height=40)
        self.canvasReinaW.place(x=420,y=185)
        reinaW = Image.open("piezas/reinaW.jpg")
        reinaW = reinaW.resize(tam)
        imageReinaW = ImageTk.PhotoImage(reinaW)
        self.canvasReinaW.image = imageReinaW
        self.canvasReinaW.create_image(imageReinaW.width()/2,imageReinaW.height()/2,ancho=CENTER,image=imageReinaW,tags="piezas")

        self.reb = self.canvasReyB = Canvas(self,width=40,height=40)
        self.canvasReyB.place(x=370,y=230)
        reyB = Image.open("piezas/reyB.jpg")
        reyB = reyB.resize(tam)
        imageReyB = ImageTk.PhotoImage(reyB)
        self.canvasReyB.image = imageReyB
        self.canvasReyB.create_image(imageReyB.width()/2,imageReyB.height()/2,ancho=CENTER,image=imageReyB,tags="piezas")

        self.rew = self.canvasReyW = Canvas(self,width=40,height=40)
        self.canvasReyW.place(x=420,y=230)
        reyW = Image.open("piezas/reyW.jpg")
        reyW = reyW.resize(tam)
        imageReyW = ImageTk.PhotoImage(reyW)
        self.canvasReyW.image = imageReyW
        self.canvasReyW.create_image(imageReyW.width()/2,imageReyW.height()/2,ancho=CENTER,image=imageReyW,tags="piezas")
        
        self.tb = self.canvasTorreB = Canvas(self,width=40,height=40)
        self.canvasTorreB.place(x=370,y=275)
        torreB = Image.open("piezas/torreB.jpg")
        torreB = torreB.resize(tam)
        imageTorreB = ImageTk.PhotoImage(torreB)
        self.canvasTorreB.image = imageTorreB
        self.canvasTorreB.create_image(imageTorreB.width()/2,imageTorreB.height()/2,ancho=CENTER,image=imageTorreB,tags="piezas")

        self.tw = self.canvasTorreW = Canvas(self,width=40,height=40)
        self.canvasTorreW.place(x=420,y=275)
        torreW = Image.open("piezas/torreW.jpg")
        torreW = torreW.resize(tam)
        imageTorreW = ImageTk.PhotoImage(torreW)
        self.canvasTorreW.image = imageTorreW
        self.canvasTorreW.create_image(imageTorreW.width()/2,imageTorreW.height()/2,ancho=CENTER,image=imageTorreW,tags="piezas")
        

    """
    Crea los botones y etiquetas que se usan en la interfaz
    """
    def creaBotones(self):
        botonGuardar = Button(self, text="Guardar diagrama",command=self.preguntaGuardar )
        botonGuardar.place(x=10,y=330)

        self.selec = Label(self,text="Selecciona una pieza")
        self.selec.place(x=330,y=330)

        delete = Label(self,text="Para borrar una pieza\n del tablero\napriete el boton derecho\n del mouse sobre la pieza")
        delete.place(x=170,y=330)
        
    """
    Nos ayuda a identificar que cuadrado esta seleccionado
    Ya que se tiene el cuadrado
    Se pide que se coloque la pieza indicada
    """        
    def coordenadas(self,evento):
        if(evento.x >= 0 and evento.x < 38):
            col = 0
        elif(evento.x >= 38 and evento.x < 76):
            col = 1
        elif(evento.x >= 76 and evento.x < 112):
            col = 2
        elif(evento.x >= 112 and evento.x < 150):
            col = 3
        elif(evento.x >= 150 and evento.x < 186):
            col = 4
        elif(evento.x >= 186 and evento.x < 222):
            col = 5
        elif(evento.x >= 222 and evento.x < 260):
            col = 6
        elif(evento.x >= 260 and evento.x < 300):
            col = 7
        if(evento.y >= 0 and evento.y < 38):
            ren = 0
        elif(evento.y >= 38 and evento.y < 76):
            ren = 1
        elif(evento.y >= 76 and evento.y < 112):
            ren = 2
        elif(evento.y >= 112 and evento.y < 150):
            ren = 3
        elif(evento.y >= 150 and evento.y < 186):
            ren = 4
        elif(evento.y >= 186 and evento.y < 222):
            ren = 5
        elif(evento.y >= 222 and evento.y < 260):
            ren = 6
        elif(evento.y >= 260 and evento.y < 300):
            ren = 7

        if (self.im == None):
            pass
        else:
            self.imagen = self.creaPieza()
            self.nombre = "pieza" + str(self.contador)
            self.agregaPiezas(self.nombre,self.imagen,ren,col)
            self.contador += 1
            for name in self.piezas:
                self.colocaPieza(name, self.piezas[name][0], self.piezas[name][1])
                self.label = Label(image=self.imagen)
                self.label.image = self.imagen
            self.canvas.tag_raise("piece")
            self.canvas.tag_lower("square")
        
    """
    Se crea una imagen nueva con la pieza que se desea colocar
    """   
    def creaPieza(self):
        tam = (30,30)
        self.im = self.im.resize(tam)
        imagenP = ImageTk.PhotoImage(self.im)
        return imagenP

    """
    Cuando se coloca la pieza en el tablero
    Se prepara para poderla poner
    """
    def agregaPiezas(self,nombre,imagen,col,ren):
        self.canvas.image = imagen
        self.canvas.create_image(col,ren,image=imagen,tags=nombre, anchor=CENTER)
        self.colocaPieza(nombre,col,ren)

    """
    Ya que se tiene la imagen que se va a poner en el tablero
    Se coloca en el cuadrado que se haya seleccionado con el mouse
    """
    def colocaPieza(self,nombre,col,ren):
        self.piezas[nombre] = (col,ren)
        x0 = (ren * self.tam) + int(self.tam/2)
        y0 = (col * self.tam) + int(self.tam/2)
        self.canvas.coords(nombre,x0,y0)

    """
    Borra una pieza que sea seleccionada en el tablero
    """
    def borra(self,evento):
        if(evento.x >= 0 and evento.x < 38):
            col = 0
        elif(evento.x >= 38 and evento.x < 76):
            col = 1
        elif(evento.x >= 76 and evento.x < 112):
            col = 2
        elif(evento.x >= 112 and evento.x < 150):
            col = 3
        elif(evento.x >= 150 and evento.x < 186):
            col = 4
        elif(evento.x >= 186 and evento.x < 222):
            col = 5
        elif(evento.x >= 222 and evento.x < 260):
            col = 6
        elif(evento.x >= 260 and evento.x < 300):
            col = 7
        if(evento.y >= 0 and evento.y < 38):
            ren = 0
        elif(evento.y >= 38 and evento.y < 76):
            ren = 1
        elif(evento.y >= 76 and evento.y < 112):
            ren = 2
        elif(evento.y >= 112 and evento.y < 150):
            ren = 3
        elif(evento.y >= 150 and evento.y < 186):
            ren = 4
        elif(evento.y >= 186 and evento.y < 222):
            ren = 5
        elif(evento.y >= 222 and evento.y < 260):
            ren = 6
        elif(evento.y >= 260 and evento.y < 300):
            ren = 7
            
        for name,tupla in (self.piezas.iteritems()):
            if (tupla[0] == ren and tupla[1] == col):
                del self.piezas[name]
                self.canvas.delete(name)
                break
        
    """
    Se obtiene la torre blanca
    """
    def obtenImagenTW(self,evento):
        ps = self.tw.postscript()
        self.im = Image.open(io.BytesIO(ps.encode('utf-8')))
        self.selec.config(text="Torre blanca seleccionada")

    """
    Se obtiene la torre negra
    """
    def obtenImagenTB(self,evento):
        ps = self.tb.postscript()
        self.im = Image.open(io.BytesIO(ps.encode('utf-8')))
        self.selec.config(text="Torre negra seleccionada")
        
    """
    Se obtiene el peon blanco
    """
    def obtenImagenPW(self,evento):
        ps = self.pw.postscript()
        self.im = Image.open(io.BytesIO(ps.encode('utf-8')))
        self.selec.config(text="Peon blanco seleccionado")
        
    """
    Se obtiene el peon negro
    """
    def obtenImagenPB(self,evento):
        ps = self.pb.postscript()
        self.im = Image.open(io.BytesIO(ps.encode('utf-8')))
        self.selec.config(text="Peon negro seleccionado")
        
    """
    Se obtiene el alfil blanco
    """
    def obtenImagenAW(self,evento):
        ps = self.aw.postscript()
        self.im = Image.open(io.BytesIO(ps.encode('utf-8')))
        self.selec.config(text="Alfil blanco seleccionado")
        
    """
    Se obtiene el alfil negro
    """
    def obtenImagenAB(self,evento):
        ps = self.ab.postscript()
        self.im = Image.open(io.BytesIO(ps.encode('utf-8')))
        self.selec.config(text="Alfil negro seleccionado")
        
    """
    Se obtiene el caballo blanco
    """
    def obtenImagenCW(self,evento):
        ps = self.cw.postscript()
        self.im = Image.open(io.BytesIO(ps.encode('utf-8')))
        self.selec.config(text="Caballo blanco seleccionado")
        
    """
    Se obtiene el caballo negro
    """
    def obtenImagenCB(self,evento):
        ps = self.cb.postscript()
        self.im = Image.open(io.BytesIO(ps.encode('utf-8')))
        self.selec.config(text="Caballo negro seleccionado")
        
    """
    Se obtiene la reina blanca
    """
    def obtenImagenRAW(self,evento):
        ps = self.raw.postscript()
        self.im = Image.open(io.BytesIO(ps.encode('utf-8')))
        self.selec.config(text="Reina blanca seleccionada")
        
    """
    Se obtiene la reina negra
    """
    def obtenImagenRAB(self,evento):
        ps = self.rab.postscript()
        self.im = Image.open(io.BytesIO(ps.encode('utf-8')))
        self.selec.config(text="Reina negra seleccionada")
        
    """
    Se obtiene el rey blanco
    """
    def obtenImagenREW(self,evento):
        ps = self.rew.postscript()
        self.im = Image.open(io.BytesIO(ps.encode('utf-8')))
        self.selec.config(text="Rey blanco seleccionado")
        
    """
    Se obtiene el rey negro
    """
    def obtenImagenREB(self,evento):
        ps = self.reb.postscript()
        self.im = Image.open(io.BytesIO(ps.encode('utf-8')))
        self.selec.config(text="Rey negro seleccionado")
        
    """
    Son las acciones que se pueden hacer en la interfaz
    """
    def acciones(self):
        self.canvasPeonB.bind("<Button-1>",self.obtenImagenPB)
        self.canvasPeonW.bind("<Button-1>",self.obtenImagenPW)
        self.canvasAlfilB.bind("<Button-1>",self.obtenImagenAB)
        self.canvasAlfilW.bind("<Button-1>",self.obtenImagenAW)
        self.canvasCaballoB.bind("<Button-1>",self.obtenImagenCB)
        self.canvasCaballoW.bind("<Button-1>",self.obtenImagenCW)
        self.canvasReinaB.bind("<Button-1>",self.obtenImagenRAB)
        self.canvasReinaW.bind("<Button-1>",self.obtenImagenRAW)
        self.canvasReyB.bind("<Button-1>",self.obtenImagenREB)
        self.canvasReyW.bind("<Button-1>",self.obtenImagenREW)
        self.canvasTorreB.bind("<Button-1>",self.obtenImagenTB)
        self.canvasTorreW.bind("<Button-1>",self.obtenImagenTW)
        self.canvas.bind("<Button-1>",self.coordenadas)
        self.canvas.bind("<Button-3>",self.borra)
        
    """
    Ventana emergente para pedir el nombre con el que se guardara el diagrama
    """
    def preguntaGuardar(self):
        self.top = Toplevel()

        self.label = Label (self.top, text= "El diagrama se guardara en formato .jpg")
        self.label.pack()

        self.entrytext = StringVar()
        Entry(self.top, textvariable=self.entrytext).pack()
        
        self.buttontext = StringVar()
        self.buttontext.set("Guardar")
        self.button = Button(self.top, textvariable=self.buttontext, command= lambda: self.guardarImagen(self.entrytext)).pack()
        
    """
    Funcion para guardar el diagrama
    """
    def guardarImagen(self,entrytext):
        diagrama = Image.new("RGB",(300,300),"white")
        self.entrytext = entrytext.get()
        nombre = self.entrytext + ".jpg"
        ps = self.canvas.postscript()
        im = Image.open(io.BytesIO(ps.encode('utf-8')))
        im.save(nombre)
        self.top.destroy()

"""
Se ejecuta el programa
Se crea la interfaz y se mantiene en un ciclo
"""
if __name__ == "__main__":
    root = Tk()
    root.geometry("500x400")
    root.title("Diagramador")
    root.wm_state("normal")
    app = Diagrama(root)
    root.mainloop()
