s1 = input("Enter String1: ")
s2 = input("Enter String2: ")

if s1 == s2:
    print("Both the strings are same")

elif s2 in s1:
    print(s2, "is a substring of", s1)

else:
    print("String2 is not a substring of String1")