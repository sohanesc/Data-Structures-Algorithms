'''
number = 1

int f(number, a[]) {
    cout = 0

    for (i = 0, i < number, i++) {  <--- O(n) itterate through the entire array
        if (arr[i] == number)     <--- O(1) check if the element is equal to the number
            cout++                 <--- O(1) increment the count
    }
    return cout                    <--- O(1) return the count
}

O(n) + O(1) + O(1) + O(1) = O(n)

ex: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output: it takes 10 operations to find the number 10
estimated time: 10 * 1 = 10 seconds
for 1000 elements, it takes 1000 seconds (16.6 minutes) 😯🙁

Hashing:
    prestoring & fetching the data in O(1) time complexity


'''
import sys

# Redirect input from input.txt and output to output.txt
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    # Determine the range of numbers in the array
    max_value = max(arr) if arr else 0
    hash = [0] * (max_value + 1)

    # Precompute
    for i in range(n):
        hash[arr[i]] += 1

    q = int(input())
    for _ in range(q):
        number = int(input())
        # Fetch
        if number <= max_value:
            print(hash[number])
        else:
            print(0)

if __name__ == "__main__":
    main()
