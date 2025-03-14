# lists
courses = ['Physics', 'Mathematics', 'English', 'Chemistry']
# courses_2 = ['Government', 'Accounts', 'Economics']

# nums = [1,2,3,4,5]

# print(max(nums))

# for course in courses:
#   print(course)

# print(len(courses))

# courses.append('Art')

# courses.insert(1, 'Agric')

# # merge two lists
# courses.extend(courses_2) 

# print(courses) 

for index, course in enumerate(courses, start=1):
  print(index, course)

# course_str = ', '.join(courses).split(', ')

# print(course_str)

# # SETS
# cs_courses = {'history', 'math', 'physics', 'compSci'}
# art_courses = {'history', 'math', 'art', 'design'}


# print(cs_courses.intersection(art_courses))
# print(cs_courses.difference(art_courses))


# empty lists
empty_list = []
empty_list = list()

# empty tuples
empty_tuple = ()
empty_tuple = tuple()

# empty sets
empty_set = {} #this is wrong, it is a dictionary
empty_set = set()