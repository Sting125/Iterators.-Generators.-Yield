import types


# Доработанный класс FlatIterator
class FlatIterator:

    def __init__(self, list_of_list):
        # Принимаем список списков и создаём итератор для внешнего списка
        self.list_of_lists = list_of_list
        self.outer_iter = iter(self.list_of_lists)
        self.inner_iter = iter([])  # Начинаем с пустого итератора для вложенных списков

    def __iter__(self):
        return self

    def __next__(self):
        # Попробуем взять следующий элемент из текущего внутреннего итератора
        try:
            return next(self.inner_iter)
        except StopIteration:
            # Если текущий внутренний итератор завершён, переходим к следующему списку
            self.inner_iter = iter(next(self.outer_iter))  # Обновляем внутренний итератор новым подсписком
            return next(self.inner_iter)  # Возвращаем первый элемент нового списка


# Функция тестирования итератора
def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        print(f"Из итератора: {flat_iterator_item}, Ожидалось: {check_item}")
        assert flat_iterator_item == check_item

    flat_list = list(FlatIterator(list_of_lists_1))
    print(f"Полный список из итератора: {flat_list}")
    assert flat_list == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


# Доработанный генератор flat_generator
def flat_generator(list_of_lists):
    # Используем вложенный цикл для прохода по элементам
    for sublist in list_of_lists:
        for item in sublist:
            yield item


# Функция тестирования генератора
def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        print(f"Из генератора: {flat_iterator_item}, Ожидалось: {check_item}")
        assert flat_iterator_item == check_item

    flat_list = list(flat_generator(list_of_lists_1))
    print(f"Полный список из генератора: {flat_list}")
    assert flat_list == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    print("Тестирование итератора:")
    test_1()

    print("\nТестирование генератора:")
    test_2()
