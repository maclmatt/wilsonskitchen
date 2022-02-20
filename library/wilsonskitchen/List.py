from constants import LOGGER

class List():
    def __init__(self):
        self._list = []
        self.length = 0

    def add_item(self, item) -> None:
        try:
            # adds item to end of list
            # increases self.length by 1
            self._list.append(item)
            self.length += 1
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Item could not be added to list.") from err

    def sort_switch(self, numbers, low, high) -> int:
        try:
            pivot = numbers[high]
            item = low - 1
            for i in range(low, high):
                # moves item around the pivot
                # depending on whether it is larger or smaller
                if numbers[i] <= pivot:
                    item = item + 1
                    (numbers[item], numbers[i]) = (numbers[i], numbers[item])
            (numbers[item + 1], numbers[high]) = (numbers[high], numbers[item + 1])
            return item + 1
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Switch of items could not be performed.") from err

    def quick_sort(self, numbers, low, high) -> None:
        try:
            # checks that low is less than high
            if low < high:
                # calls sort_switch to get pivot and move items around the pivot
                pivot = self.sort_switch(numbers, low, high)
                # calls quick_sort function to get next pivots
                self.quick_sort(numbers, low, pivot - 1)
                self.quick_sort(numbers, pivot + 1, high)
            # stops recursion when all items have been made pivot
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("List could not be sorted using quick sort.") from err

    def sort_list(self) -> None:
        try:
            # calls quick_sort
            self.quick_sort(self._list, 0, (self.length)-1)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("List could not be sorted.") from err

    def return_list(self) -> list:
        try:
            return self._list
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("List could not be returned.") from err

    def return_lowest(self) -> str or int:
        try:
            # calls sort_list
            # returns first item on list
            self.sort_list()
            return self._list[0]
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Lowest list item could not be returned.") from err

    def wipe(self) -> None:
        try:
            # empties self.list
            # makes self.length 0
            self._list = []
            self.length = 0
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("List could not be wiped.") from err
