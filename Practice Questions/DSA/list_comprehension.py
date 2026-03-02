list = [ [23,4,5],[3,4,5],[3,6,7]]

flattened_list = [items for sublist in list for items in sublist]
print(flattened_list)

















Festivals = [ [ "Holi"] ,["Eid"] , ["Dushhera"] ]

first_word = [festival[0][0] for festival in Festivals ]
print(first_word)














numbers = [ 2 ,3 ,5 , 6 ,7 ,8 ,9]

square_numbers = [ num**2 for num in numbers if num%2 == 0]
print(square_numbers)















