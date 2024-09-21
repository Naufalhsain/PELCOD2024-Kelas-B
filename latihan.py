orang1="naufal"
orang2="davin"
  

print(f"{orang1} : haloooo davin apa kabar")
print(f"{orang2} : haloooo jugaaa Naufal, alhamdulillah baik")
 
print(f"{orang1} : kamu sekolah dimana ?")
Sekolah_davin= (input(f"{orang2} : aku sekolah di "))

# OPERASI LOGIKA
if Sekolah_davin.upper() == "SMKN 1 KAMAL":
    print(f"{orang1} : Oh kita satu sekolah dong")
else:
    print(f"{orang1} : Oh kamu sekolah di {Sekolah_davin}, Kalau aku sekolah di SMKN 1 KAMAL")

print(f"{orang2} : Jarak antara rumah kamu sama sekolah kamu berapa Km kira-kira") 
jarak_naufal=int(input(f"{orang1} : kurang lebih jaraknya adalah "))
print(f"{orang1} : Kalau kamu berapa Km") 
jarak_davin=int(input(f"{orang2} : kurang lebih jarak aku ke sekolah adalah "))

# OPERASI ARITMATIKA
perbedaan_jarak=(jarak_naufal-jarak_davin)

if jarak_naufal>jarak_davin:
    print(f"{orang1} : Ternyata jarak aku lebih jauh {perbedaan_jarak} Km dari kamu ")
elif jarak_naufal==jarak_davin:
    print(f"{orang1} : Ternyata jarak kita ke sekolah sama-sama {perbedaan_jarak} Km ")
else:
    perbedaan_jarak=abs(jarak_naufal-jarak_davin)
    print(f"{orang1} : Ternyata jarak aku lebih dekat {perbedaan_jarak} Km dari kamu ")