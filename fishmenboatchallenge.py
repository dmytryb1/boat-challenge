people = [120, 100, 100, 100, 100, 100, 90, 80, 60, 50, 50, 50, 40, 20, 10, 10]
boat = 0
overweight = 0
print('Initial list')
print(people)

for i in range(people[1]):
    while people != []:
        if people[0] > 100:
#            print('real first if')
            heavy_people = people.pop(0)
            overweight += 1
            print('number of overweight people: ' + str(overweight))
#            print('real first if end')
        elif people[0] == 100:
#            print('first if start')
            boat += 1
            new_people = people.pop(0)
#            print(people)
#            print(i)
#            print('first if end')
       
        elif (people[0] + people[i + 1]) > 100:
#            print('second if start')
#            print(str(people[0]) + ' ' +  str(people[i]) + ' is too heavy')
            i = i + 1
#            print('second if end')
            
        elif (people[0] + people[i + 1]) <= 100:
#            print('third if start')
            boat += 1
            min_people = people.pop(i+1)
            new_people = people.pop(0)
#            print(people)
#            print(boat)
            i = 0
#            print('third if end')
      
     
        else:
            print('somethings wrong')
            break

        
print('Minimal number of boat rides required to move all the people: ' + str(boat))

