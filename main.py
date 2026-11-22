the_list = [5,4,6,3,2,5,3]
target = int(input("Input the target number"))
the_next_neibour_calculation_target_completed = False
one_number_comparing = 0
comparing_other_numbers = 1


 
while True:
    comparing_other_numbers_not_changed = True
    
    if comparing_other_numbers <= len(the_list) -1:
        the_next_neibour_calculation = the_list[one_number_comparing] + the_list[comparing_other_numbers]

    
    
    if the_next_neibour_calculation == target:
        print("YES")
        break

    if comparing_other_numbers_not_changed == True and comparing_other_numbers <= len(the_list) - 1 and len(the_list) >=2:
        comparing_other_numbers_not_changed = False
        comparing_other_numbers+=1
        continue

        

    elif comparing_other_numbers>len(the_list) - comparing_other_numbers and len(the_list) >=2:
        the_list.pop(one_number_comparing)
        the_next_neibour_calculation_target_completed = True
        one_number_comparing = 0
        comparing_other_numbers = 1
        continue
    
    
    else:
        print("NO")
        break
    

    
    
