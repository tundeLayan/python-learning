import os
# File Objects

# f = open('test.txt', 'r')
# print(f)
# f.close()


# print(os.getcwd())

# context manager 
# with open(os.path.join(os.path.expanduser(os.getcwd()), 'test2.txt'), 'r') as f:
#   # f.write('Hello world')
#   size_to_read = 100

#   f_contents = f.read(size_to_read)

#   while len(f_contents) > 0:
#     print(f_contents, end="*")

#     f_contents = f.read(size_to_read)

# with open('test2.txt', 'r') as rf:
#   with open('test_copy.txt', 'w') as wf:
#     for line in rf:
#       wf.write(line)
#   # print(rf.read())
#   # pass

# copying images
# with open('iphone12pro.jpg', 'rb') as rf:
#   with open('iphone12proCopy.jpg', 'wb') as wf:
#     for chunk in rf:
#       wf.write(chunk)


# copying images chunk by chunk
with open("iphone12pro.jpg", 'rb') as rf:
  with open('iphone12pro_copy.jpg', 'wb') as wf:
    byte_chunk = 4096
    file_chunk = rf.read(byte_chunk)
    while len(file_chunk) > 0:
      wf.write(file_chunk)
      file_chunk = rf.read(byte_chunk)