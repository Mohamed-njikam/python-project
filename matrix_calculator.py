import copy
import math


def create_matrix(dimensions):
    """Asks to enter the dimensions of a matrix."""
    elements_list = []
    for _row in range(int(dimensions[0])):
        elements = input().split()
        elements_list.append(elements)
    return elements_list


def get_one_matrix():
    matrix_size = input("Enter matrix size: ").split()

    print("Enter matrix:")
    matrix = create_matrix(matrix_size)

    return [matrix_size, matrix]


def get_two_matrices():
    matrix_size_a = input("Enter size of first matrix: ").split()
    print("Enter first matrix:")
    matrix_a = create_matrix(matrix_size_a)

    matrix_a_info = [matrix_size_a, matrix_a]

    matrix_size_b = input("Enter size of second matrix: ").split()
    print("Enter second matrix:")
    matrix_b = create_matrix(matrix_size_b)

    matrix_b_info = [matrix_size_b, matrix_b]

    return [matrix_a_info, matrix_b_info]


def create_matrix_result(dimensions):
    """Creates a matrix with all elements as 0."""
    elements_list = []
    for _row in range(int(dimensions[0])):
        elements = [0 for _n in range(int(dimensions[1]))]
        elements_list.append(elements)
    return elements_list


def add_matrices(dimensions, element_list_a, element_list_b):
    """Returns the sum of two matrices. Dimensions are the dimensions of the first matrix. Element_list_a
    is the list of elements of the first  matrix. Element_list_b is the list of elements of the second matrix."""
    results = []
    for row_index in range(int(dimensions[0])):
        result_list = []
        results.append(result_list)

        for element_index in range(int(dimensions[1])):
            result = float(element_list_a[row_index][element_index]) + float(element_list_b[row_index][element_index])
            result_list.append(result)
    return results


def multiply_constant(element_list, constant_):
    """Multiplies a matrix by a constant. Element_list represents the matrix and constant represents the constant
    to be multiplied by the matrix."""
    new_matrix = []
    for row in element_list:
        result = []
        new_matrix.append(result)
        for element in row:
            result.append(float(element) * float(constant_))
    return new_matrix


def multiply_by_matrix(matrix_a, matrix_b, size_a, size_b):
    """Multiplies two matrices. matrix_a is a list of elements of the first matrix. matrix_b is the list of elements
    of the second matrix. size_a and size_b are a list of dimensions of the first and second matrix respectively."""
    if size_a[1] == size_b[0]:
        result = create_matrix_result([int(size_a[0]), int(size_b[1])])

        for matrix_a_row in range(int(size_a[0])):
            for matrix_b_column in range(int(size_b[1])):
                for matrix_b_row in range(int(size_b[0])):
                    result[matrix_a_row][matrix_b_column] += float(matrix_a[matrix_a_row][matrix_b_row]) \
                                                             * float(matrix_b[matrix_b_row][matrix_b_column])
        return result
    else:
        return "The operation cannot be performed."


def transpose_through_main(original_matrix, original_size):
    transposed_matrix = create_matrix_result([original_size[1], original_size[0]])

    # go through each row
    for original_row in range(int(original_size[0])):
        # go through each element
        for original_element in range(int(original_size[1])):
            transposed_matrix[original_row][original_element] = original_matrix[original_element][original_row]
    return transposed_matrix


def transpose_through_second(original_matrix, original_size):
    original_matrix.reverse()
    for individual_row in original_matrix:
        individual_row.reverse()

    return transpose_through_main(original_matrix, original_size)


def transpose_though_vertical(original_matrix):
    for individual_row in original_matrix:
        individual_row.reverse()
    return original_matrix


def transpose_through_horizontal(original_matrix):
    original_matrix.reverse()
    return original_matrix


def get_determinant(matrix_, dimensions):
    """Calculates the determinant of a matrix given its dimensions and the matrix itself."""
    # Base case, if the square matrix is of dimensions 1X1
    if int(dimensions[0]) == int(dimensions[1]) == 1:
        return int(matrix_[0][0])

    # Base case, if the square matrix is of dimensions 2X2
    elif int(dimensions[0]) == int(dimensions[1]) == 2:
        return (float(matrix_[0][0]) * float(matrix_[1][1])) - (float(matrix_[0][1]) * float(matrix_[1][0]))

    # Recursive case if square matrix is not 2X2
    else:
        total = 0
        # list of indexes for the first row of the matrix
        first_row_indexes = list(range(len(matrix_[0])))

        # create a sub_matrix for each item of the first row of the matrix
        for first_row_index in first_row_indexes:
            sub_matrix = copy.deepcopy(matrix_)
            del sub_matrix[0]
            for n in range(len(sub_matrix)):
                del sub_matrix[n][first_row_index]

            if first_row_index % 2 == 0:
                sign = +1
                total += sign * float(matrix_[0][first_row_index]) * get_determinant(sub_matrix, [len(sub_matrix),
                                                                                                  len(sub_matrix[0])])
            else:
                sign = -1
                total += sign * float(matrix_[0][first_row_index]) * get_determinant(sub_matrix, [len(sub_matrix),
                                                                                                  len(sub_matrix[0])])

        return total


def get_cofactors_matrix(matrix):
    """Return a new matrix with the minors of each elements as elements"""

    is_positive = True

    new_matrix = []
    # create a list of indexes to reference each row of the matrix
    matrix_row_indexes = list(range(len(matrix)))

    # for each index in the list of row indexes
    for matrix_row_index in matrix_row_indexes:
        # create a new list
        new_row_list = []

        # create a list of indexes
        row = matrix[matrix_row_index]
        row_indexes = list(range(len(row)))

        # for each index in each row
        for row_index in row_indexes:

            # create the sub matrix
            comatrix = copy.deepcopy(matrix)

            # delete the row corresponding to the index in question
            del comatrix[matrix_row_index]

            # for each row in the sub matrix
            for nn in comatrix:
                # delete the element with the index in question
                del nn[row_index]

            # show the determinant of the submatrix
            comatrix_determinant_cof = math.pow(-1, matrix_row_index + row_index)\
                                       * get_determinant(comatrix, [len(comatrix), len(comatrix[0])])

            # store each determinant in a list
            new_row_list.append(comatrix_determinant_cof)

        # store each list of determinants in a list
        new_matrix.append(new_row_list)

    return new_matrix


def get_inverse(matrix):
    det_matrix = get_determinant(matrix, [len(matrix), len(matrix[0])])
    cof_matrix = get_cofactors_matrix(matrix)
    adjoint = transpose_through_main(cof_matrix, [len(cof_matrix), len(cof_matrix[0])])
    try:
        inverse_matrix = multiply_constant(adjoint, 1 / det_matrix)
    except ZeroDivisionError:
        print("This matrix doesn't have an inverse.")
    else:
        print("The result is:")
        for i_row in inverse_matrix:
            print(*i_row)


while True:
    print("\n1. Add matrices", "2. Multiply matrix by a constant", "3. Multiply matrices",
          "4. Transpose matrix", "5. Calculate a determinant ", "6. Inverse matrix", "0. Exit", sep="\n")
    choice = input("Your choice: ")

    if choice in ["1", "Add matrices"]:
        matrix_info = get_two_matrices()
        dimensions_a = matrix_info[0][0]
        dimensions_b = matrix_info[1][0]
        element_list_a = matrix_info[0][1]
        element_list_b = matrix_info[1][1]

        if dimensions_a == dimensions_b:
            result_ = add_matrices(dimensions_a, element_list_a, element_list_b)
            print("The result is:")
            for row_ in result_:
                print(*row_)

        else:
            print("The operation cannot be performed.")

    elif choice in ["2", "Multiply matrix by a constant"]:
        matrix_info = get_one_matrix()
        matrix = matrix_info[1]
        constant = input("Enter constant: ")

        print("The result is:")
        result_ = multiply_constant(matrix, constant)

        for row_ in result_:
            print(*row_)

    elif choice in ["3", "Multiply matrices"]:
        matrix_info = get_two_matrices()
        matrix_size_a = matrix_info[0][0]
        matrix_elements_a = matrix_info[0][1]
        matrix_size_b = matrix_info[1][0]
        matrix_elements_b = matrix_info[1][1]

        multiplication_result = multiply_by_matrix(matrix_elements_a, matrix_elements_b, matrix_size_a, matrix_size_b)

        print("The result is:")
        for row in multiplication_result:
            print(*row)

    elif choice in ["4", "Transpose matrix"]:
        print("\n1. Main diagonal", "2. Side diagonal", "3. Vertical line", "4. Horizontal line", sep="\n")

        operation = input("Your choice: ")

        if operation in ["1", "Main diagonal"]:
            matrix_info = get_one_matrix()
            original_matrix_size = matrix_info[0]
            original_matrix_ = matrix_info[1]

            print("The result is:")
            for r in transpose_through_main(original_matrix_, original_matrix_size):
                print(*r)

        elif operation in ["2", "Side diagonal"]:
            matrix_info = get_one_matrix()
            original_matrix_size = matrix_info[0]
            original_matrix_ = matrix_info[1]

            print("The result is:")
            for r in transpose_through_second(original_matrix_, original_matrix_size):
                print(*r)

        elif operation in ["3", "Vertical line"]:
            matrix_info = get_one_matrix()
            original_matrix_ = matrix_info[1]

            print("The result is:")
            for r in transpose_though_vertical(original_matrix_):
                print(*r)

        elif operation in ["4", "Horizontal line"]:
            matrix_info = get_one_matrix()
            original_matrix_ = matrix_info[1]

            print("The result is:")
            for r in transpose_through_horizontal(original_matrix_):
                print(*r)

    elif choice in ["5", "Calculate a determinant"]:
        matrix_info = get_one_matrix()
        m_rows = matrix_info[1]
        m_size = matrix_info[0]

        # calculate the determinant and output the determinant
        print(f"The result is:", f"{get_determinant(m_rows, m_size)}", sep="\n")

    elif choice in ["6", "Inverse matrix"]:
        matrix_info = get_one_matrix()
        get_inverse(matrix_info[1])

    elif choice in ["0", "Exit"]:
        break

