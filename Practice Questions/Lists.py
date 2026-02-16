heroes = [ 'spiderman' , 'thor' , 'hulk' , 'balveer' , 'chotabheem' , 'mighty raju']


print(len(heroes))


heroes.append('black panther')
print(heroes)



heroes.remove('black panther')
hulk_index = heroes.index('hulk')       
heroes.insert(hulk_index + 1, 'black panther')



heroes[heroes.index('hulk')] = 'doctor strange'
heroes[heroes.index('thor')] = 'doctor strange'
print(heroes)




heroes.sort()
print(heroes)