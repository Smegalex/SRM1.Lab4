def createMatrix(rows: int, columns: int):
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(columns):
            matrix[i].append(0)
    return matrix


def printMatrix(matrix: list):
    return '\n'.join(str(x) for x in matrix)


def connecting(arr1: list, arr2: list):
    final = createMatrix(len(arr1), len(arr1[0]))
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            if arr1[i][j] or arr2[i][j]:
                final[i][j] = 1
            else:
                final[i][j] = 0
    return final


def composition(matrix1: list, matrix2: list):
    final = createMatrix(len(matrix1), len(matrix1[0]))
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            for k in range(len(matrix1[i])):
                if matrix1[i][j] and matrix2[j][k]:
                    final[i][k] = 1
    return final


def isReflexive(matrix: list, reflexive: bool):
    # reflexive == True (перевірка на рефлексивність); == False (перевірка на антирефлексивність)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j and matrix[i][j] == reflexive:
                continue
            elif i != j:
                continue
            else:
                return False
    return True


def isSymetric(matrix: list, symetric: int):
    # symetric == 1 (перевірка на симетричність); == 0 (перевірка на асиметричність);  == -1 (перевірка на антисиметричність);
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if symetric != -1:
                if matrix[i][j] and (matrix[j][i] == symetric):
                    continue
                elif not matrix[i][j]:
                    continue
                else:
                    return False
            else:
                if matrix[i][j] and (matrix[j][i] == 0):
                    continue
                elif not matrix[i][j]:
                    continue
                elif i == j:
                    continue
                else:
                    return False
    return True


def isTransitive(matrix: list):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i])):
                if (matrix[i][j] == 1) and (matrix[j][k] == 1) and (matrix[i][k] != 1):
                    return False
    return True


def reflexive_closure(matrix: list):
    for i in range(len(matrix)):
        matrix[i][i] = 1
    return matrix


def symetric_closure(matrix: list):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]:
                matrix[j][i] = 1
    return matrix


def transitive_closure(matrix: list):
    final = createMatrix(len(matrix), len(matrix[0]))
    powers = createMatrix(len(matrix), len(matrix[0]))
    for topower in range(2, len(matrix[0])+1):
        if topower == 2:
            powers = composition(matrix, matrix)
        else:
            powers = composition(powers, matrix)
            final = connecting(final, powers)
    return final


bit_matrix = [
    [1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1],
]

bit_matrix1 = [
    [1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1]
]


def main(matrix: list):
    matrixInString = printMatrix(matrix)
    # перевірка на відношення еквівалентності (рефлексивне, симетричне, транзитивне)
    if isReflexive(matrix, True) and isSymetric(matrix, 1) and isTransitive(matrix):
        print(
            f"Відношення задане булевою матрицею\n{matrixInString}\nє відношенням еквівалентності.")

    # перевірка на відношення часткового порядку (рефлексивне, антисиметричне, транзитивне)
    if isReflexive(matrix, True) and isSymetric(matrix, -1) and isTransitive(matrix):
        print(
            f"Відношення задане булевою матрицею\n{matrixInString}\nє відношенням часткового порядку.")

    # перевірка на відношення строгого порядку (антирефлексивне, антисиметричне, транзитивне)
    if isReflexive(matrix, False) and isSymetric(matrix, -1) and isTransitive(matrix):
        print(
            f"Відношення задане булевою матрицею\n{matrixInString}\nє відношенням строгого порядку.")

    if not isReflexive(matrix, True):
        print(
            f"Рефлексивним замиканням матриці\n{matrixInString}\nє матриця \n{printMatrix(reflexive_closure(matrix))}\n")
    if not isSymetric(matrix, 1):
        print(
            f"Симетричним замиканням матриці\n{matrixInString}\nє матриця \n{printMatrix(symetric_closure(matrix))}\n")
    if not isTransitive(matrix):
        print(
            f"Транзитивним замиканням матриці\n{matrixInString}\nє матриця \n{printMatrix(transitive_closure(matrix))}\n")
        
    squared = composition(matrix, matrix)
    cubic = composition(squared, matrix)


main(bit_matrix)
main(bit_matrix1)