# Given a list of heterogeneous elements. Write a Python script to remove all the non-int values from the list.

mixed_list = [1, "a", 3.14, 2, "hello", 5]
int_list = [x for x in mixed_list if isinstance(x, int)]
print("List with only integers:", int_list)
