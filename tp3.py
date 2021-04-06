from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import Combobox
from tkinter import filedialog
from tkinter import messagebox
from mahasiswa import Mahasiswa
# Muhammad Iqbal Zain
# 1901423
# Ilkom C2
# Nampilin namanya belom bener

data = []
filename = "-"

class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)


class RadBut(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = StringVar()
      for pick in picks:
        rad = Radiobutton(self, text=pick, value=pick, variable=self.vars)
        rad.pack(side=side, anchor=anchor, expand=YES)
        rad.deselect()
   def state(self):
      return self.vars.get()

bapaknyaRoot = Tk()
bapaknyaRoot.title("TP 3- M Iqbal Z")
bapaknyaRoot.geometry("340x260")

def isiData():
    root = Toplevel()


    root_frame = LabelFrame(root, text="Data", padx=10, pady=10, width=350)
    root_frame.grid(row=1, column=0)



    Label(root_frame, text="Nama :" , anchor="w",width=12).grid(row=0, column=0)
    nama = Entry(root_frame, width=30, borderwidth=5)
    nama.grid(row=0, column=1,columnspan=3,sticky="W")

    Label(root_frame, text="NIM : " , anchor="w", width=12).grid(row=1, column=0)
    nim = Entry(root_frame, width=10, borderwidth=5)
    nim.grid(row=1, column=1,columnspan=3,sticky="W")


    Label(root_frame, text="Jenis Kelamin :" , anchor="w", width=12).grid(row=2, column=0)
    jk = RadBut(root_frame, ['Laki-laki', 'Perempuan'])
    jk.grid(row=2, column=2,sticky="w")

    def label(options, label, row):
        
        Label(root_frame, text=label , anchor="w", width=12).grid(row=row, column=0)

        clicked = StringVar()
        clicked.set(options[0])

        drop = OptionMenu(root_frame, clicked, *options).grid(row=row,column=1,columnspan=3,sticky="W")
        return clicked
    
    pengalaman = label(["None","1 Year","2 Years","3 Years","> 4 Years"], "Pengalaman :" , 3)

    # input1.insert(0, "Nama")

    cek = IntVar()

    Label(root_frame, text="Bahasa :" , anchor="w", width=12).grid(row=4, column=0)

    bahasa = Checkbar(root_frame, ['Python', 'Ruby', 'Perl', 'C++'])
    bahasa.grid(row=4, column=2)
    # lng.config(relief=GROOVE, bd=2)



    def imageFile():
        global  my_image
        global filename
        root.filename = filedialog.askopenfilename(initialdir = "/", title="Select a File", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
        # my_label = Label(root, text=root.filename).grid(row=9, column=0)
        my_image = ImageTk.PhotoImage(Image.open(root.filename))
        # my_image = my_image.subsample(2, 2) 
        # my_image_label = Label(image=my_image).grid(row=6, column=1)
        filename = root.filename
        messagebox.showinfo('Response', 'Alamat file berhasil Tersimpan!!')

    my_btn = Button(root, text="Open File", command=imageFile, width=47).grid(row=5, column=0)

    def save():
        global filename
        data.append( Mahasiswa(nama.get(),nim.get(),jk.state(),pengalaman.get(),list(bahasa.state()),filename))
        filename = '-'
        messagebox.showinfo('Response', 'Data Berhasil Tersimpan!!')
        


    def cabut():
        res = messagebox.askquestion('askquestion', 'Mau cabut?')
        if res == 'yes':
            root.destroy()
        elif res == 'no':
            messagebox.showinfo('Response', 'Bye')
    but = Frame(root)
    button = Button(but, text="Click Me!", command=save,width=29)
    button.pack(side=LEFT, anchor=W, expand=YES)
    button = Button(but, text="Quit", command=cabut, fg="red", bg="#000000",width=17)
    button.pack(side=LEFT, anchor=W, expand=YES)
    but.grid(row=6, column=0)

def KeluarApp():
        res = messagebox.askquestion('askquestion', 'Mau cabut?')
        if res == 'yes':
            bapaknyaRoot.quit()
        elif res == 'no':
            messagebox.showinfo('Response', 'Okay')

def about():
    top = Toplevel()
    top.title("About")

    d_frame = LabelFrame(top, text="Akutu", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="Nama : Muhammad Iqbal Zain \n NIM : 1901423 ", anchor="w").grid(row=0, column=0, sticky="w")
    d_exit = Button(d_frame, text="Exit", command=top.destroy)
    d_exit.grid(row=1, column=0)

#----------------------------------TINGGAL INI-----------------------------------------------

my_img = StringVar()
Heu = ""

def gambar(alamat):
    global Heu
    global my_img
    if alamat == '-':
        messagebox.showinfo('Image', 'Tidak terdapat foto!!')
        
    else:
        guambar = Toplevel(Heu)
        guambar.title("Images")
        #C:/Users/Iqbal Zain/Pictures/Ceuee/_s_hj_159587348_431400288140157_8032183336850918772_n.jpg
        #images/polish_cow.jpg
        # image = image.resize((450, 350), Image.ANTIALIAS)


        my_img = ImageTk.PhotoImage(Image.open(alamat).resize((350, 350), Image.ANTIALIAS))
        my_label = Label(guambar,image=my_img)
        my_label.pack()

        button_quit = Button(guambar, text="Exit", command=guambar.destroy)
        button_quit.pack()
        
def showData():
    global Heu
    Heu = Toplevel()
    Heu.title("Data")

    
    

    but = Frame(Heu)
    Label(but, text="NAMA MAHASISWA", width= 20).pack(side=LEFT,  expand=YES)
    Label(but, text="NIM MHS", width= 10).pack(side=LEFT,  expand=YES)
    Label(but, text="J KELAMIN", width= 10).pack(side=LEFT,expand=YES)
    Label(but, text="PENGALAMAN", width= 12).pack(side=LEFT,expand=YES)
    Label(but, text="Python", width= 6).pack(side=LEFT,expand=YES)
    Label(but, text="Ruby", width= 4).pack(side=LEFT,expand=YES)
    Label(but, text="Pearl", width= 5).pack(side=LEFT,expand=YES)
    Label(but, text="C++", width= 4).pack(side=LEFT,expand=YES)
    Label(but, text=" ", width= 4).pack(side=LEFT,expand=YES)
    but.pack()

    for x in data:
        konten = Frame(Heu)
        Label(konten, text=x.nama, width= 20).pack(side=LEFT,  expand=YES)
        Label(konten, text=x.nim, width= 10).pack(side=LEFT,  expand=YES)
        Label(konten, text=x.jk, width= 10).pack(side=LEFT,expand=YES)
        Label(konten, text=x.pengalaman, width= 10).pack(side=LEFT,expand=YES)
        if (x.bahasa)[0] == 1:
            Label(konten, text="v", width= 6).pack(side=LEFT,expand=YES)
        else:
            Label(konten, text=" ", width= 6).pack(side=LEFT,expand=YES)
        if (x.bahasa)[1] == 1:
            Label(konten, text="v", width= 4).pack(side=LEFT,expand=YES)
        else:
            Label(konten, text=" ", width= 4).pack(side=LEFT,expand=YES)
        if (x.bahasa)[2] == 1:
            Label(konten, text="v", width= 5).pack(side=LEFT,expand=YES)
        else:
            Label(konten, text=" ", width= 5).pack(side=LEFT,expand=YES)
        if (x.bahasa)[3] == 1:
            Label(konten, text="v", width= 4).pack(side=LEFT,expand=YES)
        else:
            Label(konten, text=" ", width= 4).pack(side=LEFT,expand=YES)
        Button(konten, text="FOTO", command=gambar(x.file), width= 4).pack(side=LEFT,expand=YES)
        konten.pack()
        print(x.file)
    Button(Heu, text="Exit", command=Heu.destroy).pack()
    # data_frame = Frame(top,padx=10, pady=10)
    # data_frame..pack(side=LEFT, anchor=W, expand=YES)
    
    # d_summary = Label(data_frame, text="Nama : Muhammad Iqbal Zain \n NIM : 1901423 ", anchor="w").grid(row=0, column=0, sticky="w")
    # d_exit = Button(data_frame, text="Exit", command=top.destroy)
    # d_exit.grid(row=1, column=0)

    

def clearSub():
    data.clear()
    messagebox.showinfo('Response', 'Data Berhasil Dihapus!!')


Label(bapaknyaRoot, text="PENGALAMAN MHS", fg="blue", font=("Arial",25)).pack()
Label(bapaknyaRoot, text="Applikasi untuk mengetahui pengalaman \nbekerja mahasiswa ilmu komputer upi.").pack()
Button(bapaknyaRoot, text="SEE ALL SUBMISSION", command=showData, width=50).pack()
Button(bapaknyaRoot, text="CLEAR SUBMISSION", command=clearSub, width=50).pack()
Button(bapaknyaRoot, text="ABOUT", command=about, width=50).pack()
Button(bapaknyaRoot, text="ISI DATA BARU", command=isiData, width=50).pack()
Label(bapaknyaRoot, text="\n\n").pack()
Button(bapaknyaRoot, text="Exit", command=KeluarApp, width=25, fg="red", bg="#000000").pack()

bapaknyaRoot.mainloop()


# run()
