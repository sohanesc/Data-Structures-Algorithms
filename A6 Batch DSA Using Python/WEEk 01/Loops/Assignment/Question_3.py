"""
 Q3.  Ask a start number and end number from user. Calculate the total sum 
of all the numbers from start to end. 
Example 1:
 Enter start = 5
 Enter end = 10
Output:
 45
 Example 1:
 Enter start = 99
 Enter end = 103
 Output:
 505
 """

start = int(input("Start number: "))
end = int(input("End number: "))

sum = 0
i = start

while i <= end:
    sum += i
    i += 1

print(sum)