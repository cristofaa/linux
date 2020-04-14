#### version demo  ####################
####empresa SURTIDORA DEPARTAMENTAL ###
####@utor cristo Fher martinez ########
####gefe directo lic.raul bailon ######
####gerente Antonio Torres ############
from tkinter import*
from tkinter.filedialog import *


class mi_app():
  def __init__(self):
    directorio = ""
    self.ventana = Tk()
    self.ventana.title("CONTROL PARA EL ENVIO DE MENSAJES SMS")
    self.ventana.geometry("1000x500")
    self.opt = {
        'defaultextension':'.csv' ,
        'filetypes' : [('Imagen', '*.csv'), ('Python','*.csv')]
              }
#asksaveasfile(**opt)
#directorio = askopenfilenames(**opt)


    self.lbl_capacidad = Label(text="capacidad actual")
    self.lbl_num_capacidad = Label (text="234423")
    self.lbl_sms = Label(text="SMS")
    self.lbl_moden_activo1 = Label(text="moden 1",bg="red",font=("Times","14", "bold"))
    self.lbl_moden_activo2 = Label(text="moden 2",bg="red",font=("Times","14", "bold"))
    self.lbl_moden_activo3 = Label(text="moden 3",bg="red",font=("Times","14", "bold"))
    self.lbl_moden_activo4 = Label(text="moden 4",bg="red",font=("Times","14", "bold"))
    self.lbl_moden_activo5 = Label(text="moden 5",bg="red",font=("Times","14", "bold"))
    self.lbl_moden_activo6 = Label(text="moden 6",bg="red",font=("Times","14", "bold"))
    self.lbl_moden_activo7 = Label(text="moden 7",bg="red",font=("Times","14", "bold"))
    self.lbl_moden_activo8 = Label(text="moden 8",bg="red",font=("Times","14", "bold"))
    self.lbl_moden_activo9 = Label(text="moden 9",bg="red",font=("Times","14", "bold"))
    self.lbl_moden_activo10 = Label(text="moden 10",bg="red",font=("Times","14", "bold"))
    self.lbl_moden_activo11 = Label(text="moden 11",bg="red",font=("Times","14", "bold"))
    self.lbl_moden_activo12 = Label(text="moden 12",bg="red",font=("Times","14", "bold"))
    self.lbl_señal1 = Label(text="-100 dbm")
    self.lbl_señal2 = Label(text="-100 dbm")
    self.lbl_señal3 = Label(text="-100 dbm")
    self.lbl_señal4 = Label(text="-100 dbm")
    self.lbl_señal5 = Label(text="-100 dbm")
    self.lbl_señal6 = Label(text="-100 dbm")
    self.lbl_señal7 = Label(text="-100 dbm")
    self.lbl_señal8 = Label(text="-100 dbm")
    self.lbl_señal9 = Label(text="-100 dbm")
    self.lbl_señal10 = Label(text="-100 dbm" )
    self.lbl_señal11 = Label(text="-100 dbm" )
    self.lbl_señal12 = Label(text="-100 dbm" )
    self.lbl_directorio = Label(text="c:/user/cristo/desktop/x.csv")
    self.lbl_enviados = Label(text= "ENVIADOS")
    self.lbl_numeros_enviados = Label(text = "23423423")
    self.txt_log = Entry(text="log")
    self.btn_enpezar = Button(text="EMPERZAR",command = self.empezar)
    self.btn_parar = Button(text = "PARAR",command = self.parar)
    self.btn_enviados = Button(text="LOG",command = self.enviados)
    self.boton_csv =  Button(text=".csv",font=("Times", "32", "bold italic"),command = self.abrir_csv)
    self.lbl_capacidad.place(x=850,y=10)
    self.lbl_num_capacidad.place(x=850,y=30)
    self.lbl_sms.place(x=950,y=30)
    self.lbl_moden_activo1.place(x=0,y=30)
    self.lbl_moden_activo2.place(x=0,y=60)
    self.lbl_moden_activo3.place(x=0,y=90)
    self.lbl_moden_activo4.place(x=200,y=30)
    self.lbl_moden_activo5.place(x=200,y=60)
    self.lbl_moden_activo6.place(x=200,y=90)
    self.lbl_moden_activo7.place(x=400,y=30)
    self.lbl_moden_activo8.place(x=400,y=60)
    self.lbl_moden_activo9.place(x=400,y=90)
    self.lbl_moden_activo10.place(x=600,y=30)
    self.lbl_moden_activo11.place(x=600,y=60)
    self.lbl_moden_activo12.place(x=600,y=90)
    self.lbl_señal1.place(x=100,y=30)
    self.lbl_señal2.place(x=100,y=60)
    self.lbl_señal3.place(x=100,y=90)
    self.lbl_señal4.place(x=300,y=30)
    self.lbl_señal5.place(x=300,y=60)
    self.lbl_señal6.place(x=300,y=90)
    self.lbl_señal7.place(x=500,y=30)
    self.lbl_señal8.place(x=500,y=60)
    self.lbl_señal9.place(x=500,y=90)
    self.lbl_señal10.place(x=700,y=30)
    self.lbl_señal11.place(x=700,y=60)
    self.lbl_señal12.place(x=700,y=90)
    self.boton_csv.place(x=315,y=140,width=300,height=100)
    self.lbl_directorio.place(x=310,y=250)
    self.lbl_enviados.place(x=700,y=300)
    self.lbl_numeros_enviados.place(x=800,y=300)
    self.txt_log.place(x=500,y=300)
    self.btn_enpezar.place(x=315,y=330,width=300,height=50)
    self.btn_parar.place(x=315,y=400,width=50,height=50)
    self.btn_enviados.place(x=560,y=400,width=50,height=50)
    self.ventana.mainloop()



  def empezar(self):
    
    print(self.directorio)
    #print() + "imprimido")
  def parar(self):
    pass
  def enviados(self):
    pass

  def abrir_csv(self):
    self.directorio = askopenfilename()
    print(self.directorio)
    self.lbl_directorio.configure(text=self.directorio)
    return 






def main():
    app = mi_app()
    return 0

if __name__ == '__main__':
    main()




