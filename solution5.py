def knapsack(items, capacity, index = 0):
    if (index >= len(items) or len(items) == 0 or index < 0 or capacity <= 0):
        return 0
    else:
        item_weight = items[index]["weight"]
        item_value = items[index]["value"]
        # If the weight of the current item is greater than remaining space in backpack
        if (item_weight > capacity):
            # Exclude this item and move to next one
            return knapsack(items, capacity, index + 1)
        else:
            # Include this item and move to next one
            return max(knapsack(items, capacity-item_weight, index+1)+item_value, knapsack(items, capacity, index+1))
        
# Testing with example from problem statement
# Example usage:
items = [{"weight": 5, "value": 2}, {"weight": 4, "value": 3}, {"weight": 3, "value": 20}]
print(knapsack(items,8))


