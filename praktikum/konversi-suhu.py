# contoh program konversi suhu

# input suhu celcius
celcius = float(input("masukkan suhu: "))

# konversi
reamur = (4 * celcius) / 5
fahrenheit = (celcius * 9 / 5) + 32

# tampilkan hasil
print("{} celcius = {} reamur".format(celcius, reamur))
print("{} celcius = {} fahrenheit".format(celcius, fahrenheit))
