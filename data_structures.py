
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

    def lu_decompose(self, b):
        L, U = Matrix.make_identity(self.rows, 1).data[:], self.data[:]
        for i in range(self.rows-1):
            for j in range(i+1, self.rows):
                factor = U[j][i] / U[i][i]
                L[j][i] = factor
                U[j] = [j - factor*i for i, j in zip(U[i], U[j])]

        y = [0 for i in range(len(L[0]))]
        for i in range(len(L)):
            front_sum = 0
            for j in range(i):
                front_sum += L[i][j]*y[j]
            y[i] = (b[i] - front_sum) / L[i][i]

        x = [0 for i in range(len(y))]
        for i in range(len(y)-1, -1, -1):
            back_sum = 0
            for j in range(len(y)-1, i, -1):
                back_sum += U[i][j] * x[j]
            
            x[i] = (y[i] - back_sum) / U[i][i]

        return x

    @staticmethod
    def inverse(matrix):
        identity = Matrix.make_identity(matrix.rows, 1)
        ans = list()
        for i in range(matrix.rows):
            ans.append(matrix.lu_decompose(identity.data[i]))
        
        return Matrix(ans).reverse()
        
    @staticmethod
    def make_identity(n, lamb):
        return Matrix([[lamb if i == j else 0 for j in range(n)] for i in range(n)])


class Polynomial():
    '''
    coefs example: 5x^4 + 2x^2 - x^1 + 8 => [(4, 5), (2, 2), (1, -1), (0, 8) (degree, coef)]
    '''
    def __init__(self, poly):
        self.polynomial = poly
    
    def __call__(self, x):
        y = 0
        for deg, coef in self.polynomial:
            y += coef * x ** deg

        return y
