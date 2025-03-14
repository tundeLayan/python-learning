# def hello_func(greeting, name="You"):
#   return f'{greeting} {name} Function'
  # pass

# print(hello_func('Hola'))


def student_info(*args, **kwargs):
  print('args', args)
  print('kwargs',kwargs)

student_info('Math', 'Art', name='John', age=22)