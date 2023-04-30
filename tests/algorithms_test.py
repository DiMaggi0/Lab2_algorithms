import time

#дополнительные функции и классы для корректной работы второго и третьего алгоритма
#binary_search - для второго алгоритма
#binary_search и все остальное - для третьего алгоритма
"""def binary_search(arr, target):
    first = 0
    last = len(arr) - 1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == target:
            return mid
        else:
            if arr[mid] > target:
                last = mid - 1
            else:
                first = mid + 1
    if first >= len(arr):
        return len(arr) - 1
    if first <= 0:
        return 0
    return first - 1


class Node:
    def __init__(self, left_ind, right_ind, left=None, right=None, value=0):
        self.right_ind = right_ind
        self.left_ind = left_ind
        self.right = right
        self.left = left
        self.value = value


def create_tree(tree):
    help_array = []
    while len(tree) != 1:
        if len(tree) % 2 == 0:
            for i in range(0, len(tree) - 1, 2):
                help_array.append(Node(tree[i].left_ind, tree[i + 1].right_ind, tree[i], tree[i + 1]))
        else:
            for i in range(0, len(tree) - 2, 2):
                help_array.append(Node(tree[i].left_ind, tree[i + 1].right_ind, tree[i], tree[i + 1]))
            help_array.append(Node(tree[len(tree) - 1].left_ind, tree[len(tree) - 1].right_ind, tree[len(tree) - 1]))
        tree = help_array[:]
        help_array.clear()
    return tree[0]


def go_to_tree(head, first, last, flag):
    if head is not None:
        if is_part_cover(head.left_ind, head.right_ind, first, last):
            if is_full_cover(head.left_ind, head.right_ind, first, last):
                return Node(head.left_ind, head.right_ind, head.left, head.right, head.value + flag)
            new = Node(head.left_ind, head.right_ind, head.left, head.right, head.value)
            new.left = go_to_tree(new.left, first, last, flag)
            new.right = go_to_tree(new.right, first, last, flag)
            return new
        if not is_part_cover(head.left_ind, head.right_ind, first, last):
            return head


def print_tree(head):
    if head is not None:
        print(head, head.left_ind, head.right_ind, head.value, head.left, head.right)
        print_tree(head.left)
        print_tree(head.right)


def search_answer(head, left_ind, right_ind):
    if head is not None:
        if is_part_cover(head.left_ind, head.right_ind, left_ind, right_ind):
            if is_full_cover(head.left_ind, head.right_ind, left_ind, right_ind):
                return head.value
            else:
                return head.value + search_answer(head.left, left_ind, right_ind) + search_answer(head.right, left_ind,
                                                                                                  right_ind)
        else:
            return 0
    return 0


def is_part_cover(a, b, c, d):
    return not (b < c or a > d)


def is_full_cover(a, b, c, d):
    return a >= c and b <= d"""


def main():
    p1, p2 = 99523, 98621
    times = []
    for count in [10, 50, 100, 300, 500, 750, 1000]:

#код для теста времени работы первого алгоритма
        """array_of_figures = []
        for i in range(count):
            for i in range(count):
                array_of_figures.append([(1+i) * 2, (1+i) * 2, (count-i) * 3, (count-i) * 3])
        answer_array = []
        start_time = time.time()
        for i in range(count//2):
            count_for_point = 0
            i = 1
            x_coord, y_coord = ((p1 + i) ** 3) % (count*2), ((p2 + i) ** 3) % (count*2)

            for j in range(len(array_of_figures)):
                if (array_of_figures[j][0] <= x_coord <= array_of_figures[j][2]
                        and array_of_figures[j][1] <= y_coord <= array_of_figures[j][3]):
                    count_for_point += 1
            answer_array.append(count_for_point)"""

#код для теста времени работы второго алгоритма
        """x_coordinates = []
        map_for_figures = []
        points = []
        for i in range(count):
            points.append([(1+i) * 2, (1+i) * 2, (count-i) * 3, (count-i) * 3])
            x_coordinates.extend(((1+i) * 2, (count-i) * 3))
        x_coordinates = sorted(set(x_coordinates))
        y_coordinates = x_coordinates[:]
        for j in range(len(y_coordinates) + 1):
            map_for_figures.append([0] * (len(x_coordinates) + 1))
        for k in range(len(points)):
            for i in range(binary_search(y_coordinates, points[k][1]), binary_search(y_coordinates, points[k][3]) + 1):
                for j in range(binary_search(x_coordinates, points[k][0]),
                               binary_search(x_coordinates, points[k][2]) + 1):
                    map_for_figures[i][j] += 1
        answer_array = []
        start_time = time.time()
        for i in range(count//2):
            first_coord, second_coord = ((p1 + i) ** 3) % (count*2), ((p2 + i) ** 3) % (count*2)
            answer_array.append(map_for_figures[binary_search(y_coordinates, second_coord)]
                                [binary_search(x_coordinates, first_coord)])"""


#код для теста времени работы третьего алгоритма
        """x_coordinates = []
        points = []
        for i in range(count):
            points.append([(1+i) * 2, (1+i) * 2, (count-i) * 3, (count-i) * 3])
            x_coordinates.extend(((1 + i) * 2, (count - i) * 3))

        x_coordinates = sorted(set(x_coordinates))
        y_coordinates = x_coordinates[:]
        max_x, min_x = max(x_coordinates), min(x_coordinates)
        max_y, min_y = max_x, min_x
        tree_versions = []
        tree = []
        for i in range(len(y_coordinates) - 1):
            tree.append(Node(i, i))
        head = create_tree(tree)
        for i in range(len(x_coordinates)):
            for x in range(len(points)):
                if points[x][0] == x_coordinates[i]:
                    head = go_to_tree(head, binary_search(y_coordinates, points[x][1]),
                                      binary_search(y_coordinates, points[x][3]) - 1, 1)
                elif points[x][2] == x_coordinates[i]:
                    head = go_to_tree(head, binary_search(y_coordinates, points[x][1]),
                                      binary_search(y_coordinates, points[x][3]) - 1, -1)

            tree_versions.append(head)
        answer_array = []
        start_time = time.time()
        for i in range(count//2):
            x_coord, y_coord = ((p1 + i) ** 3) % (count*2), ((p2 + i) ** 3) % (count*2)
            if x_coord > max_x or x_coord < min_x or y_coord > max_y or y_coord < min_y:
                answer_array.append(0)
            else:
                answer_array.append(search_answer(tree_versions[binary_search(x_coordinates, x_coord)],
                                                  binary_search(y_coordinates, y_coord),
                                                  binary_search(y_coordinates, y_coord)))"""




        #print(round(time.time() - start_time, 9))
        #times.append(round(time.time() - start_time, 9))


    print(times)


if __name__ == '__main__':
    main()
