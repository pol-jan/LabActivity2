"""Average of grades"""
pr=int(input('Enter Prelims grade: '))
mt=int(input('Enter Midterm grade: '))
sf=int(input('Enter Semifinals grade: '))
fn=int(input('Enter Finals grade: '))
avg=(pr+mt+sf+fn)/4
print('Average =',str(avg))
if(avg>=75):
    print("PASSED")
else:
    print("FAILED")
if(avg>=99 and avg<=100):
    print("Grade: A")
elif(avg>=90 and avg<=98):
    print("Grade: B")
elif(avg>=80 and avg<=89):
    print("Grade: C")
elif(avg>=71 and avg<=79):
    print("Grade: D")
elif(avg>=61 and avg<=70):
    print("Grade: E")
else: 
    print("Grade: F")