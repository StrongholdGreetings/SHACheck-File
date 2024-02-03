import hashlib
from tkinter import messagebox
def HashMD5():
    global filedir
    with open("Data/SHATemp.txt","r", encoding="utf-8") as f:
        filedir=f.read()
    filename=list(filedir.split("/"))[-1]
    with open(filedir,'rb') as file:
        data=file.read()
        md5_hash=hashlib.md5(data).hexdigest()
    messagebox.showinfo("SHACheck File",f"The MD5 hash of {filename} is: \n{md5_hash}")

def HashSHA1():
    global filedir
    with open("Data/SHATemp.txt","r", encoding="utf-8") as f:
        filedir=f.read()
    filename=list(filedir.split("/"))[-1]
    with open(filedir,'rb') as file:
        data=file.read()
        sha1_hash=hashlib.sha1(data).hexdigest()
    messagebox.showinfo("SHACheck File",f"The SHA-1 hash of {filename} is: \n{sha1_hash}")

def HashSHA224():
    global filedir
    with open("Data/SHATemp.txt","r", encoding="utf-8") as f:
        filedir=f.read()
    filename=list(filedir.split("/"))[-1]
    with open(filedir,'rb') as file:
        data=file.read()
        sha224_hash=hashlib.sha224(data).hexdigest()
    messagebox.showinfo("SHACheck File",f"The SHA-224 hash of {filename} is: \n{sha224_hash}")

def HashSHA256():
    global filedir
    with open("Data/SHATemp.txt","r", encoding="utf-8") as f:
        filedir=f.read()
    filename=list(filedir.split("/"))[-1]
    with open(filedir,'rb') as file:
        data=file.read()
        sha256_hash=hashlib.sha256(data).hexdigest()
    messagebox.showinfo("SHACheck File",f"The SHA-256 hash of {filename} is: \n{sha256_hash}")

def HashSHA384():
    global filedir
    with open("Data/SHATemp.txt","r", encoding="utf-8") as f:
        filedir=f.read()
    filename=list(filedir.split("/"))[-1]
    with open(filedir,'rb') as file:
        data=file.read()
        sha384_hash=hashlib.sha384(data).hexdigest()
    messagebox.showinfo("SHACheck File",f"The SHA-384 hash of {filename} is: \n{sha384_hash}")

def HashSHA512():
    global filedir
    with open("Data/SHATemp.txt","r", encoding="utf-8") as f:
        filedir=f.read()
    filename=list(filedir.split("/"))[-1]
    with open(filedir,'rb') as file:
        data=file.read()
        sha512_hash=hashlib.sha512(data).hexdigest()
    messagebox.showinfo("SHACheck File",f"The SHA-512 hash of {filename} is: \n{sha512_hash}")