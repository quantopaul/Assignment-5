# Assignment 5
## Task 1
  1) Used variable "dict1" to store the keys and values
  
  2) Used variable "a" to take input from the user.
  
  3) Used if-else and "in" membership operator to find whether the name is on the list

### Code used
    dict1={"Raman": 90, "Baman": 100 , "Shay": 65}
    a=(input("Enter the name of the student: "))
    if a in dict1:
                print(f"{a}'s Marks = {dict1.get(a)}")
    else:
        print("No one by that name is on the list.")

  ### Output:
  1) If the name entered by the user is on the list:
     
         Enter the name of the student: Raman
         Raman's Marks = 90

  2) If the name entered by the user isn't on the list:

         Enter the name of the student: Amaan
         No one by that name is on the list.  

## Task 2
   1) "l" variable to store list of numbers from 1 to 10
   
   2) "sub" variable to store extracted list and that makes it easier to reverse
       the extracted one.

### Code used
    l=[1,2,3,4,5,6,7,8,9,10]
    sub=l[:5]
    print("Extracted list:",sub)
    sub.reverse()
    print("reverse of extracted list:",sub)

  ### Output:
      Extracted list: [1, 2, 3, 4, 5]
      reverse of extracted list: [5, 4, 3, 2, 1]
