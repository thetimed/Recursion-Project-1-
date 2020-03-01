# Name: <TODO: replace with your name>
# Section: <TODO: replace with your section>

# p1q1

# TODO: fill q1_recursive
# m is a matrix represented by a 2D list of integers. e.g. m = [[1,2,3],[4,5,6],[7,8,9]]
# This function returns the another 2D list based on the specified logic in the requirements.

# DO NOT EDIT q1(m)
#len(m)
#len(m)  to find rows
#len(m[0])  to find columns
def q1(m):
  # creating an output 2D list with the same dimensions and initializing all values to None
  # q1_recursive function will update this 2D list accordingly with the computed values
  output = [[None for i in range(len(m[0]))] for j in range(len(m))]
  q1_recursive(m, output, 0, 0)
  return output

def q1_recursive(m, output, row, col):
    for rows in range(len(m)):
        for columns in range(len(m[0])):
            output[rows][columns] = adding_rows(m,rows,columns) + adding_columns(m,rows,columns)
    return output
  # reduction step - valid cell => process across and down and compute total

def adding_rows(m,row,col):
    if col + 1 == len(m[row]):
        return m[row][col] # if col + 1 equals to no of columns left, return that value
    else:
        #Do recursion by reducing the problem
        #We do recursion by reducing the array
        return m[row][col] + adding_rows(m,row,col+1)

def adding_columns(m,row,col):
    if row +1 == len(m):
        return m[row][col] # if col + 1 equals to no of columns left, return that value
    else:
        #Do recursion by reducing the problem
        #We do recursion by reducing the array
        return m[row][col] + adding_columns(m,row+1,col)
