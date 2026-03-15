import numpy as np

data_type = [('name', 'S15'), ('class', int), ('roll', int)]

studDetails = [
    ('Zainab', 5, 32),
    ('Ibrahim', 5, 23),
    ('Musa', 5, 33),
    ('Ryan', 5, 46)]

stud = np.array(studDetails, dtype=data_type)
print("OriginalArray:")
print(stud)
print("Sorting with RollNumber")
print(np.sort(stud, order='roll'))