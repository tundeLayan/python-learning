import shutil
import os

source_path = '/Users/macintoshhd/Documents/Names and Emails.csv'
destination_path = os.getcwd()

shutil.move(source_path, destination_path)


