dict1={"Raman": 90, "Baman": 100 , "Shay": 65}
a=(input("Enter the name of the student: "))
if a in dict1:
                print(f"{a}'s Marks = {dict1.get(a)}")
else:
        print("No one by that name is on the list.")
