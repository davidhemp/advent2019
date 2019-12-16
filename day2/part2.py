from opcode import opcode

if __name__ == "__main__":
    for i in range(0,100):
        for j in range(0,100):     
            with open('input') as f:
                data = [int(i) for i in f.read().split(",")]
    
            data[1] = i
            data[2] = j
            if opcode(data)[0] == 19690720:
                print(i,j, 100*i+j)

