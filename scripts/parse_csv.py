import csv

with open("Names and Emails.csv", 'r') as csv_file:
  csv_reader = csv.reader(csv_file)

  # next(csv_reader)
  with open('new_names_and_emails.csv', 'w') as new_file:
    csv_writer = csv.writer(new_file, delimiter='-')

    for line in csv_reader:
      csv_writer.writerow(line)