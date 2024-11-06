# Sample list
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Reversing a list
reversed_data = data[::-1]
print("Reversed:", reversed_data)

# 2. Slicing with a step
step_slice = data[::2]  # Every second element
print("Every second element:", step_slice)

# 3. Slicing with a negative step (reverse slice)
reverse_step_slice = data[8:2:-2]  # Slices from index 8 to 2 with step -2
print("Reverse step slice:", reverse_step_slice)

# 4. Slicing with start and end indices
range_slice = data[3:7]  # Elements from index 3 to 6
print("Elements from index 3 to 6:", range_slice)

# 5. Slicing with a combination of start, end, and step
combined_slice = data[1:9:3]  # Elements from index 1 to 8 with step 3
print("Elements from index 1 to 8 with step 3:", combined_slice)
