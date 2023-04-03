#!/usr/bin/env python
# coding: utf-8

# In[3]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd =""
)
cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE D3_TI_2023")


# In[4]:


#create table
import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database = "D3_TI_2023"
)

#preparing a cursor object
cursorObject = dataBase.cursor()

#creating table
studentRecord = """CREATE TABLE Mata_Kuliah (
                    Kode_MK VARCHAR(10) PRIMARY KEY,
                    Nama_MK VARCHAR(50),
                    Waktu DATE,
                    Ruangan VARCHAR(10)
                    );
                    CREATE TABLE Mahasiswa (
                    NIM VARCHAR(10) PRIMARY KEY,
                    Nama VARCHAR(30),
                    Alamat VARCHAR(255),
                    Mata_Kuliah_Ikut VARCHAR(10),
                    FOREIGN KEY (Mata_Kuliah_Ikut) REFERENCES Mata_Kuliah(Kode_MK)
                    );
                    CREATE TABLE DOSEN (
                    NIP VARCHAR(20) PRIMARY KEY,
                    Nama_Dosen VARCHAR(50),
                    Mata_Kuliah_Ajar VARCHAR(10),
                    FOREIGN KEY (Mata_Kuliah_Ajar) REFERENCES Mata_Kuliah(Kode_MK)
                    );"""
#table created
cursorObject.execute(studentRecord)

# disconnecting from server
dataBase.close()


# In[5]:


#menambahkan data pada tabel Mata Kuliah
import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database = "D3_TI_2023"
)


cursorObject = dataBase.cursor()

sql = "INSERT INTO Mata_Kuliah (Kode_MK, Nama_MK, Waktu, Ruangan)VALUES (%s, %s, %s, %s)"
val = [("MK0001", "Praktik Pemrograman Python", "2023-05-01", "R01"),
       ("MK0002", "Praktik Wireless Communication", "2023-05-02", "R02"),
       ("MK0003", "Praktik Pemrograman Web", "2023-05-03", "R03"),
       ("MK0004", "Basis Data", "2023-05-04", "R04"),
       ("MK0005", "Praktik Mikrokontroller", "2023-05-05", "R05")
       
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[7]:


#menambahkan data pada tabel Mahasiswa
import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database = "D3_TI_2023"
)


cursorObject = dataBase.cursor()

sql = "INSERT INTO Mahasiswa (NIM, Nama, Alamat, Mata_Kuliah_Ikut)VALUES (%s, %s, %s, %s)"
val = [("V3922001", "Amanda", "Jalan Pahlawan No. 10", "MK0001"),
        ("V3922002", "Aris", "Jalan Merdeka No. 20", "MK0002"),
        ("V3922003", "Budi", "Jalan Diponegoro No. 30", "MK0003"),
        ("V3922004", "Citra", "Jalan Ahmad Yani No. 40", "MK0004"),
        ("V3922005", "Diana", "Jalan Sudirman No. 50", "MK0005")
       
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[8]:


#menambahkan data pada tabel Dosen
import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database = "D3_TI_2023"
)


cursorObject = dataBase.cursor()

sql = "INSERT INTO DOSEN (NIP, Nama_Dosen, Mata_Kuliah_Ajar)VALUES (%s, %s, %s)"
val = [("1122330001", "Yusuf Fadlila S.Kom, M.Kom", "MK0001"),
        ("1122330002", "Yusuf Fadlila S.Kom, M.Kom", "MK0002"),
        ("1122330003", "Masbahah S.Pd M.Pd", "MK0003"),
        ("1122330004", "Masbahah S.Pd M.Pd", "MK0004"),
        ("1122330005", "Fendi Aji Purnomo S.Si, M.Eng", "MK0005")
       
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[10]:


import mysql.connector

dataBase= mysql.connector.connect(
    host = "localhost",
    user= "root",
    password = "",
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()

# Query untuk menampilkan data mata kuliah yang diikuti oleh mahasiswa beserta dosen yang mengajar
query = "SELECT Mahasiswa.NIM, Mahasiswa.Nama AS Nama_Mahasiswa, Mata_Kuliah.Nama_MK AS Mata_Kuliah, Dosen.Nama_Dosen          FROM Mahasiswa          INNER JOIN Mata_Kuliah ON Mahasiswa.Mata_Kuliah_Ikut = Mata_Kuliah.Kode_MK          INNER JOIN Dosen ON Dosen.Mata_Kuliah_Ajar = Dosen.Mata_Kuliah_Ajar"

# Mengeksekusi query
cursorObject.execute(query)

# Menampilkan data
for data in cursorObject.fetchall():
    print("NIM        : ", data[0])
    print("Mahasiswa  : ", data[1])
    print("Mata Kuliah: ", data[2])
    print("Dosen      : ", data[3])
    print()
    
# Menutup koneksi ke database
dataBase.close()


# In[ ]:




