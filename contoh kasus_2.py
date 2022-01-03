#contoh kasus_2

umur = int(input("masukkan umur anda :"))
harga_motor = int(input("masukkan harga motor Rp :"))


if umur >=80:
    print("anda tidak dspat boleh berkendara")
elif umur >=17:
    pajak = harga_motor*7.5/100
    print("kamu dapat membuat sim")
else:
    print("anda tidak dapat membuat sim")
