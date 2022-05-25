# Recursion

a function that calls itself until it does not

for example,

- think of a function called "open_gift_box" that checks if inside the gift box there is a ball
- if there is not a ball then the function will get called again
- if there is a ball then we will return the ball

## BASE CASE

BASE CASE or when the function will stop calling itself is when the function returns the ball

## RECURSIVE CASE

RECURSIVE CASE when the function calls itself again

### Important

to note to always return something AKA always have a return statement

- and that statement has to be something that is eventually true because if you do not then you are going to have a stack overflow

# Call Stack

start explaining call stack with functions that are not recursive first because important to learn that before going into recursion

in CallStack.py we run a script that calls on three functions using a call stack

- notice even though the functions get called in the order of 1,2,3 they get printed out out 3,2,1
- that is because of the order they called off the call stack

### Run and Debug

- bring up side window

  1. select "debug console"
     ![debug](https://i.imgur.com/9OnSzHl.png)

  2. next to funcOne() you will see a bright red dot
  3. which creates a break point
  4. only focus on call stack
  5. where it says run and debug make sure you select "python current file" is chosen
     ![breakPoint](https://i.imgur.com/WtZtTYp.png)

# Factorial

4!

4 x 3 x 2 x 1

4!

4 x 3!

3 x 2!

2 x 1!

1
