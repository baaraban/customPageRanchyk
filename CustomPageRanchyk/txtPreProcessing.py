def createWithoutBlankLines(path):
    with open(path, 'r') as infile, open(path + "lineFree", 'w') as outfile:
        for line in infile:
            if not line.strip(): continue  # skip the empty line
            outfile.write(line)  # non-empty line. Write it to output