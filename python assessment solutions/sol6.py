r = input("Enter roll number: ")
n = input("Enter student name: ")
s = input("Enter standard: ")

print("Enter marks of 4 subjects")

m = []

for i in range(4):
    x = float(input("Enter marks: "))
    m.append(x)

p = sum(m) / 4

if p >= 80:
    g = "A"
elif p >= 60:
    g = "B"
elif p >= 40:
    g = "C"
else:
    g = "F"

print("\nStudent Details")
print("Roll Number:", r)
print("Name:", n)
print("Standard:", s)
print("Percentage:", p)
print("Grade:", g)

if g != "F":
    print("Student is promoted")
else:
    print("Student is not promoted")