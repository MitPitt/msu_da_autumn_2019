import re
import operator
from functools import reduce

def solution1(arr):
    return list(map(lambda i: int(re.sub('[^0-9]', '', i)[::-1]), arr))

def solution2(z):
    return list(map(lambda i: i[0]*i[1], list(z)))

def solution3(a):
    return list(filter(lambda i: i%6 in {0,2,5}, a))

def solution4(arr):
    return list(filter(lambda i: i, arr))

def solution5(rooms):
    list(map(lambda i: operator.setitem(i, "square", i["width"]*i["length"]), rooms))
    return rooms

def solution6(rooms):
    q = list(map(dict,rooms))
    list(map(lambda i: operator.setitem(i, "square", i["width"]*i["length"]), q))
    return q

def solution7(arr):
    return reduce(set.intersection, arr)

def solution8(arr):
    return reduce(lambda i,j: operator.setitem(i, j, 1 if i.get(j)==None else i[j]+1) or i, arr, dict())

def solution9(students):
    return list(map(lambda j: j['name'], list(filter(lambda i: i['gpa']>4.5, students))))

def solution10(arr):
    return list(filter(lambda i: sum(map(int, i[0::2]))==sum(map(int, i[1::2])), arr))

solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}



if __name__ == "__main__":
    print(solution1(['12', '25.6', '84,02', '  69-91']))
    print(solution2(zip(range(2, 5), range(3, 9, 2))))
    print(solution3(range(20)))
    print(solution4(['', 25, None, 'python',
                     0.0, [], ('msu', '1755-01-25')]))
    rooms = [
    {"name": "комната1", "width": 2, "length": 4},
    {"name": "комната2", "width": 2.5, "length": 5.6},
    {"name": "кухня", "width": 3.5, "length": 4},
    {"name": "туалет", "width": 1.5, "length": 1.5},
    ]
    print(solution5(rooms))
    rooms1 = [
    {"name": "комната1", "width": 2, "length": 4},
    {"name": "комната2", "width": 2.5, "length": 5.6},
    {"name": "кухня", "width": 3.5, "length": 4},
    {"name": "туалет", "width": 1.5, "length": 1.5},
    ]
    print(solution6(rooms1))
    print(rooms1)
    print(solution7([{1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}, {3, 4, 5, 6, 7}]))
    print(solution8([1, 2, 1, 1, 3, 2, 3, 2, 4, 2, 4]))
    students = [
    {'name': 'Alina', 'gpa': 4.57},
    {'name': 'Sergey', 'gpa': 5.0},
    {'name': 'Nastya', 'gpa': 4.21},
    {'name': 'Valya', 'gpa': 4.72},
    {'name': 'Anton', 'gpa': 4.32},
    ]
    print(solution9(students))
    print(solution10(['165033', '477329', '631811', '478117', '475145', '238018', '917764', '394286']))
