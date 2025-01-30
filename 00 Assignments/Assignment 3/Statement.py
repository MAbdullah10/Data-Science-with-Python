# Task 1: 1D Array - Sum of Even and Odd Indexed Elements
# You are given a 1D array of integers. Write a function that computes the sum of all elements at even indices and the sum of all elements at odd indices.
# Input: A 1D array of integers.
# Example Input:[2, 5, 3, 8, 10, 7]
# Expected Output: Sum of elements at even indices = 15  
# 		 Sum of elements at odd indices = 20
# Hint: Remember, indices start from 0. Even indices are 0, 2, 4... Odd indices are 1, 3, 5...


# Task 2: 2D Array - Row-wise Maximum
# You are given a 2D array with each row containing scores of students in different subjects. Write a function that finds the highest score in each row.
# Input: A 2D array of student scores.
# Example Input:[
#  [65, 78, 85, 92, 55],   # Student 1
#  [82, 91, 88, 60, 70],   # Student 2
#  [95, 80, 75, 88, 72]    # Student 3
# ]
# Expected Output:[92, 91, 95]
# Hint: Use the built-in max() function to get the maximum score in each row.


# Task 3: 3D Array - Diagonal in a Cube
# You are given a 3D array (cube) with dimensions n x n x n. Write a function that sums up the elements that are located on the main diagonal of the 3D matrix. The diagonal elements will have the same index across all three dimensions (i.e., where i == j == k).
# Input: A 3D array (cube) of size n x n x n.
# Example Input (3x3x3 cube):[
#  [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
#  [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
#  [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
# ]
# Expected Output: 45   # (Sum of diagonal elements: 1 + 14 + 27)