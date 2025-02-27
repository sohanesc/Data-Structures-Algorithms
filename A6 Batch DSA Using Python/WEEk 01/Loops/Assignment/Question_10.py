"""
Q10. Ask two number from user that is start and end. Also start can be 
greater or smaller than the end number. Print from start to end. See the 
examples below.
 Example 1:
 Enter start = 5
Enter end = 10
 Output:
 5 6 7 8 9 10
 Example 2:
 Enter start = 9
 Enter end = 1
 Output:
 1 2 3 4 5 6 7 8 9 
Example 3:
 Enter start = 9
 Enter end = -3
 Output:-3 -2 -1 0 1 2 3 4 5 6 7 8 9
 Example 4:
 Enter start = -11
 Enter end = -6
 Output:-11 -10 -9 -8 -7 -6 
"""

start = int(input("Start Number: "))
end = int(input("End Number: "))

if start > end:
    temp = start
    start = end
    end = temp

i = start

while i <= end:
    print(i, end = " ")
    i += 1