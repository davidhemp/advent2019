from opcode import opcode

def test(data, required, index, test_no):
    test_return = opcode(data)
    if test_return[index] == required:
        print("Test {} passed".format(test_no))
    else:
        raise ValueError("test {} failed".format(test_no))
    

if __name__ == "__main__":
    with open('input') as f:
        data = [int(i) for i in f.read().split(",")]
    
    data[1] = 12
    data[2] = 2
    print(opcode(data)[0])
