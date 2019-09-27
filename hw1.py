import argparse

class Matrix():
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
        return

    def add(self, data):
        ans = list()
        for i in range(self.rows):
            ans.append([a + b for a, b in zip(self.data[i], data.data[i])])

        return Matrix(ans)

    def mul(self, data):
        operand = data.reverse().data
        ans = list()
        for i in range(self.rows):
            cur_row = list()
            for j in range(data.cols):
                cur_row.append(sum([a*b for a, b in zip(self.data[i], operand[j])]))
            ans.append(cur_row)

        return Matrix(ans)

    def reverse(self):
        res = [[0 for j in range(self.rows)] for i in range(self.cols)]
        for i in range(self.cols):
            for j in range(self.rows):
                res[i][j] = self.data[j][i]

        return Matrix(res)

    def inverse(self):
        L, U = make_identity(self.rows, 1), self.data[:]
        for i in range(self.rows-1):
            for j in range(i+1, self.rows):
                factor = U[i][j] / U[i][i]
                L.data[j][i] = factor
                U[j] = [j - factor*i for i, j in zip(U[i], U[j])]
                print (U[j])
        # print (L.data, U)

        return
                
def make_identity(n, lamb):
    return Matrix([[lamb if i == j else 0 for j in range(n)] for i in range(n)])


def read_testcase(sample_in):
    test_cases = open(sample_in, 'r')
    data_points = list()
    for data_point in test_cases:
        data_array = tuple(data_point.strip().split(','))
        data_points.append(data_array)
    
    return data_points

def lse(data_points, base, lamb):
    # print (f'Processing LSE with data points: {data_points} and lambda {lamb}')
    A = list()
    for x, y in data_points:
        row = list()
        for i in range(base-1, -1, -1):
            row.append(float(x)**i)
        A.append(row)

    A = Matrix(A)
    identity = make_identity(A.cols, lamb)
    A = A.reverse().mul(A).add(identity)

    return

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", type=str, help="Path of testcase")
    parser.add_argument("-n", "--base", type=int, help="polynomial bases of predicted regression")
    parser.add_argument("-l", "--lamb", type=int, help="lambda of LSE")
    args = parser.parse_args()

    return args

if __name__ == "__main__":
    args = get_args()
    data_points = read_testcase(args.path)

    lse(data_points, args.base, args.lamb)
    op1 = Matrix([[-1, 2, -1], [1, -4, 6] ,[-2, 6, -6]])
    op1.inverse()
