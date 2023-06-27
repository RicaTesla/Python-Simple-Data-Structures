#1. initialization
numbers= [10, 20, 30, 40, 50]

#2. Accessing elements
print("Elements in the array: ")
for element in numbers:
    print(element)


#3. Searching an element
search_element=int(input("enter element to search:"))
if search_element in numbers:
    print(f"{search_element} is found in the numbers.")
else:
    print(f"sorry {search_element} not present")


#4. Sorting the array
sorted_numbers= sorted(numbers)
print("Sorted array: ")
for element in sorted_numbers:
    print(element)

#5. Inserting an element
insert_index=2
insert_value= int(input("Enter element to insert:"))
numbers.insert(insert_index, insert_value)
print(f"Numbers after inserting {insert_value} at index {insert_index}")


#6. Deleting an element
delete_value= int(input("Enter the element to be deleted: "))
numbers.remove(delete_value)
print(f"Numbers after deleting {delete_value}: {numbers}")

#7. Updating an element
update_index=1
update_value= int(input("Enter element to update:"))
numbers[update_index]=update_value
print(f"Numbers after updating element at index{update_index} with {update_value}: {numbers}")

#8. Traversing the array
print("Traversing the array using index:")
for i in range(len(numbers)):
    print(f"Element at index {i}: {numbers[i]}")