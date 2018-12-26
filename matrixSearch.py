"""
Find the target value in a 2D matrix
for i<j, matrix[x][i]<matrix[x][j] and matrix[i][x]<matrix[j][x]

Use: FindNum(target, matrix, row_number, coloumn_number)
    input: matrix should be lists of list
    output: list of position tuple of target or None if not found

Author: Yixuan Wei
2018.8.4
"""


# only deals with column or row search
def BinarySearch(low, high, list, num):
    if low>high:
        return None
    elif low == high:
        if num == list[low]:
            return low
        else:
            return None
    else:
        while True:
            if high - low == 1:
                if list[low] == num:
                    return low
                elif list[high] == num:
                    return high
                else:
                    return None

            elif list[int((low+high) / 2)] > num:
                high = int((low + high) / 2)
            else:
                low = int((low + high) / 2)


def FindNum(num, matrix, m, n):
    m_low = 0
    n_low = 0
    m_high = m - 1
    n_high = n - 1
    # boundary cases
    if matrix[0][0] > num or matrix[m - 1][n - 1] < num:
        return None
    else:
        # matrix[i][j]<=num<=matrix[i+1][j+1], binary search on diagonal direction
        while True:
            if m_high - m_low == 1 or n_high - n_low == 1:
                break
            if matrix[int((m_low + m_high) / 2)][int((n_low + n_high) / 2)] > num:
                m_high = int((m_low + m_high) / 2)
                n_high = int((n_low + n_high) / 2)
            else:
                m_low = int((m_low + m_high) / 2)
                n_low = int((n_low + n_high) / 2)

        # (matrix[m_low --- m][n_low] && matrix[m_high][0 --- n_high] )  &&
        # (matrix[0 --- m_high]][n_high] && matrix[m_low] [n_low---n] )
        # O(lg(m+n))
        print(m_low, m_high, n_low, n_high)
        result = []

        temp = BinarySearch(m_low, m - 1, [each[n_low] for each in matrix], num)
        if temp:
            result.append((temp,n_low))
        temp = BinarySearch( 0, n_high, matrix[m_high], num)
        if temp:
            result.append((m_high,temp))
        temp = BinarySearch(n_low, n - 1, matrix[m_low], num)
        if temp:
            result.append((m_low,temp))
        temp = BinarySearch(0, m_high,[each[n_high] for each in matrix], num)
        if temp:
            result.append((temp,n_high))
        if result:
            return sorted(set(result))
        else:
            return None


if __name__ == "__main__":
    matrix = [[1, 7, 8], [7, 8, 9]]
    num = 7
    print(FindNum(num, matrix, 2, 3))
