import os

# f = open(os.path.expanduser("~/Desktop/testing_python.txt"), "r")
# f.write('\nHola, testing testing')
# f.close()

# or

with open(os.path.expanduser("~/Desktop/testing_python.txt"), "r") as f:
  # f.write("This was written with the context manager")
  print(f.read())
  for line in f:
    print (line)