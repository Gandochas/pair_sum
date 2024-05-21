from pair_sum import pair_sum


def test_pair_sum():
    """Тестирование функции проверки пары чисел с заданной суммой."""
    arr = [1, 7, 13, 23, 3, 9, 4, 5, 15]

    assert pair_sum(arr, 10) == True, "Test case 1 failed"
    assert pair_sum(arr, 29) == False, "Test case 2 failed"
    assert pair_sum(arr, 28) == True, "Test case 3 failed"
    assert pair_sum(arr, 17) == True, "Test case 4 failed"
    assert pair_sum(arr, 2) == True, "Test case 5 failed"


if __name__ == "__main__":
    test_pair_sum()
    print("Все тесты пройдены успешно!")
