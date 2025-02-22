class Fit:
    @staticmethod
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

    print("")
    print("")
    print("===========================================")
    @staticmethod
    def first_fit(blockSize, m, processSize, n):
        allocation = [-1] * n

        for i in range(n):
            for j in range(m):
                if blockSize[j] >= processSize[i]:
                    allocation[i] = j
                    blockSize[j] -= processSize[i]
                    break

        print("Process No.        Process Size	       Block no.")
        for i in range(n):
            print(" ", i + 1, "	          	  ", processSize[i],
                  "	   ", end="		 ")
            if allocation[i] != -1:
                print(allocation[i] + 1)
            else:
                print("Not Allocated")

        print("")
        print("")
        print("===========================================")

    @staticmethod
    def best_fit(blockSize, m, processSize, n):
        allocation = [-1] * n

        for i in range(n):
            best_idx = -1
            for j in range(m):
                if blockSize[j] >= processSize[i]:
                    if best_idx == -1:
                        best_idx = j
                    elif blockSize[best_idx] > blockSize[j]:
                        best_idx = j

            if best_idx != -1:
                allocation[i] = best_idx
                blockSize[best_idx] -= processSize[i]

        print("Process No.        Process Size	       Block no.")
        for i in range(n):
            print(" ", i + 1, "	          	  ", processSize[i],
                  "	   ", end="		 ")
            if allocation[i] != -1:
                print(allocation[i] + 1)
            else:
                print("Not Allocated")

        print("")
        print("")
        print("===========================================")

    @staticmethod
    def worst_fit(blockSize, m, processSize, n):
        allocation = [-1] * n

        for i in range(n):
            wst_idx = -1
            for j in range(m):
                if blockSize[j] >= processSize[i]:
                    if wst_idx == -1:
                        wst_idx = j
                    elif blockSize[wst_idx] < blockSize[j]:
                        wst_idx = j

            if wst_idx != -1:
                allocation[i] = wst_idx
                blockSize[wst_idx] -= processSize[i]

        print("Process No.        Process Size	       Block no.")
        for i in range(n):
            print(" ", i + 1, "	          	  ",processSize[i],
                  "	   ", end="		 ")
            if allocation[i] != -1:
                print(allocation[i] + 1)
            else:
                print("Not Allocated")
        print("")
        print("")
        print("===========================================")

    @staticmethod
    def exit_program():
        print("Exiting the program")
        exit()



    @staticmethod
    def insert_new_lines(num_lines):
        for _ in range(num_lines):
            print()




def main():
    fit_object = Fit()
    numlines = 100

    choice = 1
    while choice != 0:

        print("Choose a choice below: ")
        print("1. First Fit Algorithm")
        print("2. Best Fit Algorithm")
        print("3. Worst Fit Algorithm")
        print("4. EXIT")
        print("")
        choice = int(input("Enter your choice: "))
        if choice == 0:
            fit_object.exit_program()
        elif choice == 1:
            fit_object.insert_new_lines(numlines)
            print("You chose the First Fit Algorithm")
            block_sizes, process_sizes = fit_object.get_block_and_process_sizes()
            fit_object.first_fit(block_sizes, len(block_sizes), process_sizes, len(process_sizes))
            neworexit()
        elif choice == 2:
            fit_object.insert_new_lines(numlines)
            print("You chose the Best Fit Algorithm")
            block_sizes, process_sizes = fit_object.get_block_and_process_sizes()
            fit_object.best_fit(block_sizes, len(block_sizes), process_sizes, len(process_sizes))
            neworexit()
        elif choice == 3:
            fit_object.insert_new_lines(numlines)
            print("You chose the Worst Fit Algorithm")
            block_sizes, process_sizes = fit_object.get_block_and_process_sizes()
            fit_object.worst_fit(block_sizes, len(block_sizes), process_sizes, len(process_sizes))
            neworexit()
        elif choice == 4:
            fit_object.insert_new_lines(numlines)
            print("You chose to end the program")
            fit_object.exit_program()
        else:
            fit_object.insert_new_lines(numlines)
            print("Invalid Choice, Try again")


def neworexit():
    fit_object = Fit()
    numlines = 100
    option = 1
    while option !=0:
        print("1. New Algorithm")
        print("2. End Program")
        print("")
        option = int(input("Enter your option: "))
        if option == 1:
            fit_object.insert_new_lines(numlines)
            print("===========================================")
            main()
        elif option == 2:
            exit()
        else:
            print("Invalid Option, Try Again")

if __name__ == '__main__':
    main()
