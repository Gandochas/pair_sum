def pair_sum(arr, k):
    seen_numbers = set()
    for number in arr:
        if (k - number) in seen_numbers:
            return True
        seen_numbers.add(number)
    return False


if __name__ == "__main__":
    k = int(input("Enter the value of k: "))
    arr = [1, 7, 13, 23, 3, 9, 4, 5, 15]
    print(pair_sum(arr, k))  # O(n^2)
