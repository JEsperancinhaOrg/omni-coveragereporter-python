def total_lines(file_name):
    f = open(file_name)
    data = f.readlines()
    f.close()
    return len(data)
