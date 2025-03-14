import os

# print(dir(os))

# os.chdir('/Users/macintoshhd/dev/python/python tutorial 2')

# os.mkdir('testing-folder-creation')
# os.makedirs('OS-Demo-2/sub-dir-1')

# print('os.getcwd()', os.getcwd())
# print(os.listdir())

# print(os.walk(os.getcwd()))

# for dirpath, dirnames, filenames in os.walk(os.getcwd()):
#   print('Current Path:', dirpath)
#   print('Directories:', dirnames)
#   print('Files:', filenames)
#   print()

print(os.environ.get('HOME'))
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')

print('file_path: ',file_path)

# with open(file)