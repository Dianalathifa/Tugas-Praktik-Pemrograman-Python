#!/usr/bin/env python
# coding: utf-8

# In[20]:


angka = [0, 1]
panjang = int(input("Masukan panjang deret fibbonacci: "))

for i in range (panjang):
        angka.append(angka[-2]+angka[-1])
        print(angka)


# In[2]:


def array(kal):
    konsonan = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnopqrstvwxyz"
    vokal = "AIUEOaiueo"
    jumlahvokal =""
    jumlahkonsonan =""
    totalhuruf=""

    for nama in kal:
        if nama in vokal:
            jumlahvokal += nama
            totalhuruf= jumlahvokal+jumlahkonsonan

        if nama in konsonan:
            jumlahkonsonan += nama
        
    print("Jumlah banyaknya huruf vokal : ")
    print(len(jumlahvokal))
    print("Jumlah banyaknya huruf konsonan : ")
    print(len(jumlahkonsonan))
    print("Total huruf : ")
    print(len(totalhuruf))
    print("Setiap huruf dalam kalimat: ")
    print(list(kal))
    
print('\nProgram Kumpulan Huruf Menjadi Sebuah Tulisan\n')
kal= str (input("Masukkan Nama : "))
array(kal)


# In[ ]:




