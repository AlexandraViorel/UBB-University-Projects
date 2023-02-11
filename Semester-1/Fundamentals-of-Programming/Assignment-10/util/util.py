class MyContainer:
    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self._dictionary = dictionary
        self.position = None

    def __setitem__(self, key, value):
        self._dictionary[key] = value

    def __getitem__(self, key):
        return self._dictionary[key]

    def __delitem__(self, key):
        del self._dictionary[key]

    def __len__(self):
        return len(self._dictionary)

    def list(self):
        return list(self._dictionary.values())

    def __iter__(self):
        self.position = 0
        return self.position

    def __next__(self):
        if self.position == len(list(self._dictionary.keys())):
            raise StopIteration()
        self.position += 1
        return self._dictionary[list(self._dictionary.keys())[self.position - 1]]

    def add(self, key, element):
        self._dictionary[key] = element

    def remove(self, key):
        del self._dictionary[key]

    def update(self, key, new_element):
        self._dictionary[key] = new_element


def my_shell_sort(list_to_be_sorted, comparison_function):
    """
        This sorting method is a generalized version of the insertion sort. It sorts the elements using intervals
    between them. The interval is first the length of the list div 2, and it reduces until it becomes 0 (aka the moment
    when the list is sorted).
    for example:
    LIST = [4, 6, 2, 8, 1, 5], ascending sort
    1. The first gap is 3, so the pairs of elements that are going to be compared are:
            - base element: 8 <-> 4 => the list remains the same
            - base element: 1 <-> 5 => [4, 1, 2, 8, 6, 5]
            - base element: 6 <-> 2 => the list remains the same
    so after the first interval between elements the list becomes: [4, 1, 2, 8, 6, 5].
    2. The second gap is 3 div 2 = 1, so the pairs of elements that are going to be compared are:
            - base element: 1 <-> 4 => [1, 4, 2, 8, 6, 5]
            - base element: 2 <-> 4 => [1, 2, 4, 8, 6, 5]
            - base element: 8 <-> 4 => the list remains the same
            - base element: 6 <-> 8 => [1, 2, 4, 6, 8, 5]
            - base element: 5 <-> first with 8 => [1, 2, 4, 6, 8, 8], then with 6 => [1, 2, 4, 6, 6, 8] and then we put
            the base element on the correct position (3) => [1, 2, 4, 5, 6, 8]
    3. The gap becomes 0 => we stop the sorting, the list is sorted ascending.


    :param list_to_be_sorted: the list that is going to be sorted
    :param comparison_function: this function is used to determine the order between two elements
    :return: the sorted list
    """
    interval_between_elements = len(list_to_be_sorted) // 2
    while interval_between_elements > 0:
        for i in range(interval_between_elements, len(list_to_be_sorted)):
            base_element_for_comparison = list_to_be_sorted[i]
            j = i
            while j >= interval_between_elements and comparison_function(list_to_be_sorted[j - interval_between_elements], base_element_for_comparison):
                list_to_be_sorted[j] = list_to_be_sorted[j - interval_between_elements]
                j -= interval_between_elements
            list_to_be_sorted[j] = base_element_for_comparison
        interval_between_elements //= 2
    return list_to_be_sorted


def my_filter(list_to_be_filtered, filter_function):
    """
    :param list_to_be_filtered: the list that is going to be filtered
    :param filter_function: this function is used to determine which elements pass the filter
    :return: the filtered list
    """
    filtered_list = []
    for element in list_to_be_filtered:
        if filter_function(element):
            filtered_list.append(element)
    return filtered_list
