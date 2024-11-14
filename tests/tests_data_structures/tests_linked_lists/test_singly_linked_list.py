from typing import Callable

import pytest

from data_structures.linked_lists import SinglyLinkedList


class TestSinglyLinkedList:
    @pytest.fixture
    def empty_linked_list(self) -> SinglyLinkedList:
        return SinglyLinkedList()

    @pytest.fixture
    def filled_linked_list(self) -> Callable:
        def _create_linked_list(values) -> SinglyLinkedList:
            linked_list = SinglyLinkedList()
            linked_list.append_many(values)
            return linked_list

        return _create_linked_list

    def test_insert_at_start(self, filled_linked_list) -> None:
        linked_list = filled_linked_list([10, 20])

        first_pos, first_value = 0, 100
        linked_list.insert(first_pos, first_value)

        assert linked_list.get(first_pos) == first_value
        assert linked_list.length == 3

    def test_insert_at_end(self, filled_linked_list) -> None:
        linked_list = filled_linked_list([10, 20])

        last_pos, last_value = 2, 400
        linked_list.insert(last_pos, last_value)

        assert linked_list.get(last_pos) == last_value
        assert linked_list.length == 3

    def test_insert_at_middle(self, filled_linked_list) -> None:
        linked_list = filled_linked_list([10, 20, 30])

        middle_pos, middle_value = 1, 50
        linked_list.insert(middle_pos, middle_value)

        assert linked_list.get(middle_pos) == middle_value
        assert linked_list.length == 4

    def test_insert_out_of_index(self, empty_linked_list) -> None:
        with pytest.raises(IndexError) as err_info:
            empty_linked_list.insert(99, 10)

    def test_pop_first_item(self, filled_linked_list) -> None:
        items: list[int] = [10, 20, 30, 40]
        linked_list = filled_linked_list(items)

        first_item = linked_list.pop(0)

        assert first_item.data == 10
        assert linked_list.length == len(items) - 1

    def test_pop_last_item(self, filled_linked_list) -> None:
        items: list[int] = [10, 20, 30, 40]
        linked_list = filled_linked_list(items)

        last_item = linked_list.pop(3)

        assert last_item.data == 40
        assert linked_list.length == len(items) - 1

    def test_pop_middle_item(self, filled_linked_list) -> None:
        items: list[int] = [10, 20, 30, 40]
        linked_list = filled_linked_list(items)

        last_item = linked_list.pop(2)

        assert last_item.data == 30
        assert linked_list.length == len(items) - 1

    def test_pop_from_empty_list(self, empty_linked_list) -> None:
        with pytest.raises(IndexError) as err_info:
            empty_linked_list.pop(0)

    def test_pop_list_with_index_out(self, filled_linked_list) -> None:
        items: list[int] = [10, 20, 30]
        linked_list = filled_linked_list(items)

        with pytest.raises(IndexError) as err_info:
            linked_list.pop(99)
        assert linked_list.length == len(items)

    def test_prepend(self, empty_linked_list) -> None:
        empty_linked_list.prepend(1)
        empty_linked_list.prepend(2)
        empty_linked_list.prepend(7)

        first_item = empty_linked_list.get(0)

        assert first_item == 7
        assert empty_linked_list.length == 3

    def test_append(self, empty_linked_list) -> None:
        empty_linked_list.append(5)
        empty_linked_list.append(1)
        empty_linked_list.append(9)

        last_item = empty_linked_list.get(2)

        assert last_item == 9
        assert empty_linked_list.length == 3

    def test_remove_exists(self, filled_linked_list) -> None:
        items: list[int] = [10, 20, 30, 20]
        linked_list = filled_linked_list(items)

        result = linked_list.remove(20)

        assert result is None
        assert linked_list.length == len(items) - 1
        assert linked_list.get(1) == 30

    def test_remove_not_exists(self, filled_linked_list) -> None:
        items: list[int] = [10, 20]
        linked_list = filled_linked_list(items)

        with pytest.raises(ValueError) as err_info:
            linked_list.remove(99)
        assert linked_list.length == len(items)

    def test_get_from_list(self, filled_linked_list) -> None:
        items: list[int] = [10, 20, 30]
        linked_list = filled_linked_list(items)

        middle_item_value = linked_list.get(1)

        assert middle_item_value == 20
        assert linked_list.length == len(items)

    def test_get_from_list_out_of_index(self, filled_linked_list) -> None:
        items: list[int] = [10, 20, 30]
        linked_list = filled_linked_list(items)

        with pytest.raises(IndexError) as err_info:
            linked_list.get(99)
        assert linked_list.length == len(items)

    def test_get_from_empty_list(self, empty_linked_list) -> None:
        with pytest.raises(IndexError) as err_info:
            empty_linked_list.get(99)

    def test_append_many(self, empty_linked_list) -> None:
        items: list[int] = [1, 2, 3, 4]
        empty_linked_list.append_many(items)

        assert empty_linked_list.length == len(items)
