from constants import LOGGER
from ast import Index
from multiprocessing.dummy import Value


class List():
    def __init__(self):
        self._list = []
        self.length = 0

    def add_item(self, item) -> None:
        try:
            list = self._list
            list.append(item)   # adds item to end of list
            self.length += 1
        except BaseException as err:
            LOGGER.error(err)   #logs error in log file
            raise RuntimeError("Item could not be added to list.") from err

    def sort_switch(self, numbers, low, high) -> Index:
        try:
            pivot = numbers[high]
            item = low - 1
            for i in range(low, high):
                if numbers[i] <= pivot:
                    item = item + 1
                    (numbers[item], numbers[i]) = (numbers[i], numbers[item])
            (numbers[item + 1], numbers[high]) = (numbers[high], numbers[item + 1])
            return item + 1
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Switch of items could not be performed.") from err

    def quick_sort(self, numbers, low, high) -> None:
        try:
            if low < high:
                pivot = self.list_sort_switch(numbers, low, high)
                self.list_quick_sort(numbers, low, pivot-1)
                self.list_quick_sort(numbers, pivot + 1, high)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("List could not be sorted using quick sort.") from err

    def sort_list(self) -> None:
        try:
            self.list_quick_sort(self._list, 0, (self.length)-1)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("List could not be sorted.") from err

    def return_list(self) -> list:
        try:
            return self._list
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("List could not be returned.") from err

    def return_lowest(self) -> Value:
        try:
            self.sort_list()
            return self._list[0]
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Lowest list item could not be returned.") from err

    def wipe(self) -> None:
        try:
            self._list = []
            self.length = 0
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("List could not be wiped.") from err
