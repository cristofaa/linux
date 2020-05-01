#### version demo  ####################
####empresa SURTIDORA DEPARTAMENTAL ###
####@utor Ing.cristo Fher martinez ####
####gefe directo Lic.Raul Bailon ######
####gerente Antonio Torres ############
from tkinter import*
from tkinter.filedialog import *
import csv,time,os
import serial


class mi_app():
  def __init__(self):
    self.conector1 =  serial.Serial("COM9",19200)
    self.conector2 =  serial.Serial("COM6",19200)
    self.conector3 =  serial.Serial("COM6",19200)
    self.conector4 =  serial.Serial("COM6",19200)
    self.conector5 =  serial.Serial("COM6",19200)
    self.conector6 =  serial.Serial("COM6",19200)
    self.conector7 =  serial.Serial("COM6",19200)
    self.conector8 =  serial.Serial("COM6",19200)
    self.conector9 =  serial.Serial("COM6",19200)
    self.conector10 = serial.Serial("COM6",19200)
    self.conector11 = serial.Serial("COM6",19200)
    self.conector12 = serial.Serial("COM6",19200)

    directorio = ""
    self.var_parar = 0
    self.ventana = Tk()
    self.ventana.title("                  CONTROL PARA EL ENVIO DE MENSAJES SMS")
    self.ventana.geometry("1000x500")
    self.ventana.config(bg="#3b3c34")
    self.opt = {
        'defaultextension':'.csv' ,
        'filetypes' : [('BLASTER', '*.csv'), ('SMS','*.csv')]
              }
#asksaveasfile(**opt)
#directorio = askopenfilenames(**opt)

    self.img_surtidora = PhotoImage(file = "descarga.png")
    self.imagen = Label(self.ventana,image = self.img_surtidora).place(x=60,y=120)
    self.lbl_capacidad = Label(text="capacidad actual",bg="#04a4a3")
    self.lbl_num_capacidad = Label (text="234423",bg="#04a4a3",fg="red")
    self.lbl_sms = Label(text="SMS",bg="#04a4a3")
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
    self.lbl_señal1 = Label(text="-100 dbm",bg="#04a4a3")
    self.lbl_señal2 = Label(text="-100 dbm",bg="#04a4a3")
    self.lbl_señal3 = Label(text="-100 dbm",bg="#04a4a3")
    self.lbl_señal4 = Label(text="-100 dbm",bg="#04a4a3")
    self.lbl_señal5 = Label(text="-100 dbm",bg="#04a4a3")
    self.lbl_señal6 = Label(text="-100 dbm",bg="#04a4a3")
    self.lbl_señal7 = Label(text="-100 dbm",bg="#04a4a3")
    self.lbl_señal8 = Label(text="-100 dbm",bg="#04a4a3")
    self.lbl_señal9 = Label(text="-100 dbm",bg="#04a4a3")
    self.lbl_señal10 = Label(text="-100 dbm" ,bg="#04a4a3")
    self.lbl_señal11 = Label(text="-100 dbm" ,bg="#04a4a3")
    self.lbl_señal12 = Label(text="-100 dbm" ,bg="#04a4a3")
    self.txt_moden1 = Entry()
    self.txt_moden2 = Entry()
    self.txt_moden3 = Entry()
    self.txt_moden4 = Entry()
    self.txt_moden5 = Entry()
    self.txt_moden6 = Entry()
    self.txt_moden7 = Entry()
    self.txt_moden8 = Entry()
    self.txt_moden9 = Entry()
    self.txt_moden10 = Entry()
    self.txt_moden11 = Entry()
    self.txt_moden12 = Entry()
    self.btn_señal   = Button(text="señal",bg= "#353937",command = self.señal)
    

    self.lbl_directorio = Label(text="file" ,bg="#04a4a3")
    self.lbl_enviados = Label(text= "ENVIADOS" ,bg="#04a4a3")
    self.lbl_numeros_enviados = Label(text = "0" ,bg="#04a4a3")
    self.lbl_log = Label(text="log" ,bg="#04a4a3")
    self.btn_enpezar = Button(text="EMPERZAR" ,bg="#353937",command = self.empezar)
    self.btn_parar = Button(text = "PARAR" ,bg="#353937",command = self.parar)
    self.btn_enviados = Button(text="LOG" ,bg="#353937",command = self.enviados)
    self.boton_csv =  Button(text=".csv" ,bg="#353937",font=("Times", "32", "bold italic"),command = self.abrir_csv)
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
    self.lbl_moden_activo10.place(x=595,y=30)
    self.lbl_moden_activo11.place(x=595,y=60)
    self.lbl_moden_activo12.place(x=595,y=90)
    self.lbl_señal1.place(x=140,y=30)
    self.lbl_señal2.place(x=140,y=60)
    self.lbl_señal3.place(x=140,y=90)
    self.lbl_señal4.place(x=340,y=30)
    self.lbl_señal5.place(x=340,y=60)
    self.lbl_señal6.place(x=340,y=90)
    self.lbl_señal7.place(x=540,y=30)
    self.lbl_señal8.place(x=540,y=60)
    self.lbl_señal9.place(x=540,y=90)
    self.lbl_señal10.place(x=750,y=30)
    self.lbl_señal11.place(x=750,y=60)
    self.lbl_señal12.place(x=750,y=90)
    self.boton_csv.place(x=315,y=140,width=300,height=100)
    self.lbl_directorio.place(x=310,y=250)
    self.lbl_enviados.place(x=700,y=300)
    self.lbl_numeros_enviados.place(x=800,y=300)
    self.lbl_log.place(x=300,y=300)
    self.btn_enpezar.place(x=315,y=330,width=300,height=50)
    self.btn_parar.place(x=315,y=400,width=50,height=50)
    self.btn_enviados.place(x=560,y=400,width=50,height=50)

    self.txt_moden1.place(x=80,y=30,width=50)
    self.txt_moden2.place(x=80,y=60,width=50)
    self.txt_moden3.place(x=80,y=90,width=50)
    self.txt_moden4.place(x=280,y=30,width=50)
    self.txt_moden5.place(x=280,y=60,width=50)
    self.txt_moden6.place(x=280,y=90,width=50)
    self.txt_moden7.place(x=480,y=30,width=50)
    self.txt_moden8.place(x=480,y=60,width=50)
    self.txt_moden9.place(x=480,y=90,width=50)
    self.txt_moden10.place(x=690,y=30,width=50)
    self.txt_moden11.place(x=690,y=60,width=50)
    self.txt_moden12.place(x=690,y=90,width=50)
    
    self.btn_señal.place(x=900,y=60)

    self.ventana.mainloop()
    
    

  def empezar(self):
    
    print(self.directorio)
    archivo_csv = open(self.directorio,"r")
    log = open("log.txt","w")
    datos= csv.reader(archivo_csv)
    contador=0
    contador_slog = 0
    for telefono , mensaje in datos: 
######################################################
      if contador_slog == 0:
        self.conector1.write(b"AT\r\n")
        print (self.conector1.readline())
        time.sleep(4)
        self.conector1.write(b'AT+CMGS=\"'+telefono.encode()+ b'\"\r\n')
        print (telefono)
        time.sleep(4)
        self.conector1.write(mensaje.encode())
        print(mensaje)
        time.sleep(4)
        self.conector1.write(bytes([26]))
        time.sleep(0.6)
        log_lectura=self.conector1.readline()
        contador_slog = contador_slog + 1
      elif contador_slog == 1:
        self.conector1.write(b"AT\r\n")
        print (self.conector1.readline())
        time.sleep(4)
        self.conector1.write(b'AT+CMGS=\"'+telefono.encode()+ b'\"\r\n')
        print (telefono)
        time.sleep(4)
        self.conector1.write(mensaje.encode())
        print(mensaje)
        time.sleep(4)
        self.conector1.write(bytes([26]))
        time.sleep(0.6)
        log_lectura=self.conector1.readline()
        contador_slog = contador_slog + 1      
      elif contador_slog == 2:
        self.conector1.write(b"AT\r\n")
        print (self.conector1.readline())
        time.sleep(4)
        self.conector1.write(b'AT+CMGS=\"'+telefono.encode()+ b'\"\r\n')
        print (telefono)
        time.sleep(4)
        self.conector1.write(mensaje.encode())
        print(mensaje)
        time.sleep(4)
        self.conector1.write(bytes([26]))
        time.sleep(0.6)
        log_lectura=self.conector1.readline()
        contador_slog = contador_slog + 1
      elif contador_slog == 3:
        self.conector1.write(b"AT\r\n")
        print (self.conector1.readline())
        time.sleep(4)
        self.conector1.write(b'AT+CMGS=\"'+telefono.encode()+ b'\"\r\n')
        print (telefono)
        time.sleep(4)
        self.conector1.write(mensaje.encode())
        print(mensaje)
        time.sleep(4)
        self.conector1.write(bytes([26]))
        time.sleep(0.6)
        log_lectura=self.conector1.readline()
        contador_slog = contador_slog + 1
      elif contador_slog == 4:
        self.conector1.write(b"AT\r\n")
        print (self.conector1.readline())
        time.sleep(4)
        self.conector1.write(b'AT+CMGS=\"'+telefono.encode()+ b'\"\r\n')
        print (telefono)
        time.sleep(4)
        self.conector1.write(mensaje.encode())
        print(mensaje)
        time.sleep(4)
        self.conector1.write(bytes([26]))
        time.sleep(0.6)
        log_lectura=self.conector1.readline()
        contador_slog = contador_slog + 1
      elif contador_slog == 5:
        self.conector1.write(b"AT\r\n")
        print (self.conector1.readline())
        time.sleep(4)
        self.conector1.write(b'AT+CMGS=\"'+telefono.encode()+ b'\"\r\n')
        print (telefono)
        time.sleep(4)
        self.conector1.write(mensaje.encode())
        print(mensaje)
        time.sleep(4)
        self.conector1.write(bytes([26]))
        time.sleep(0.6)
        log_lectura=self.conector1.readline()
        contador_slog = contador_slog + 1
      elif contador_slog == 6:
        self.conector1.write(b"AT\r\n")
        print (self.conector1.readline())
        time.sleep(4)
        self.conector1.write(b'AT+CMGS=\"'+telefono.encode()+ b'\"\r\n')
        print (telefono)
        time.sleep(4)
        self.conector1.write(mensaje.encode())
        print(mensaje)
        time.sleep(4)
        self.conector1.write(bytes([26]))
        time.sleep(0.6)
        log_lectura=self.conector1.readline()
        contador_slog = contador_slog + 1
      elif contador_slog == 7:
        self.conector1.write(b"AT\r\n")
        print (self.conector1.readline())
        time.sleep(4)
        self.conector1.write(b'AT+CMGS=\"'+telefono.encode()+ b'\"\r\n')
        print (telefono)
        time.sleep(4)
        self.conector1.write(mensaje.encode())
        print(mensaje)
        time.sleep(4)
        self.conector1.write(bytes([26]))
        time.sleep(0.6)
        log_lectura=self.conector1.readline()
        contador_slog = contador_slog + 1
      elif contador_slog = 8:
        self.conector1.write(b"AT\r\n")
        print (self.conector1.readline())
        time.sleep(4)
        self.conector1.write(b'AT+CMGS=\"'+telefono.encode()+ b'\"\r\n')
        print (telefono)
        time.sleep(4)
        self.conector1.write(mensaje.encode())
        print(mensaje)
        time.sleep(4)
        self.conector1.write(bytes([26]))
        time.sleep(0.6)
        log_lectura=self.conector1.readline()
        contador_slog = contador_slog + 1
      elif contador_slog = 9:
        self.conector1.write(b"AT\r\n")
        print (self.conector1.readline())
        time.sleep(4)
        self.conector1.write(b'AT+CMGS=\"'+telefono.encode()+ b'\"\r\n')
        print (telefono)
        time.sleep(4)
        self.conector1.write(mensaje.encode())
        print(mensaje)
        time.sleep(4)
        self.conector1.write(bytes([26]))
        time.sleep(0.6)
        log_lectura=self.conector1.readline()
        contador_slog = contador_slog + 1
      elif contador_slog = 10:
        self.conector1.write(b"AT\r\n")
        print (self.conector1.readline())
        time.sleep(4)
        self.conector1.write(b'AT+CMGS=\"'+telefono.encode()+ b'\"\r\n')
        print (telefono)
        time.sleep(4)
        self.conector1.write(mensaje.encode())
        print(mensaje)
        time.sleep(4)
        self.conector1.write(bytes([26]))
        time.sleep(0.6)
        log_lectura=self.conector1.readline()
        contador_slog = contador_slog + 1
      elif contador_slog = 11:
        self.conector1.write(b"AT\r\n")
        print (self.conector1.readline())
        time.sleep(4)
        self.conector1.write(b'AT+CMGS=\"'+telefono.encode()+ b'\"\r\n')
        print (telefono)
        time.sleep(4)
        self.conector1.write(mensaje.encode())
        print(mensaje)
        time.sleep(4)
        self.conector1.write(bytes([26]))
        time.sleep(0.6)
        log_lectura=self.conector1.readline()
        contador_slog = contador_slog + 1
      elif contador_slog = 12:
        self.conector1.write(b"AT\r\n")
        print (self.conector1.readline())
        time.sleep(4)
        self.conector1.write(b'AT+CMGS=\"'+telefono.encode()+ b'\"\r\n')
        print (telefono)
        time.sleep(4)
        self.conector1.write(mensaje.encode())
        print(mensaje)
        time.sleep(4)
        self.conector1.write(bytes([26]))
        time.sleep(0.6)
        log_lectura=self.conector1.readline()
        contador_slog = 0
            
      
      log.write(str(log_lectura))
      ##print(str(log_lectura))
      contador=contador+1
      self.lbl_numeros_enviados.configure(text = str(contador))
    archivo_csv.close()
    log.close()
    

  def parar(self):
    self.var_parar = 1
  def enviados(self):
    os.system("notepad.exe log.txt")   
 
  def abrir_csv(self):
    self.directorio = askopenfilename(**self.opt)
    print(self.directorio)
    self.lbl_directorio.configure(text=self.directorio)
    return 

  def señal(self):
    self.conector1.write(b"AT\r\n")
    encendido1 = self.conector1.readline()
    if encendido1 == b'OK\r\n':
        self.lbl_moden_activo1.config(bg="green")
        
    self.conector2.write(b"AT\r\n")
    encendido2 = self.conector2.readline()
    if encendido2 == b'OK\r\n':
        self.lbl_moden_activo2.config(bg="green")

    self.conector3.write(b"AT\r\n")
    encendido3 = self.conector3.readline()
    if encendido3 == b'OK\r\n':
        self.lbl_moden_activo3.config(bg="green")


    self.conector4.write(b"AT\r\n")
    encendido4 = self.conector4.readline()
    if encendido4 == b'OK\r\n':
        self.lbl_moden_activo4.config(bg="green")


    self.conector5.write(b"AT\r\n")
    encendido5 = self.conector5.readline()
    if encendido5 == b'OK\r\n':
        self.lbl_moden_activo5.config(bg="green")


    self.conector6.write(b"AT\r\n")
    encendido6 = self.conector6.readline()
    if encendido6 == b'OK\r\n':
        self.lbl_moden_activo6.config(bg="green")





    self.conector7.write(b"AT\r\n")
    encendido7 = self.conector7.readline()
    if encendido7 == b'OK\r\n':
        self.lbl_moden_activo7.config(bg="green")


    self.conector8.write(b"AT\r\n")
    encendido8 = self.conector8.readline()
    if encendido8 == b'OK\r\n':
        self.lbl_moden_activo8.config(bg="green")


    self.conector9.write(b"AT\r\n")
    encendido9 = self.conector9.readline()
    if encendido9 == b'OK\r\n':
        self.lbl_moden_activo9.config(bg="green")


    self.conector10.write(b"AT\r\n")
    encendido10 = self.conector10.readline()
    if encendido10 == b'OK\r\n':
        self.lbl_moden_activo10.config(bg="green")


    self.conector11.write(b"AT\r\n")
    encendido11 = self.conector11.readline()
    if encendido10 == b'OK\r\n':
        self.lbl_moden_activo10.config(bg="green")


    self.conector11.write(b"AT\r\n")
    encendido11 = self.conector11.readline()
    if encendido11 == b'OK\r\n':
        self.lbl_moden_activo11.config(bg="green")




    self.conector12.write(b"AT\r\n")
    encendido12 = self.conector12.readline()
    if encendido12 == b'OK\r\n':
        self.lbl_moden_activo12.config(bg="green")








def main():
    app = mi_app()
    return 0

if __name__ == '__main__':
    main()














