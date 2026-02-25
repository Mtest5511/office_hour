from tkinter.font import names


print("Hello World")

age =25
year= 2026 

"My name is John and I am 25 years old and the year is 2026"

#### operators (+ - * / % ** //)

print(age + 5) # addition
print(age - 5) # subtraction
print(age * 3) # multiplication
print(age / 4) # division
print(age % 4) # modulus
print(age ** 2) # exponentiation

# String - single quote vs double quote

name = "John"
other_name = 'Jane'
print(name)
print(other_name)

sentence = "This is a sentence."
print(sentence)

### List###
John_Grades_inSchool = ["A", "D", "C", "D-", "F", "D+"]
John_Grades_inSchool.append("B+")
print(John_Grades_inSchool)

### Dictionary ###
Student= {
    "name": "Quincy",
    "age": 25,
    "favorite_activity" : "reading",
    "favorite_soda" : "Coca Cola",
    "Grades" : ["A", "A+", "A+"]
}
print(Student)
print(Student["Grades"])

#### For Loop ###
for each_element in range(1,1): print(each_element)

###Shorthand for loop

for i in range (1,11) :
    print(i)

for eachGrade in John_Grades_inSchool:
    print(eachGrade)
for applecomicsBoomerang in range(1,11):
    print(applecomicsBoomerang)
           
for eachelement in range(1,11) : 
    if eachelement % 2 == 0:
        print(eachelement)

for i in range(1,21) :
    if i % 2 == 0:
        print(i)  

numbers = [1,57,85,32,0]
total = 0
for n in numbers:
    total += n
print(total)

namelength = ["Coltoon","Qasmi","Mesgaw","Vasantha","Selam","Hima","Monika","Yamrot","Lucy"]
for name in namelength:
    if len(name) > 5:
        print(name)

for num in numbers:
    if num % 2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")
