
class NewLineInserter:
    @staticmethod
    def insert_new_lines(num_lines):
        for _ in range(num_lines):
            print()

class First:

    @staticmethod
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


class Best:

    @staticmethod
    def bestFit(blockSize, m, processSize, n):
        allocation = [-1] * n

        for i in range(n):
            bestIdx = -1
            for j in range(m):
                if blockSize[j] >= processSize[i]:
                    if bestIdx == -1:
                        bestIdx = j
                    elif blockSize[bestIdx] > blockSize[j]:
                        bestIdx = j

            if bestIdx != -1:
                allocation[i] = bestIdx
                blockSize[bestIdx] -= processSize[i]

        print("Process No.   Process Size	 Block no.")
        for i in range(n):
            print(i + 1, "	          	  ", processSize[i],
                  end="		 ")
            if allocation[i] != -1:
                print(allocation[i] + 1)
            else:
                print("Not Allocated")


class Worst:

    @staticmethod
    def worstFit(blockSize, m, processSize, n):
        allocation = [-1] * n

        for i in range(n):
            wstIdx = -1
            for j in range(m):
                if blockSize[j] >= processSize[i]:
                    if wstIdx == -1:
                        wstIdx = j
                    elif blockSize[wstIdx] < blockSize[j]:
                        wstIdx = j

            if wstIdx != -1:
                allocation[i] = wstIdx
                blockSize[wstIdx] -= processSize[i]

        print("Process No.   Process Size	 Block no.")
        for i in range(n):
            print(i + 1, "	          	  ",
                  processSize[i], end="	 ")
            if allocation[i] != -1:
                print(allocation[i] + 1)
            else:
                print("Not Allocated")


def main():
    num_lines = 100
    inserter = NewLineInserter()

    while True:
        print("1 (First)  2 (Best)  3 (Worst)  4 (Exit)")
        choice = input("Enter your choice: ")

        if choice == '1':
            inserter.insert_new_lines(num_lines)
            blockSize, processSize = get_block_and_process_sizes()
            First.firstFit(blockSize.copy(), len(blockSize), processSize.copy(), len(processSize))
        elif choice == '2':
            inserter.insert_new_lines(num_lines)
            blockSize, processSize = get_block_and_process_sizes()
            Best.bestFit(blockSize.copy(), len(blockSize), processSize.copy(), len(processSize))
        elif choice == '3':
            inserter.insert_new_lines(num_lines)
            blockSize, processSize = get_block_and_process_sizes()
            Worst.worstFit(blockSize.copy(), len(blockSize), processSize.copy(), len(processSize))
        elif choice == '4':
            exit()
            break
        else:
            inserter.insert_new_lines(num_lines)
            print("Please input a valid number (1, 2, 3, or 4).")


def get_block_and_process_sizes():
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

    return blockSize, processSize


if __name__ == '__main__':
    main()
