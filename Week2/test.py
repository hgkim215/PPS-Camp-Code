print(ord('A'))
temp = ord('A') - 3
if (temp < 65) :
  temp = 90 - (65 - temp) + 1
  print(temp)
print(chr(temp))