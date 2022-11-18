

dict = [{'name': 'Jurre', 'age': '39', 'height': '184'},
        {'name': 'Pieter', 'age': '45', 'height': '190'},
        {'name': 'Klaas', 'age': '28', 'height': '178'}]

fieldnames = list(dict[0].keys())
list_of_dict = []
for dict in dict:
    if dict['name'] != 'Jurre':
        list_of_dict.append(dict)
print(list_of_dict)

# with open('test.csv', 'w', newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     i = 0
#     while i < len(dict):
#         writer.writerow(dict[i])
#         i += 1
#     f.close()
