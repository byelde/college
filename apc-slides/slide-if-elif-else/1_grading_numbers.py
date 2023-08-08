"""Create a program that input a integer N and print a message grading it as odd, even, positive, negative or neutral."""

#main
N = int(input())

if N % 2 == 0:
    print(f'The number {N} is even', end=" ")
else:
    print(f'The number {N} is odd', end=" ")

if N > 0:
    print('and positive.')
elif N == 0:
    print('and neutral.')
else:
    print('and negative.')