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