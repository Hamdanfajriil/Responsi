from types import coroutine
import conn
conn.header("Manajement RAM dalam Komputer")

blok = 2 # dikarenakan tidak ada inptan blok, maka saya memasukan blok secara otomatis di program
Ram = int(input("Masukan Kapasitas Total RAM\t: "))
petabit = int(input("Masukan Total Petabit\t\t: "))
print("-"*50)
os = int(input("Masukan kapasitas RAM yang di gunakan OS\t : "))
kaprog1 = int(input("Masukan Kapasitas RAM yang di gunakan program 1\t : "))
kaprog2 = int(input("Masukan Kapasitas RAM yang di gunakan program 2\t : "))

#perhitungan
pt = conn.Ramterpakai(os,kaprog1,kaprog2)
ptt = conn.RamTidakTerpakai(Ram,os,kaprog1,kaprog2)
pb = conn.hitungPetaBit(conn.ubahRamKeMbps(Ram), blok)
jb = conn.hitungPetaBit(conn.ubahRamKeMbps(kaprog1 + kaprog2),pb)


conn.hasil("Output :")
print("Total RAM\t\t\t= ",Ram)
print("Total Petabit\t\t\t= ",petabit)
print("Total Kapasitas per Petabit\t= ", pb , "Kbps dengan",blok,"blok")
print("Total Ram Terpakai\t\t= ", pt , "Gbps")
print("Total Ram Tidak Terpakai\t= ", ptt , "Gbps")
print("Jumlah Blok yang bernilai 1\t= ",jb)
print("Jumlah Blok yang bernilai 0\t= ", blok - jb)

conn.akhir("5200411006")