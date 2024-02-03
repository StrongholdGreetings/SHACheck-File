import tkinter,os,requests,time
from tkinter import messagebox,ttk,filedialog
from tkinter import *
import HashFeature

filename="Choose your file!"
filedir=''
hashmode=["MD5","SHA-1","SHA-224","SHA-256","SHA-384","SHA-512"]
appdir=os.getcwd()

def main():
    if not os.path.isdir(appdir+'/Data'):
	    os.makedirs(appdir+"/Data")
    global filenamechoice,InProgress
    winmain=Tk()
    winmain.geometry("500x450")
    winmain.title("SHACheck File")
    
    Status=Label(winmain,text="Status:",font=("Arial",12,"bold"))
    Status.place(relx=0.5,rely=0.78,anchor=CENTER)
    
    InProgress=Label(winmain,text="READY!",font=("Arial",12,"bold"),fg="green")
    InProgress.place(relx=0.5,rely=0.82,anchor=CENTER)

    try:
        winmain.iconbitmap("Data/Icon.ico")

        img=PhotoImage(file='Data/IconPhotoSmall.png')
        Label(winmain,image=img).place(relx=0.25,rely=0.035,anchor=W)

        img2=PhotoImage(file='Data/key.png')
        Label(winmain,image=img2).place(relx=0.282,rely=0.92,anchor=W)

        img3=PhotoImage(file='Data/IconPhotoSmall.png')
        Label(winmain,image=img3).place(relx=0.69,rely=0.035,anchor=W)
    except tkinter.TclError:
        response=requests.get("https://github.com/StrongholdGreetings/SHACheck-File/raw/main/Data/Icon.ico")
        with open('Data/Icon.ico',"wb") as a:
            a.write(response.content)
        response=requests.get("https://github.com/StrongholdGreetings/SHACheck-File/raw/main/Data/IconPhotoSmall.png")
        with open('Data/IconPhotoSmall.png',"wb") as a:
            a.write(response.content)
        response=requests.get("https://github.com/StrongholdGreetings/SHACheck-File/raw/main/Data/key.png")
        with open('Data/key.png',"wb") as a:
            a.write(response.content)
        winmain.iconbitmap("Data/Icon.ico")

    heavyfile=Label(winmain,text="* Heavier file may result in slower performance (even CertUtil does)!")
    heavyfile.place(relx=0.5,rely=0.65,anchor=CENTER)

    cannotfillall=Label(winmain,text="* I cannot add all hashing algorithm since there are too much!",font=('Arial',10))
    cannotfillall.pack(side=BOTTOM)

    var = StringVar(winmain)
    var.set(hashmode[3])
    w=OptionMenu(winmain,var,*hashmode)
    w.configure(font=('Arial',9,'bold'))
    w.place(relx=0.53,rely=0.92,anchor=W)

    filenamechoice=Label(winmain,text=filename,font=('Times New Roman',12))
    filenamechoice.place(relx=0.5,rely=0.5,anchor=CENTER)

    def GetFileSize():
        global sizeunit,filesize,filedir,sizestring
        sizeunit=" B"
        filesize=round(os.path.getsize(filedir),2)
        if filesize>=1024:
            filesize=round(filesize/1024,2)
            sizeunit=" kB"
            if filesize>=1024:
                filesize=round(filesize/1024,2)
                sizeunit=" MB"
                if filesize>=500:
                    sizeunit=" MB (Getting hash may be slower on this file!)"
                if filesize>=1024:
                    filesize=round(filesize/1024,2)
                    sizeunit=" GB (Getting hash may be slower on this file!)"
                    if filesize>=1024:
                        filesize=round(filesize/1024,2)
                        sizeunit=" TB (Getting hash will be slower on this file!)"
        sizestring=f"{filesize}{sizeunit}"

    def AskForFileDir():
        global filedir,filename,filenamechoice
        filedir=filedialog.askopenfilename()
        filename=list(filedir.split("/"))[-1]
        if filename=="":
            messagebox.showerror("SHACheck File","You haven't chosen a file yet!")
            filename="Choose your file!"
            filedir=""
        filenamechoice.destroy()
        filenamechoice=Label(text=filename,font=('Times New Roman',12))
        filenamechoice.place(relx=0.5,rely=0.5,anchor=CENTER)

    def ShowFileDirectory():
        global filedir,sizestring
        if filedir=='':
            messagebox.showerror("Error!","Action cannot be done! File not selected!")
        else:            
            try:
                GetFileSize()
                messagebox.showinfo("SHACheck File",f"The directory to your chosen file:\n{filedir}\nFile size: {sizestring}")
            except NameError:
                messagebox.showerror("Error!","Action cannot be done! File not selected!")

    def WorkInProgress(event):
            os.system('start \"\" https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    def StartHash():
        global InProgress,filedir
        if filedir=='':
            messagebox.showerror("Error!","Action cannot be done! File not selected")
        else:
            try:
                with open("Data/SHATemp.txt","w",encoding="utf-8") as f:
                    f.write(filedir)
                hashchoice=var.get()
                InProgrss=Label(winmain,text="RUNNING!",font=("Arial",12,"bold"),fg="red")
                InProgrss.place(relx=0.5,rely=0.82,anchor=CENTER)
                winmain.update()
                winmain.update_idletasks()
                if hashchoice=="MD5":
                    HashFeature.HashMD5()
                elif hashchoice=="SHA-1":
                    HashFeature.HashSHA1()
                elif hashchoice=="SHA-224":
                    HashFeature.HashSHA224()
                elif hashchoice=="SHA-256":
                    HashFeature.HashSHA256()
                elif hashchoice=="SHA-384":
                    HashFeature.HashSHA384()
                elif hashchoice=="SHA-512":
                    HashFeature.HashSHA512()
                InProgrss.destroy()
            except NameError:
                messagebox.showerror("Error!","Action cannot be done! File not selected!")
    title1=Label(winmain,text="SHACheck File",font=('Arial',20,'bold'))
    title1.pack()

    winmain.bind("WYNS2022ID",WorkInProgress)

    title2=Label(winmain,text="Made by StrongholdGreetings",font=('Arial',10,'normal'))
    title2.pack()   

    title2p5=Label(winmain,text="Version 1.0",font=('Arial',9,'normal'))
    title2p5.pack()

    title3=Label(winmain,text="Hash Algorithm:",font=('Arial',10,'normal'))
    title3.place(relx=0.43,rely=0.92,anchor=CENTER)

    title4=Label(winmain,text="File you choose to chek hash is:",font=('Arial',15,'bold'))
    title4.place(relx=0.5,rely=0.44,anchor=CENTER)



    askfilename=Button(winmain,height=1,text="Choose in Explorer",command=AskForFileDir)
    askfilename.place(relx=0.5,rely=0.58,anchor=CENTER)

    showfiledir=Button(winmain,height=1,text="Show directory",command=ShowFileDirectory)
    showfiledir.place(relx=0.3,rely=0.58,anchor=CENTER)

    starthash=Button(winmain,height=1,width=11,text="Check hash!",command=StartHash)
    starthash.place(relx=0.699,rely=0.58,anchor=CENTER)

    winmain.resizable(False,False)
    winmain.mainloop()
    #DO NOT PUT ANY LINE BEHIND THIS TEXT

try:
    main()
except FileNotFoundError as e:
    messagebox.showerror("Error!",e)