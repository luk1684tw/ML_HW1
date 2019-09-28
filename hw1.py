import argparse
import matplotlib.pyplot as plot
import numpy as np

from data_structures import Matrix
from data_structures import Polynomial


def read_testcase(sample_in):
    test_cases = open(sample_in, 'r')
    data_points = list()
    for data_point in test_cases:
        data_array = tuple(data_point.strip().split(','))
        data_points.append(data_array)
    
    return data_points

def plot_figure(data_points, solution):
    data_x, data_y = list(), list()
    for data_point in data_points:
        data_x.append(float(data_point[0]))
        data_y.append(float(data_point[1]))
    
    plot.scatter(data_x, data_y, c='r')
    
    sol = list()
    for i, coef in enumerate(reversed(solution)):
        sol.append((i, coef[0]))

    sol = Polynomial(sol)
    sample_x = np.linspace(min(data_x), max(data_x), 50)
    sample_y = sol(sample_x)

    plot.plot(sample_x, sample_y)
    plot.savefig('lse_plot.png')
    return


def lse(data_points, base, lamb):
    # print (f'Processing LSE with data points: {data_points} and lambda {lamb}')
    A = list()
    b = list()
    for x, y in data_points:
        row = list()
        for i in range(base-1, -1, -1):
            row.append(float(x)**i)
        A.append(row)
        b.append([float(y)])

    b = Matrix(b)
    A = Matrix(A)
    identity = Matrix.make_identity(A.cols, lamb)
    A_reverse = A.reverse()
    
    A = A.reverse().mul(A).add(identity)
    A = Matrix.inverse(A)

    return A.mul(A_reverse).mul(b).data

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

    ans = lse(data_points, args.base, args.lamb)
    # ans = 
    plot_figure(data_points, ans)
    print (ans)

