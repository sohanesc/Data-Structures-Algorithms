"""
Q6. Print all the numbers divisible by 2, 3 and 5 from start to end. Ask start 
and end numbers from the user.
 Example 1:
 Enter start = 5
 Enter end = 177
 Output:
 30 60 90 120 150
 Example 2:
 Enter start = 876
 Enter end = 2000
 Output:
 900 930 960 990 1020 1050 1080 1110 1140 1170 1200 1230 1260 1290 1320 1350 1380 
1410 1440 1470 1500 1530 1560 1590 1620 1650 1680 1710 1740 1770 1800 1830 1860 1890 
1920 1950 1980
"""

start = int(input("Start number = "))
end = int(input("End number = "))

i = start

while i <= end:
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
        print(i, end = " ")

    i += 1