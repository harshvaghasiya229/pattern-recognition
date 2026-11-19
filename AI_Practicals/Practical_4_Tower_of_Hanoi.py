print("IAR/17360")

# Function to solve Tower of Hanoi
def tower_of_hanoi(number_of_discs, source, destination, auxiliary):

    # Base case: move one disc directly
    if number_of_discs == 1:
        print("Move disc 1 from", source, "to", destination)
        return

    # Move the top discs to the auxiliary peg
    tower_of_hanoi(number_of_discs - 1, source, auxiliary, destination)

    # Move the largest disc to the destination peg
    print("Move disc", number_of_discs, "from", source, "to", destination)

    # Move the remaining discs to the destination peg
    tower_of_hanoi(number_of_discs - 1, auxiliary, destination, source)


print("Tower of Hanoi solution for 3 discs:")
tower_of_hanoi(3, 'A', 'C', 'B')
