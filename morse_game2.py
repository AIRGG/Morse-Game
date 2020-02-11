import os
import random

morse = {
	"A":".-",
	"B":"-...",
	"C":"-.-.",
	"D":"-..",
	"E":".",
	"F":"..-.",
	"G":"--.",
	"H":"....",
	"I":"..",
	"J":".---",
	"K":"-.-",
	"L":".-..",
	"M":"--",
	"N":"-.",
	"O":"---",
	"P":".--.",
	"Q":"--.-",
	"R":".-.",
	"S":"...",
	"T":"-",
	"U":"..-",
	"V":"...-",
	"W":".--",
	"X":"-..-",
	"Y":"-.--",
	"Z":"--..",
	"1":".----",
	"2":"..---",
	"3":"...--",
	"4":"....-",
	"5":".....",
	"6":"-....",
	"7":"--...",
	"8":"---..",
	"9":"----.",
	"0":"-----"
}
def ambilAngka(awal=0, akhir=757):
	acak = random.randint(awal, akhir)
	return acak
def bersih(strnya):
	isi = strnya.replace(" ", "")
	return isi
def rumbey():
	print("==========================================")
def soal(strnya):
	try:
		hasil = ""
		strnya = strnya.replace(" ", "")
		strnya = strnya.split(",")
		for x in strnya:
			for a in x:
				for k, v in morse.items():
					if a.upper() == k:
						hasil += "{}, ".format(v)
						#print(" Huruf: {0} -> {1}".format(k, v))
		return hasil+"| "
	except Exception as e:
		print(" Ada Kesalahan: {0}".format(e))


while True:
	os.system("cls")
	print(" 1 : Easy")
	print(" 2 : Medium")
	print(" 3 : Hard")
	pilihLvl = str(input(" Level: ")).upper()

	f = open("indonesian-stopwords-complete.txt", "r")
	isia = f.read()
	isi = isia.split("\n")
	morseAcakV = isi
	morseAcakK = isi

	tanya = ""
	jwban = ""
	hasil = ""
	if pilihLvl == "1":
		acak = ambilAngka()
		tanya = soal(isi[acak]).upper()
		jwban = isi[acak].upper()
		print("\n Kode: "+tanya)
		usrJwb = str(input("\n Masukkan Jawaban: ")).upper()
		if usrJwb == jwban:
			rumbey()
			print(" Selamat Jawabannya Benar yaitu, {0}".format(jwban.upper()))
			print("\n Main Lagi? (Y/N)")
			usrCon = input().upper()
			if usrCon == "N":
				break
		else:
			rumbey()
			print(" Maaf Jawaban Salah yang Benar yaitu, {0}".format(jwban.upper()))
			print("\n Main Lagi? (Y/N)")
			usrCon = input().upper()
			if usrCon == "N":
				break


	elif pilihLvl == "2":
		acak = ambilAngka(2, 3)
		for x in range(0,acak):
			ambil = ambilAngka()
			tanya += soal(isi[ambil])
			jwban += isi[ambil]+", "
		jwban = jwban.split(",")
		for x in jwban:
			hasil += x
		print("\n Kode: "+tanya)
		usrJwb = str(input("\n Masukkan Jawaban: ")).upper()
		if bersih(usrJwb.upper()) == bersih(hasil.upper()):
			rumbey()
			print(" Selamat Jawabannya Benar yaitu, {0}".format(hasil.upper()))
			print("\n Main Lagi? (Y/N)")
			usrCon = input().upper()
			if usrCon == "N":
				break
		else:
			rumbey()
			print(" Maaf Jawaban Salah yang Benar yaitu, {0}".format(hasil.upper()))
			print("\n Main Lagi? (Y/N)")
			usrCon = input().upper()
			if usrCon == "N":
				break


	elif pilihLvl == "3":
		acak = ambilAngka(5, 14)
		for x in range(0,acak):
			ambil = ambilAngka()
			tanya += soal(isi[ambil])
			jwban += isi[ambil]+", "
		jwban = jwban.split(",")
		for x in jwban:
			hasil += x
		print("\n Kode: "+tanya)
		usrJwb = str(input("\n Masukkan Jawaban: ")).upper()
		if bersih(usrJwb.upper()) == bersih(hasil.upper()):
			rumbey()
			print(" Selamat Jawabannya Benar yaitu, {0}".format(hasil.upper()))
			print("\n Main Lagi? (Y/N)")
			usrCon = input().upper()
			if usrCon == "N":
				break
		else:
			rumbey()
			print(" Maaf Jawaban Salah yang Benar yaitu, {0}".format(hasil.upper()))
			print("\n Main Lagi? (Y/N)")
			usrCon = input().upper()
			if usrCon == "N":
				break
	else:
		print(" Maaf input Salah :(")