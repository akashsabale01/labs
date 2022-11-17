# Write a program to solve a fractional Knapsack problem using a greedy method.

# The basic idea of the greedy approach is to calculate the ratio value/weight for each item and sort the item on the basis of this ratio. 
# Then take the item with the highest ratio and add them until we can’t add the next item as a whole and at the end add the next item as much as we can. 
# Which will always be the optimal solution to this problem.

# Time Complexity: O(N * log N)
# Auxiliary Space: O(N)


# Structure for an item which stores weight and corresponding value of Item
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        

def fractionalKnapsack(W, arr):
    
    # Sorting Item on basis of ratio
    arr.sort(key=lambda x: (x.value/x.weight), reverse=True)
    
    # Result(value in Knapsack)
    final_value = 0.0

    for item in arr:
        # If adding Item won't overflow, add it completely
        if item.weight <= W:
            W -= item.weight
            final_value += item.value
        
        # If we can't add current Item, add fractional part of it
        else:
            final_value += item.value * W / item.weight
            break
        
    return final_value
        

if __name__ == '__main__':
    W = 50 # max allowed weight of bag
    
    arr = [Item(60,10), Item(100,20), Item(120, 30)]
    
    max_val = fractionalKnapsack(W, arr)
    
    print("Maximum value we can obtain = ", max_val)
    
    
# https://www.geeksforgeeks.org/fractional-knapsack-problem/
