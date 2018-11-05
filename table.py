file_name = 'sales.csv'
title_list = ['id', 'title', 'price', 'month', 'day', 'year']
max_length_column = []


def main():
    table = get_table_from_file(file_name)
    print_table(table, title_list)


def max_length(table):
    for column in range(len(title_list)):
        temp = 0
        for row in range(len(table)):
            if len(str(table[row][column])) > temp:
                temp = len(str(table[row][column]))
                temp = int(temp)
        max_length_column.append(temp)
    return max_length_column


def sum_length_table(max_length_column):
    sum_length = len(title_list)*2
    for i in range(len(max_length_column)):
        sum_length += max_length_column[i]
    return sum_length


def print_top_border(sum_length):
    print('/', ('-'*(sum_length-3)), '\\')


def print_middle_border(sum_length):
    print('|', ('-'*(sum_length-3)), '|')


def print_bottom_border(sum_length):
    print('\\', ('-'*(sum_length-3)), '/')


def print_table(table, title_list):
    print('Its work')
    temp_table = table.copy()
    temp_table.append(title_list)
    max_length_column = max_length(temp_table)
    sum_length = sum_length_table(max_length_column)
    print_top_border(sum_length)
    print_columns_title(title_list)

    print_items_table(table, sum_length)
    print_bottom_border(sum_length)


def print_columns_title(title_list):
    for col_i in range(len(title_list)):
        col = title_list[col_i]
        width = max_length_column[col_i]
        print('|', col.center(width),  end='')
    print('|')


def print_items_table(table, sum_length):
    for row in table:
        print_middle_border(sum_length)
        for col_i in range(len(row)):
            col = row[col_i]
            width = max_length_column[col_i]
            print('|', col.center(width),  end='')
        print('|')


def get_table_from_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(';')for element in lines]
    return table


main()
