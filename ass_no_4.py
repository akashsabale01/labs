# Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and
# bound strategy.

# code
# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity W


def knapSack(W, wt, val, n):
	dp = [0 for i in range(W+1)] # Making the dp array

	for i in range(1, n+1): # taking first i elements
		for w in range(W, 0, -1): # starting from back,so that we also have data of
								# previous computation when taking i-1 items
			if wt[i-1] <= w:
				# finding the maximum value
				dp[w] = max(dp[w], dp[w-wt[i-1]]+val[i-1])

	return dp[W] # returning the maximum value of knapsack


if __name__ == '__main__':
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    # This code is contributed by Suyash Saxena
    print(knapSack(W, wt, val, n))
    
    
# Time Complexity: O(N*W). As redundant calculations of states are avoided.
# where ‘N’ is the number of weight element and ‘W’ is capacity. As for every weight element we traverse through all weight capacities 1<=w<=W.
# Auxiliary Space: O(W) As we are using 1-D array instead of 2-D array.

# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/