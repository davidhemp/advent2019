def opcode(data):

    def add(line):
        data[line[3]] = data[line[1]] + data[line[2]]

    def multi(line):
        data[line[3]] = data[line[1]] * data[line[2]]

    def end(line):
        i = len(data)
    
    def null(line):
        return

    commands = [null]*100
    commands[1] = add
    commands[2] = multi
    commands[99] = end
    i = 0
    while i < len(data):
        line = data[i:i+4]
        commands[line[0]](line)
        i += 4
    return data

