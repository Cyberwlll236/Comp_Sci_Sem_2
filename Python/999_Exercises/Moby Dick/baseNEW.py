with open('moby.txt') as f:
    wcount = 0
    lnum = 0
    for line in f:
        lnum = lnum + 1
        sentence = line.strip()
        for i in range(0, len(sentence)):
            if sentence[i:i+5] == "whale":
                wcount = wcount + 1
                print("Line " + str(lnum))
            elif sentence[i:i+5] == "WHALE":
                wcount = wcount + 1
                print("Line " + str(lnum))
            elif sentence[i:i+5] == "Whale":
                wcount = wcount + 1
                print("Line " + str(lnum))
    print("Whale count: " + str(wcount))

f.close()
