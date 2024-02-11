#Here you prompt the user to enter the following details
bookID= int(input("Enter Book ID : "))
dueDate= int(input("Enter Due Date : "))
returnDate= int(input("Enter Return Date : "))

daysOVERDUE= returnDate-dueDate
#if--else statement to determine fine rate
if daysOVERDUE <= 7:
    fineRATE=20
elif daysOVERDUE >= 8 and daysOVERDUE >= 14:
    fineRATE=50
elif daysOVERDUE >= 15:
    fineRATE=100
#using the finerate obtained to calculate the fineamount
fineAMOUNT = fineRATE * daysOVERDUE
print("\n")
print("Book ID : ",bookID)
print("Due Date : ",dueDate)
print("Return Date : ",returnDate)
print("Days Overdue : ",daysOVERDUE)
print("Fine Rate : ",fineRATE)
print("Fine Amount : Ksh.",fineAMOUNT)