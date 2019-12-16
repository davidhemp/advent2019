from opcode import opcode

def test(data, required, index, test_no):
    test_return = opcode(data)
    if test_return[index] == required:
        print("Test {} passed".format(test_no))
    else:
        raise ValueError("test {} failed".format(test_no))


if __name__ == "__main__":
    test([1,9,10,3,2,3,11,0,99,30,40,50], 3500, 0, 1)
    test([1,0,0,0,99], 2, 0, 2)
    test([2,3,0,3,99], 6, 3, 3)
    test([2,4,4,5,99,0], 9801, 5, 4)
    test([1,1,1,4,99,5,6,0,99], 30, 0, 5)
