import os

os.chdir('/Users/macintoshhd/dev/python/scripts/files')

print(os.getcwd())

for f in os.listdir():
  f_name, f_ext = os.path.splitext(f)
  f_title, f_num = f_name.split(" ")

  f_title = f_title.strip()
  f_num = f_num.strip()[1:].zfill(2)

  new_name = f'{f_num}-{f_title}{f_ext}'

  os.rename(f, new_name)
  # print(file_name.split(" "))