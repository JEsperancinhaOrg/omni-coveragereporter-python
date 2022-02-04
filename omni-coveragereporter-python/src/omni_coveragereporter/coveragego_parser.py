MINIMAL_STATS_LENGTH = 14


def total_lines(file_name):
    f = open(file_name)
    data = f.readlines()
    f.close()
    return len(data)


def merge(lines, index, hits):
    if lines[index] is None:
        lines[index] = hits
    else:
        lines[index] += hits
