def binary_search(arr, target):
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


def main():
    figure_count = int(input())
    x_coordinates = []
    y_coordinates = []
    map_for_figures = []
    points = []
    for i in range(figure_count):
        x_coord, y_coord, x1_coord, y1_coord = map(int, input().split())
        points.append([x_coord, y_coord, x1_coord, y1_coord])
        x_coordinates.extend((x_coord, x1_coord))
        y_coordinates.extend((y_coord, y1_coord))
    x_coordinates = sorted(set(x_coordinates))
    y_coordinates = sorted(set(y_coordinates))
    for j in range(len(y_coordinates) + 1):
        map_for_figures.append([0] * (len(x_coordinates) + 1))
    for k in range(len(points)):
        for i in range(binary_search(y_coordinates, points[k][1]), binary_search(y_coordinates, points[k][3]) + 1):
            for j in range(binary_search(x_coordinates, points[k][0]), binary_search(x_coordinates, points[k][2]) + 1):
                map_for_figures[i][j] += 1
    answer_array = []
    points_count = int(input())
    for i in range(points_count):
        first_coord, second_coord = map(int, input().split())
        answer_array.append(map_for_figures[binary_search(y_coordinates, second_coord)]
                            [binary_search(x_coordinates, first_coord)])
    print(*answer_array)


if __name__ == '__main__':
    main()
