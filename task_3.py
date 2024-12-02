class FlatIterator:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.cursor = 0
        self.result_list = []


    def flatten(self, element):
        if isinstance(element, list):
            for item in element:
                self.flatten(item)
        else:
            self.result_list.append(element)

    def __iter__(self):
        self.flatten(self.list_of_lists)
        return self

    def __next__(self):
        if self.cursor < len(self.result_list):
            item = self.result_list[self.cursor]
            self.cursor += 1
            return item
        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()

    lst = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for i in FlatIterator(lst):
        print(i)
