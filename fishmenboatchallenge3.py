import random

people_amount = int(input('How many fishmen you want? '))
boat_weight = int(input('How much weight can a boat take (between 50kg and 1 000 000kg) '))
people = []

for i in range(people_amount):
    people_weight = random.randint(50, 100)
    people.append(people_weight)
    
print(people)
people.sort(reverse = True)
print(people)

boat = 0
overweight = 0



for i in range(people[1]):
        while people != []:
                
                if people[0] > boat_weight:
                        heavy_people = people.pop(0)
                        overweight += 1
                        print('number of overweight people: ' + str(overweight))
                        print(people)
                        print('^ Our initial list of Fishermen without the overweight^')

                elif len(people) == 1:
                        boat += 1
                        print(people)
                        print(boat)
                        break

                elif people[0] == boat_weight:
                        boat += 1
                        new_people = people.pop(0)
                        print(people)
                        print(boat)
       
                elif (people[0] + people[-1]) <= boat_weight:
                        boat += 1
                        min_people = people.pop(-1)
                        new_people = people.pop(0)
                        print(people)
                        print(boat)

                elif (people[0] + people[-1]) > boat_weight:
                        new_people = people.pop(0)
                        boat += 1
                        print(people)
                        print(boat)
     
                else:
                        print('somethings wrong')
                        print(boat)
                        break
        break


       
print('Minimal number of boat rides required to move all the people: ' + str(boat))

