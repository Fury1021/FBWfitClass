def firstFit(blockSize, m, processSize, n):
    allocation = [-1] * n

    for i in range(n):
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                allocation[i] = j
                blockSize[j] -= processSize[i]
                break

    print("Process No.   Process Size	 Block no.")
    for i in range(n):
        print(" ", i + 1, "	          	  ", processSize[i],
              "		 ", end=" ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

if __name__ == '__main__':
    blockSize = []
    processSize = []

    print("Enter block sizes. Type 'done' when finished:")
    while True:
        size_input = input()
        if size_input.lower() == 'done':
            break
        blockSize.append(int(size_input))

    print("Enter process sizes. Type 'done' when finished:")
    while True:
        size_input = input()
        if size_input.lower() == 'done':
            break
        processSize.append(int(size_input))

    m = len(blockSize)
    n = len(processSize)

    firstFit(blockSize, m, processSize, n)
