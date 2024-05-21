from pair_sum import pair_sum
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_pair_sum():
    """Тестирование функции проверки пары чисел с заданной суммой."""
    arr = [1, 7, 13, 23, 3, 9, 4, 5, 15]

    assert pair_sum(arr, 10) == True, "Test case 1 failed"
    assert pair_sum(arr, 30) == False, "Test case 2 failed"
    assert pair_sum(arr, 28) == True, "Test case 3 failed"
    assert pair_sum(arr, 17) == True, "Test case 4 failed"
    assert pair_sum(arr, 8) == True, "Test case 5 failed"


if __name__ == "__main__":
    test_pair_sum()
    print("Все тесты пройдены успешно!")
