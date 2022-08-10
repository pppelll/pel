
#trimming left side
def ltrim(b):
    idx = 0
    while b[idx] == ' ':
        idx += 1
    return b[idx:]
def rtrim(b):
    idx = len(b) - 1
    while b[idx] == ' ':
        idx -= 1
    return b[:idx + 1]
def lrtrim(b):
    return(rtrim(ltrim(b)))
