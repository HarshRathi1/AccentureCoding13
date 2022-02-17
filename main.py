'''Instructions: You are required to write the code. You can click on compile and run anytime to check compilation/execution status. The code should be logically/syntactically correct.
Problem: Write a program in C to display the table of a number and print the sum of all the multiples in it.
Test Cases:
Test Case 1:
Input:
5
Expected Result Value:
5, 10, 15, 20, 25, 30, 35, 40, 45, 50
275'''
n=15
t=[]
for i in range(1,11):
    t.append(n*i)
print(*t,sep=',')
print(sum(t))