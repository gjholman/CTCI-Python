test_matrix = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]

def rotate_matrix(input_matrix):
    #Step 1: check outlier cases
    if len(input_matrix) == 0:
        return
    if len(input_matrix) != len(input_matrix[]): #the second statement should be input_matrix[0]
        return
    print(str(len(input_matrix)))
    N = len(input_matrix)
    upper_limit = N / 2

    for i in range(upper_limit):
        row1 = extract_row(i, input_matrix)
        column1 = extract_row(n-i, input_matrix)
        input_matrix = insert_column(n-i, row1, input_matrix, false) #Because we have to change the input matrix in the function,
        row2 = extract_row(i, input_matrix)                         # the output of those must be the input matrix
        input_matrix = insert_row(n-i, column1, input_matrix, true)
        column_2 = extract_column(i, input_matrix)
        input_matrix = insert_column(i, row2, input_matrix, false)
        insert_row(i, column2, input_matrix, True)
    
    print(input_matrix)

def extract_row(row_num, input_matrix):
    return 

def extract_column(column_num, input_matrix):
    return 

def insert_column(column_num, new_values, input_matrix, reverse):
    return

def insert_row(row_num, new_values, input_matrix, reverse):
    return

#How did I do?
# Format was correct, same outlier cases, same for loop sequence, the only thing is that
# the content in the for loop can be made a lot simpler than you thought, but the 
# pattern is the same as in the answer book! :) :) :)
# not 100% and it took me a little over 45 minutes, and I didn't get to the helper functions

rotate_matrix(test_matrix)
