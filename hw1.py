import argparse

class Matrix():
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
        return
    
    def mul(self, data):
        operand = data.reverse().data
        for 
    def reverse(self):
        res = [[0 for j in range(self.rows)] for i in range(self.cols)]
        for i in range(self.cols):
            for j in range(self.rows):
                res[i][j] = self.data[j][i]

        return Matrix(res)

    def inverser(self):
        pass

def read_testcase(sample_in):
    test_cases = open(sample_in, 'r')
    data_points = list()
    for data_point in test_cases:
        data_array = tuple(data_point.strip().split(','))
        data_points.append(data_array)
    
    return data_points

def lu_decompose():
    pass

def lse(data_points, base, lamb):
    # print (f'Processing LSE with data points: {data_points} and lambda {lamb}')

    A = list()
    for x, y in data_points:
        row = list()
        for i in range(base-1, -1, -1):
            row.append(float(x)**i)
        A.append(row)

    A = Matrix(A)
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
    test = Matrix([[1, 3, 5], [2, 4, 6]])
    print (test.reverse().data)
    