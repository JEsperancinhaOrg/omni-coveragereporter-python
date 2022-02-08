MINIMAL_STATS_LENGTH = 14

def merge(lines, index, hits):
    if lines[index] is None:
        lines[index] = hits
    else:
        lines[index] += hits
