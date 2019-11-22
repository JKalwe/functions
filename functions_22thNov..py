"""

uses the *def keyword, followed by parenthesis, then a colon:
    def marks the start of the function heaader
"""


# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# # print("Hello")
#
# def print_hello_word():
#     #body of the function
#     print("hello world")
#     print("I am OK")
#     print("sawa")
#
# # Calling the function
# print_hello_word()
# print_hello_word()
# print_hello_word()
# print_hello_word()


# create a random list

q = list(range(1,7))
print(q)
print(q[0])  #accesses the ist element
r = list(range(10,71))
print(r)
print(r[0])
s = list(range(1000,2000,100))
print(s)
print(s[0])
x = list(range(1,7))
x = list(range(1,7))

def gets_first_list_item(alist):
    print(alist[0])

gets_first_list_item(q)
gets_first_list_item(r)
gets_first_list_item(s)

    #() contains a paremeter (optional)


# create a fuction that passes my name
#
# def print_my_name(aname):
#     print(aname)
# print_my_name("Kalwe")
# print_my_name(1)
# print_my_name(22)
# print_my_name(123)
#
# # Add 2 numbers
#
# def add_two_numbers(a,b):
#     result = a + b
#     print(result)

# add_two_numbers(20,10)
# add_two_numbers(200,100)
# add_two_numbers(2230,123)
# add_two_numbers(1,2)

# Return function

def subtract_two_numbers(a,b):
    difference = a - b
    return difference
z = subtract_two_numbers(100,10)
print(z)

