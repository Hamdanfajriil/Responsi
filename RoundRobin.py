import conn

conn.header("Penjadwalan Round Robin")

Nm1 = str(input("Input Nama 1\t: "))
lama1 = int(input("Input Waktu 1\t: "))
Nm2 = str(input("Input Nama 2\t: "))
lama2 = int(input("Input Waktu 2\t: "))
Nm3 = str(input("Input Nama 3\t: "))
lama3 = int(input("Input Waktu 3\t: "))
quantumtime = int(input("jatah Waktu(quantum time)\t: "))

x = conn.cuy(lama1,lama2,lama3)

conn.hasil("Output :")
print("Nama Program")
print("\n",Nm1,lama1,"\n",Nm2,lama2, "\n",Nm3,lama3)

print("Lama Waktu Program 1-3 =",x)
print("Quantum Time / Jatah Waktu :",quantumtime)
print("Urutan Round Robin nya adalah ")

rr = conn.proses(lama1,lama2,lama3)
conn.akhir("5200411006")



