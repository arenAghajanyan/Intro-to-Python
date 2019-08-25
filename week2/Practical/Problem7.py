str1="How are you John?"
name="|My name|"
str2=str1.replace("John", name)
print(str2)
str2=str1[0:12]+name+str1[-1]
print(str2)