x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
def change_val(lst):
    for x in lst:
        x[1][0] = 15
    return lst

print(x)


# Change the last_name of the first student from 'Jordan' to 'Bryant'
def students(lst):
    for x in lst:
        students[0]['last_name'] = 'Bryant'
    return lst

print(students)

# In the sports_directory, change 'Messi' to 'Andres'
def sports(lst):
    for x in lst:
        sports['soccer'][0] = 'Andres'
    return lst

print(sports)
# Change the value 20 in z to 30