class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            old, new = 1, 2
            for _ in range(n-2):
                old, new = new, old + new

            return new
        
"""
This is a typical dynamic programming problem. There are two base cases. When
you are one step from the end, there is only one possible way to reach the end.
When you are two steps from the end, there are two ways to reach the end, either
climbing one step twice, or climbing two steps once.

For any other number of steps, the number of ways to reach a step is equal to
the number of ways to reach the step before it plus the number of ways to reach
the step two before it. This is exactly the same recursive relationship as the
Fibonacci sequence. Therefore, within the else block is the Pythonic way of 
generating the Fibonacci sequence and the output of the function is the final
value.
"""