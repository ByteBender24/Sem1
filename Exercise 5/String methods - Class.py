#Upper,lower,capitalize,casefold:
str = "this is string example....wow!!!";
print("--------------------UPPER--------------------")
print ("str.upper() : ", str.upper())
b=str.upper()
print("--------------------lower--------------------")
print ("b.lower() : ", b.lower())
print("--------------------Capitalize--------------------")
print ("str.capitalize() : ", str.capitalize())
print("--------------------Casefold--------------------")
print ("str.casefold() : ", b.casefold())
c=b.casefold()

print("--------------------count(substring,start,end)---------")
sub = "i";
print ("str.count(sub, 4, 40) : ", str.count(sub, 4, 40))
sub = "wow";
print ("str.count(sub) : ", str.count(sub))
print("--------------------find(substring,start,end)--------------------")
str2 = "exam";
print (str.find(str2))
print (str.find(str2, 10,15))
print (str.find(str2, 40))
print("--------------------strip--------------------")
str1 = "0000000this is string example....wow!!!0000000";
print (str1.strip( '0' ))
print("--------------------rjust and ljust(length of returned string, character to fill missing space)--------------------")
print (str.rjust(50, '*'))
print (str.ljust(50, '$'))


print("--------------------index--------------------")
print (str.index(str2))
print (str.index(str2, 10))
# print (str.index(str2, 40))
print("--------------------isalnum--------------------")
str3='exam3122'
print(str2.isalnum())
print(str.isalnum())
print(str3.isalnum())
print("--------------------isalpha--------------------")
str3='exam3122'
print(str2.isalpha())
print(str.isalpha())
print(str3.isalpha())
print("--------------------isdecimal--------------------")
str4='312217121001'
print(str2.isdecimal())
print(str.isdecimal())
print(str4.isdecimal())
print("--------------------replace--------------------")
str5 = "this is string example....wow!!! this is really string"
print (str5.replace("is", "was"))
print (str5.replace("is", "was", 3))#only three occurances
print("--------------------startswith--------------------")
print (str.startswith( 'this' ))
print (str.startswith( 'is', 2, 4 ))
print (str.startswith( 'this', 2, 4 ))
print("--------------------endswith--------------------")
suffix = "wow!!!";
print (str.endswith(suffix))
print (str.endswith(suffix,20))

suffix1 = "is";
print (str.endswith(suffix1, 2, 4))
print (str.endswith(suffix1, 2, 6))

print("--------------------partition--------------------")
txt = "I could eat apples apples all day"
x = txt.partition("apples")
print(x)


#String formatting

name="hannah"
age=8
print("name=%s and age =%d" %(name,age))
s="name=%s and age =%5d" %(name,age)
print(s)

person1="Tiana"
person2="Julina"
greeting = "hello {}!".format(person1)
print (greeting)
greeting = "hello {0} and {1}!".format(person1,person2)
print (greeting)
print("hello {0} and {1}!".format(person1,person2))
