#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Function untuk mencari FPB
def fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function untuk mencari KPK
def kpk(a, b):
    return a * b // fpb(a, b)

# Function untuk menampilkan pilihan menu
def menu():
    print("Pilih operasi:")
    print("1. Mencari FPB")
    print("2. Mencari KPK")
    print("3. Keluar")

# Function utama
def main():
    while True:
        menu()
        choice = input("Masukkan pilihan Anda (1/2/3): ")

        if choice == '1':
            a = int(input("Masukkan bilangan pertama: "))
            b = int(input("Masukkan bilangan kedua: "))
            print("FPB dari", a, "dan", b, "adalah", fpb(a, b))
        elif choice == '2':
            a = int(input("Masukkan bilangan pertama: "))
            b = int(input("Masukkan bilangan kedua: "))
            print("KPK dari", a, "dan", b, "adalah", kpk(a, b))
        elif choice == '3':
            print("Terima kasih sudah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid. Mohon masukkan pilihan yang sesuai.")

if __name__ == "__main__":
    main()


# In[ ]:




