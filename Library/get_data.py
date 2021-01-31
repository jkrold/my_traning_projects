with open('database.txt') as data:
    splited_data = []
    for i, line in enumerate(data):
        splited_line = line.split('\t')
        splited_line[2] = splited_line[2][:-1]
        print(splited_line)
        splited_data.append(splited_line)

