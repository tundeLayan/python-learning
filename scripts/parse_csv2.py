import csv

html_str = ""
names = []

with open('Names and Emails.csv', 'r') as data_file:
  csv_data = csv.reader(data_file)

  for line in csv_data:
    names.append(f"{line[0]} {line[1]}")

html_str += f'<p>There are currently {len(names)} names. Thank you</p>'

html_str += '\n<ul>'

for name in names:
  html_str += f'\n\t<li>{name}</li>'

html_str += '\n</ul>'

print(html_str)