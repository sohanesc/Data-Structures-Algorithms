def is_palindrome(s):
    # Helper function for recursion
    def helper(s, start, end):
        # Base case: if the start index is greater than or equal to the end index
        if start >= end:
            return True
        # Check characters at current indices
        if s[start] != s[end]:
            return False
        # Recursive call for the next pair of characters
        return helper(s, start + 1, end - 1)
    
    # Remove spaces and convert to lower case for accurate comparison
    s = s.replace(" ", "").lower()
    return helper(s, 0, len(s) - 1)

s = input("Enter a string: ")
if is_palindrome(s):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
