# Author 1: Altay Acar - 2018400084
# Author 2: Engin Oguzhan Senol - 2020400324

import random
import sys

"""
runs a las vegas algorithm for n (parameter 0) queens problem and writes the results to file (parameter 1)
"""
def queens_lv(n, file) :
    """
    initializes the n*n chess board
        [][]
    column row
    """
    chess_board = [[0 for x in range(n)] for y in range(n)]
    available_columns = [i for i in range(n)]     # all columns are available initially
    r = 0   # beginning with the first row
    queens_in_columns = [None for x in range(n)]    # queens placed has [cloumn_number] in the list
    result = "" # result of the computation

    while r <= n-1 and available_columns:
        c = random.choice(available_columns) # column c is chosen randomly for queen to be placed
        chess_board[r][c] = 1   # queen #r is placed at cth column, rth row
        queens_in_columns[r] = c    # rth queen in the list is marked with its corresponding column
        r = r + 1  # next iteration will be for the next row
        # each unavailable column is removed from the available_columns list
        temp_row = 0
        # iterates over each row in the board
        column_list = [i for i in range(n)] # stores available columns
        for row in chess_board:
            factor = r - temp_row   # to compute the diagonal cells to be removed from the available_columns
            temp_column = 0
            # iterates over each column for each row
            for cell in row:
                if cell == 1:   # checks if the current cell is placed a queen
                    back = temp_column - factor # to be removed cell that resides in the column that stays in the back of the current column
                    current = temp_column   # to be removed cell that resides in the column that stays in the current column
                    front = temp_column + factor    # to be removed cell that resides in the column that stays in the front of the current column
                    # checks if above calculated cells are in the available_columns list and removes them if so
                    if back in column_list:
                        column_list.remove(back)
                    if current in column_list:
                        column_list.remove(current)
                    if front in column_list:
                        column_list.remove(front)
                temp_column = temp_column + 1   # next iteration -> next column
            temp_row = temp_row + 1 # next iteration -> next row
        available_columns = column_list # available columns is updated
        # stores the steps of computation in a string as a whole
        result = result + "Step " + str(r) + ": Columns :" + "".join(str(queens_in_columns)) + "\n" + "Step " + str(r) + ": Available :" + "".join(str(available_columns)) + "\n"

    """
    checks if the result of computation is successful or not.
    if there is a 1 in the last row of chess board, meaning a queen is placed in that row
    then the computation is successful and a queen is placed in each row of the chess board

    Successful computation -> returns True and computation steps
    Unsuccessful computation -> return False and computation steps
    """
    if 1 in chess_board[n-1]:
        # Success
        file.write(result + "Successful\n...\n\n")
        return True, result
    else:
        # Fail
        file.write(result + "Unsuccessful\n...\n\n")
        return False, result

"""
looks for the list of available columns (parameter 3) of current row r (parameter 1) of n*n (parameter 0) chess_board (parameter 2)
if there are available columns, then tries to fill the board starting from that cell.
if successfully fills out the board according to n queens problem, then returns true. if not, then returns false
"""
def backtrack(n, r, chess_board, available_columns):
    # checks if there is any available column left for the current row r
    if available_columns:
        # iterates over each available column in the current row r
        for c in available_columns:
            chess_board[r][c] = 1   # places a queen the first available cell
            if r == n -1 :
                return True # if the last row is placed, algorithm is successful
            r = r + 1   # moves to the next row
            # each unavailable column is removed from the available_columns list
            temp_row = 0
            # iterates over each row in the board
            column_list = [i for i in range(n)] # stores available columns
            for row in chess_board:
                factor = r - temp_row   # to compute the diagonal cells to be removed from the available_columns
                temp_column = 0
                # iterates over each column for each row
                for cell in row:
                    if cell == 1:   # checks if the current cell is placed a queen
                        back = temp_column - factor # to be removed cell that resides in the column that stays in the back of the current column
                        current = temp_column   # to be removed cell that resides in the column that stays in the current column
                        front = temp_column + factor    # to be removed cell that resides in the column that stays in the front of the current column
                        # checks if above calculated cells are in the available_columns list and removes them if so
                        if back in column_list:
                            column_list.remove(back)
                        if current in column_list:
                            column_list.remove(current)
                        if front in column_list:
                            column_list.remove(front)
                    temp_column = temp_column + 1   # next iteration -> next column
                temp_row = temp_row + 1 # next iteration -> next row
            available_columns = column_list # available columns is updated
            # calls backtracking algorithm recursively
            result = backtrack(n, r, chess_board, available_columns)
            if result:
                # if the backtracking algorithm successfully places a queen in each row, then it reaches the last row and returns true
                return True
            else:
                # if backtracking algorithm fails finding a suitable place for row r, it backtracks to row (r - 1) and removes the queen placed in the previous row (r - 1)
                r = r - 1
                chess_board[r][c] = 0
    return False    # if no available columns left, then returns false, computation is fail

"""
places k (parameter 1) queens in the first k row of a n*n (parameter 0) chess board.
after that tries to fill out the rest of the board for n queens problem using backtracking algorithm.
"""
def queens_lv_k(n, k):
    """
    initializes the n*n chess board
        [][]
    column row
    """
    chess_board = [[0 for x in range(n)] for y in range(n)]
    available_columns = [i for i in range(n)]     # all columns are available initially
    r = 0   # beginning with the first row
    queens_in_columns = [None for x in range(n)]    # queens placed has [cloumn_number] in the list

    # randomly places k queens in the first k row of the board
    while r < k and available_columns:
        c = random.choice(available_columns) # column c is chosen randomly for queen to be placed
        chess_board[r][c] = 1   # queen #r is placed at cth column, rth row
        queens_in_columns[r] = c    # rth queen in the list is marked with its corresponding column
        r = r + 1  # next iteration will be for the next row
        # each unavailable column is removed from the available_columns list
        temp_row = 0
        # iterates over each row in the board
        column_list = [i for i in range(n)] # stores available columns
        for row in chess_board:
            factor = r - temp_row   # to compute the diagonal cells to be removed from the available_columns
            temp_column = 0
            # iterates over each column for each row
            for cell in row:
                if cell == 1:   # checks if the current cell is placed a queen
                    back = temp_column - factor # to be removed cell that resides in the column that stays in the back of the current column
                    current = temp_column   # to be removed cell that resides in the column that stays in the current column
                    front = temp_column + factor    # to be removed cell that resides in the column that stays in the front of the current column
                    # checks if above calculated cells are in the available_columns list and removes them if so
                    if back in column_list:
                        column_list.remove(back)
                    if current in column_list:
                        column_list.remove(current)
                    if front in column_list:
                        column_list.remove(front)
                temp_column = temp_column + 1   # next iteration -> next column
            temp_row = temp_row + 1 # next iteration -> next row
        available_columns = column_list # available columns is updated
    # starts the search in the next row
    if available_columns:
        # iterates over each available column
        for c in available_columns:
            chess_board[r][c] = 1   # places a queen to the first available column
            # checks whether one queen placed at each row or not 
            if r == n - 1:
                # if the last row is placed, algorithm is successful
                return True
            r = r + 1   # if there are still rows that are not placed a queen continues for search
            # each unavailable column is removed from the available_columns list
            temp_row = 0
            # iterates over each row in the board
            column_list = [i for i in range(n)] # stores available columns
            for row in chess_board:
                factor = r - temp_row   # to compute the diagonal cells to be removed from the available_columns
                temp_column = 0
                # iterates over each column for each row
                for cell in row:
                    if cell == 1:   # checks if the current cell is placed a queen
                        back = temp_column - factor # to be removed cell that resides in the column that stays in the back of the current column
                        current = temp_column   # to be removed cell that resides in the column that stays in the current column
                        front = temp_column + factor    # to be removed cell that resides in the column that stays in the front of the current column
                        # checks if above calculated cells are in the available_columns list and removes them if so
                        if back in column_list:
                            column_list.remove(back)
                        if current in column_list:
                            column_list.remove(current)
                        if front in column_list:
                            column_list.remove(front)
                    temp_column = temp_column + 1   # next iteration -> next column
                temp_row = temp_row + 1 # next iteration -> next row
            available_columns = column_list # available columns is updated
            # calls backtrack function to place next queen to row r 
            result = backtrack(n, r, chess_board, available_columns)
            if result:
                return True # if backtracking algorithm successfully places a queen in each row, then it returns true and the computation is successful
            else:
                # if not, then the algorithm moves one step back and removes the initially placed queen and continues for the next available column
                r = r - 1
                chess_board[r][c] = 0
        return False    # if each available cell is tried and still no correct solution found, then it is a failure
    else:
        return False    # if no available columns left for current row to placed, then the computation fails

"""
runs the first part of the project
"""
def part1():
    # corresponding file names for computation of each problem with n queens
    file_6 = "results_6.txt"
    file_8 = "results_8.txt"
    file_10 = "results_10.txt"

    success_count_6 = 0     # total success count for 6 queens problem
    success_count_8 = 0     # total success count for 8 queens problem
    success_count_10 = 0    # total success count for 10 queens problem

    f_6 = open(file_6, "a")
    # runs queens_lv for 10000 times for 6 queens and keeps the track of successful computations besides the results for results_mini
    for i in range(10000):
        result = queens_lv(6, f_6)  # One random computation for 6 queens
        if result[0]:
            success_count_6 = success_count_6 + 1
    prob_6 = success_count_6 / 10000
    # prints the probabilistic result of 6 queens problem to command line according to problem description
    print("LasVegas Algorithm n = 6")
    print("Number of successful placements is " + str(success_count_6))
    print("Number of trials is 10000")
    print("Probability that it will come to a solution is " + str(prob_6) + "\n")
    f_6.close()

    f_8 = open(file_8, "a")
    # runs queens_lv for 10000 times for 8 queens and keeps the track of successful computations besides the results for results_mini
    for i in range(10000):
        result = queens_lv(8, f_8)  # One random computation for 8 queens
        if result[0]:
            success_count_8 = success_count_8 + 1
    prob_8 = success_count_8 / 10000
    # prints the probabilistic result of 8 queens problem to command line according to problem description    
    print("LasVegas Algorithm n = 8")
    print("Number of successful placements is " + str(success_count_8))
    print("Number of trials is 10000")
    print("Probability that it will come to a solution is " + str(prob_8) + "\n")
    f_8.close()

    f_10 = open(file_10, "a")
    # runs queens_lv for 10000 times for 10 queens and keeps the track of successful computations besides the results for results_mini
    for i in range(10000):
        result = queens_lv(10, f_10)    # One random computation for 10 queens
        if result[0]:
            success_count_10 = success_count_10 + 1
    prob_10 = success_count_10 / 10000
    # prints the probabilistic result of 10 queens problem to command line according to problem description
    print("LasVegas Algorithm n = 10")
    print("Number of successful placements is " + str(success_count_10))
    print("Number of trials is 10000")
    print("Probability that it will come to a solution is " + str(prob_10) + "\n")
    f_10.close()

"""
runs the second part of the project
"""
def part2():
    # runs the n queens problem with initial k queens and (6*6 board) using backtracking algorithm to fill the rest 10000 times
    # k starts from 0 and is incremented after each trial until k = 5
    # prints the results to the command line
    print("--------------- 6 ---------------")
    for k in range(6):
        print("k is " + str(k))
        success_count_6 = 0     # stores the total number of successful computations for 6*6 board
        for t in range(10000):
            result = queens_lv_k(6, k)
            if result:
                success_count_6 = success_count_6 + 1
        print("Number of successful placements is " + str(success_count_6))
        print("Number of trials is 10000")
        prob_6 = success_count_6 / 10000    # success rate of the computation for 6*6 board
        print("Probability that it will come to a solution is " + str(prob_6))
    print("\n")
    # runs the n queens problem with initial k queens and (8*8 board) using backtracking algorithm to fill the rest 10000 times
    # k starts from 0 and is incremented after each trial until k = 7
    # prints the results to the command line
    print("--------------- 8 ---------------")
    for k in range(8):
        print("k is " + str(k))
        success_count_8 = 0     # stores the total number of successful computations for 8*8 board
        for t in range(10000):
            result = queens_lv_k(8, k)
            if result:
                success_count_8 = success_count_8 + 1
        print("Number of successful placements is " + str(success_count_8))
        print("Number of trials is 10000")
        prob_8 = success_count_8 / 10000    # success rate of the computation for 8*8 board
        print("Probability that it will come to a solution is " + str(prob_8))
    print("\n")
    # runs the n queens problem with initial k queens and (10*10 board) using backtracking algorithm to fill the rest 10000 times
    # k starts from 0 and is incremented after each trial until k = 9
    # prints the results to the command line
    print("--------------- 10 ---------------")
    for k in range(10):
        print("k is " + str(k))
        success_count_10 = 0    # stores the total number of successful computations for 10*10 board
        for t in range(10000):
            result = queens_lv_k(10, k)
            if result:
                success_count_10 = success_count_10 + 1
        print("Number of successful placements is " + str(success_count_10))
        print("Number of trials is 10000")
        prob_10 = success_count_10 / 10000  # success rate of the computation for 10*10 board
        print("Probability that it will come to a solution is " + str(prob_10))
    print("\n")

run_part = sys.argv[1]

if run_part == "part1":
    part1()
if run_part == "part2":
    part2()