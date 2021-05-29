import tkinter as tk
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox 

class keluar:
    def keluar():
        for n in range(1):
            ucapan="Terimakasih telah menggunakan jasa GB EXP iEx"
            messagebox.showinfo("iEx Jasa GB Game Online", ucapan)
            exit(0)

#Menu Point Blank
def PB():
    def pesan():
        if len(stringID.get()) == 0:
            messagebox.showerror("Error!!!","BELUM MENGISI ID ANDA")
            return 0
        if len(stringpass.get()) == 0:
            messagebox.showerror("Error!!!","BELUM MENGISI PASSWORD ANDA")
            return 0
        if len(stringnick.get()) == 0:
            messagebox.showerror("Error!!!","BELUM MENGISI NICNAME ANDA")
            return 0
        if len(stringpangkat.get()) == 0:
            messagebox.showerror("Error!!!","BELUM MENGISI PANGKAT ANDA")
            return 0
        if tujuan.get() == 0:
            messagebox.showerror("Eror!!!","BELUM MEMILIH EXP")
            return 0
        else:
            if tujuan.get()==1:
                harga="50.000"
                exp="1 JT EXP"
                waktu="1 Minggu"                   
            elif tujuan.get()==2:
                harga="100.000"
                exp="10 JT EXP"
                waktu="2 Minggu"                    
            elif tujuan.get()==3:
                harga="150.000"
                exp="50 JT EXP"
                waktu="3 Minggu"                   
            elif tujuan.get()==4:
                harga="200.000"  
                exp="100 JT EXP"
                waktu="1 Bulan"
            keluar =  "Nick Name: " + stringnick.get()+ "\nPilihan exp: " + exp + "\nDengan harga Rp" + harga + "\nAkan di proses selama " + waktu
            messagebox.showinfo("iEx Jasa GB Game Online", keluar)
            return 0

    global bg1
    pb = Toplevel()
    pb.geometry("650x350")
    pb.title('iEx Jasa GB Game Online')
    pb.iconbitmap('D:/Tio/iEx.ico')

    # Define image
    bg1 = PhotoImage(file="D:/Tio/GUI2.png")
    # Create a canvas
    my_canvas = Canvas(pb, width=800, height=500)
    my_canvas.pack(fill="both", expand=True)
    # Set image in canvas
    my_canvas.create_image(0,0, image=bg1, anchor="nw")
    # Add a label
    my_canvas.create_text(370, 55, text="GB Point Blank", font=("Garamond", 50), fill="#9DCBE7")

    #ID
    stringID = StringVar()
    ID = Entry(pb, width = 20, textvariable=stringID).place(x = 180, y = 130) 

    #Password
    stringpass = StringVar()
    password = Entry(pb, width = 20, textvariable=stringpass).place(x = 180, y = 170)

    #NickName
    stringnick = StringVar()
    nick = Entry(pb, width = 20, textvariable=stringnick).place(x = 180, y = 210)

    #Pangakat
    stringpangkat = StringVar()
    pangkat = Entry(pb, width = 20, textvariable=stringpangkat).place(x = 180, y = 250)

    #label
    label1 = tk.Label(pb, bg="#B6C7DD", text ="Pilih Jumlah EXP yang Ingin Anda Pesan\t:").place(x=350, y=130)
    label2 = tk.Label(pb, bg="#789FB5", text = "Masukkan ID \t\t:").place(x=10, y=130)
    label3 = tk.Label(pb, bg="#789FB5", text = "Masukkan Password \t:").place(x=10, y=170)
    label4 = tk.Label(pb, bg="#789FB5", text = "Masukkan Nickname \t:").place(x=10, y=210)
    label5 = tk.Label(pb, bg="#789FB5", text = "Masukkan Pangkat Anda \t:").place(x=10, y=250)

    #EXP
    tujuan = IntVar()
    button1 = Radiobutton(pb, bg="#457373", text="1 JT EXP", variable=tujuan, value=1).place(x=350, y=160)
    button2 = Radiobutton(pb, bg="#457373", text="10 JT EXP", variable=tujuan, value=2).place(x=350, y=190)
    button3 = Radiobutton(pb, bg="#457373", text="50 JT EXP", variable=tujuan, value=3).place(x=350, y=220)
    button4 = Radiobutton(pb, bg="#457373", text="100 JT EXP", variable=tujuan, value=4).place(x=350, y=250)  

    #BUTTON Window
    button1 = Button(pb, width=35, height=1, bg="#7393C2", command = pesan, text="PESAN").place(x=50,y=300)
    button2 = Button(pb, width=35, height=1, bg="#7393C2", command = pb.destroy, text="KEMBALI").place(x=350,y=300)

#Menu Valorant
def valo():
    def pesan():
        if len(stringID.get()) == 0:
            messagebox.showerror("Error!!!","BELUM MENGISI USERNAME ANDA")
            return 0 
        if len(stringpass.get()) == 0:
            messagebox.showerror("Error!!!","BELUM MENGISI PASSWORD ANDA")
            return 0
        if len(stringnick.get()) == 0:
            messagebox.showerror("Error!!!","BELUM MENGISI RIOT ID ANDA")
            return 0
        if tujuan.get() == 0:
            messagebox.showerror("Eror!!!","BELUM MEMILIH RANK")
            return 0
        else:
            if tujuan.get()==1:
                harga="7.000"
                exp="Iron"
                waktu="1 Hari"
            elif tujuan.get()==2:
                harga="10.000"
                exp="Bronze"
                waktu="2 Hari"
            elif tujuan.get()==3:
                harga="14.000"
                exp="Silver"
                waktu="3 Hari"
            elif tujuan.get()==4:
                harga="22.000"  
                exp="Gold"
                waktu="4 Hari"
            elif tujuan.get()==5:
                harga="37.000"  
                exp="Platinum"
                waktu="6 Hari"
            elif tujuan.get()==6:
                harga="70.000"  
                exp="Diamond"
                waktu="1 Minggu"
            hasil = "Riot ID " + stringnick.get() + "\nMemilih Rank GB " + exp + "\ndengan harga Rp" + harga + "\nakan di proses selama " + waktu
            messagebox.showinfo("iEx Jasa GB Game Online", hasil)
            return 0

    global bg1
    valo = Toplevel()
    valo.geometry("650x350")
    valo.title('iEx Jasa GB Game Online')
    valo.iconbitmap('D:/Tio/iEx.ico')

    # Define image
    bg1 = PhotoImage(file="D:/Tio/Wallpaper/GUI.png")
    # Create a canvas
    my_canvas = Canvas(valo, width=800, height=500)
    my_canvas.pack(fill="both", expand=True)
    # Set image in canvas
    my_canvas.create_image(0,0, image=bg1, anchor="nw")
    # Add a label
    my_canvas.create_text(360, 55, text="GB Valorant", font=("Garamond", 50), fill="#9DCBE7")

    #USERNAME 
    stringID = StringVar()
    ID = Entry(valo, width = 20, textvariable=stringID).place(x = 180, y = 125) 

    #Password
    stringpass = StringVar()
    password = Entry(valo, width = 20, textvariable=stringpass).place(x = 180, y = 185)

    #RIOT ID
    stringnick = StringVar()
    nick = Entry(valo, width = 20, textvariable=stringnick).place(x = 180, y = 245)

    #label
    label1 = tk.Label(valo, bg="#B6C7DD", text ="Pilih Rank yang ingin dipesan\t:").place(x=350, y=125)
    label2 = tk.Label(valo, bg="#789FB5", text = "Masukkan Username \t:").place(x=10, y=125)
    label3 = tk.Label(valo, bg="#789FB5", text = "Masukkan Password \t:").place(x=10, y=185)
    label4 = tk.Label(valo, bg="#789FB5", text = "Masukkan Riot ID  \t:").place(x=10, y=245)

    #RANK
    tujuan = IntVar()
    button1 = Radiobutton(valo, bg="#457373", text="Rank Iron", variable=tujuan, value=1).place(x=350, y=160)
    button2 = Radiobutton(valo, bg="#457373", text="Rank Bronze", variable=tujuan, value=2).place(x=350, y=200)
    button3 = Radiobutton(valo, bg="#457373", text="Rank Silver", variable=tujuan, value=3).place(x=350, y=240)
    button4 = Radiobutton(valo, bg="#457373", text="Rank Gold", variable=tujuan, value=4).place(x=450, y=160)
    button5 = Radiobutton(valo, bg="#457373", text="Rank Platinum", variable=tujuan, value=5).place(x=450, y=200) 
    button6 = Radiobutton(valo, bg="#457373", text="Rank Diamond", variable=tujuan, value=4).place(x=450, y=240) 

    #BUTTON Valo
    button1 = Button(valo, width=35, height=1, bg="#7393C2", command = pesan, text="PESAN").place(x=50,y=300)
    button2 = Button(valo, width=35, height=1, bg="#7393C2", command = valo.destroy, text="KEMBALI").place(x=350,y=300)

#Menu Utama
utama = Tk()  
utama.geometry("500x450")
utama.title("iEx Jasa GB Game Online")
utama.iconbitmap("D:/Tio/iEx.ico")

# Define image
bg = PhotoImage(file="D:/Tio/GUI2.png")
# Create a canvas
my_canvas = Canvas(utama, width=800, height=500)
my_canvas.pack(fill="both", expand=True)
# Set image in canvas
my_canvas.create_image(0,0, image=bg, anchor="nw")
# Add a label
my_canvas.create_text(300, 55, text="iEx Jasa GB", font=("Garamond", 50), fill="#9DCBE7")

#Nulis Nama
stringInama = StringVar()
nama = Entry(utama, width = 20).place(x = 200, y = 160) 

#Nulis No Telp
stringItelp = StringVar()
telp = Entry(utama, width = 20).place(x = 200, y = 190) 

#Nulis ID Line
stringIline = StringVar()
line = Entry(utama, width = 20).place(x = 200, y = 220) 

#Label Menu Utama
label1 = tk.Label(utama, bg="#789FB5", text = "Masukkan Data Diri Anda").place(x = 180, y=110)
label2 = tk.Label(utama, bg="#789FB5", text = "Masukkan Nama Anda \t:").place(x = 20, y=160)
label3 = tk.Label(utama, bg="#789FB5", text = "Masukkan No Telp \t:").place(x = 20, y=190)
label4 = tk.Label(utama, bg="#789FB5", text = "Masukkan ID LINE \t:").place(x = 20, y=220)
label5 = tk.Label(utama, bg="#789FB5", text = "Silahkan Pilih Game Yang Mau Di GB").place(x = 160, y=260)

#Button TOP
button1 = Button(utama, width=50, height=1, bg="#7393C2", command=PB, text="POINT BLANK").place(x = 75,y = 300)
button2 = Button(utama, width=50, height=1, bg="#7393C2", command=valo, text="VALORANT").place(x = 75,y = 350)
button3 = Button(utama, width=50, height=1, bg="#7393C2", command = keluar.keluar, text="KELUAR").place(x=75,y=400)

utama.mainloop()