num = input('What number should we go up to: ')

try:
  num = int(num)
  for i in range(num):
    if i%2 != 0:
      print(i**2)
    else:
      continue
except Exception:
  print('error')