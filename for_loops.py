# loops for loops and while loops
# for loops are used to iterate through data
# syntax for variable_name in name_of_data_collection_variable

shopping_list = ["eggs", "milk", "supermalt"]
print(shopping_list)

# for items in shopping_list:
#     if items == "milk":
#         print(items)
#         break

    for items in shopping_list:
        if items == "milk":
            print(items)
            continue

        # shopping_list = {"protein": "eggs", "dairy": "milk", "drink": "supermalt"}
# print(shopping_list)

# for keys in shopping_list:
#     if keys == "Protein":
#         print(keys)
