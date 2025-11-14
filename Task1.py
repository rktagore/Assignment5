students = {'Alice':85.5,'Carol':93.9}
find = input("Enter the student's name:")
flag=0
for key in students.keys():
    if key == find:
        flag=1
        print(f"{key}'s marks:{students[key]}")
if(flag==0):
    print(f"{find} student marks not found")
