from second_algorithm import binary_search


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
    return a >= c and b <= d


def main():
    figure_count = int(input())
    if figure_count != 0:
        x_coordinates = []
        y_coordinates = []
        points = []
        for i in range(figure_count):
            x_coord, y_coord, x1_coord, y1_coord = map(int, input().split())
            points.append([x_coord, y_coord, x1_coord, y1_coord])
            x_coordinates.extend((x_coord, x1_coord))
            y_coordinates.extend((y_coord, y1_coord))
        x_coordinates = sorted(set(x_coordinates))
        max_x, min_x = max(x_coordinates), min(x_coordinates)
        y_coordinates = sorted(set(y_coordinates))
        max_y, min_y = max(y_coordinates), min(y_coordinates)
        tree_versions = []
        tree = []
        for i in range(len(y_coordinates) - 1):
            tree.append(Node(i, i))
        head = create_tree(tree)
        for i in range(len(x_coordinates)):
            for x in range(len(points)):
                if points[x][0] == x_coordinates[i]:
                    head = go_to_tree(head, binary_search(y_coordinates, points[x][1]),
                                      binary_search(y_coordinates, points[x][3])-1, 1)
                elif points[x][2] == x_coordinates[i]:
                    head = go_to_tree(head, binary_search(y_coordinates, points[x][1]),
                                      binary_search(y_coordinates, points[x][3])-1, -1)

            tree_versions.append(head)
        answer_array = []
        points_count = int(input())
        for i in range(points_count):
            x_coord, y_coord = map(int, input().split())
            if x_coord > max_x or x_coord < min_x or y_coord > max_y or y_coord < min_y:
                answer_array.append(0)
            else:
                answer_array.append(search_answer(tree_versions[binary_search(x_coordinates, x_coord)],
                                                  binary_search(y_coordinates, y_coord),
                                                  binary_search(y_coordinates, y_coord)))
        print(*answer_array)
    else:
        answer_array = []
        points_count = int(input())
        for i in range(points_count):
            x_coord, y_coord = map(int, input().split())
            answer_array.append(0)
        print(*answer_array)


if __name__ == '__main__':
    main()
