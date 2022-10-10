#testing environment
print('Hello World!')

#variables
#first_name = 'Benedek'
#UK_resident = True
#salary = 19000
#DOB = 2000
#travel = 23.5
#gross = salary + travel

"""first_name = 'Benedek'
last_name = 'Kovács'
salary = 19000
travel = 1.5
print(first_name)
print(last_name)
print(salary)
print(travel)"""

#taking in user data
#name
print('Good morning! Please enter your name: ')
name = input().split()
first_name, last_name = name[0], name[1]
print('Hello', first_name, last_name)
#dob
print('Enter DOB: ')
dob = input()
print('DOB: ', dob)
#course name
print('Enter course name: ')
c_n = input()
print('Course name: ', c_n)
#uk residency
print('Enter UK residency: ')
UKr = input()
print('UK residency: ', UKr)