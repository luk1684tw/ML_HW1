sample_in = './sample_in.txt'

def read_testcase(sample_in):
    test_cases = open(sample_in, 'r')
    data_points = list()
    for data_point in test_cases:
        data_array = tuple(data_point.split(','))
        data_points.append(data_array)
    return data_points

def lu_decompose()

if __name__ == "__main__":
    data_points = read_testcase(sample_in)
    