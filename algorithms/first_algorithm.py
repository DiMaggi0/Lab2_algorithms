def main():
    figure_count = int(input())
    array_of_figures = []
    for i in range(figure_count):
        array_of_figures.append([int(i) for i in input().split()])
    point_count = int(input())
    answer_array = []
    for i in range(point_count):
        count_for_point = 0
        x_coord, y_coord = map(int, input().split())
        for i in range(len(array_of_figures)):
            if(array_of_figures[i][0] <= x_coord <= array_of_figures[i][2]
                    and array_of_figures[i][1] <= y_coord <= array_of_figures[i][3]):
                count_for_point += 1
        answer_array.append(count_for_point)
    print(*answer_array)


if __name__ == '__main__':
    main()




