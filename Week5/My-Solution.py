input_data = input()
final_data = {}

while input_data:
    (first,second,sets) = input_data.split(':')
    (first_set,second_set) = (0,0)
    (first_game,second_game) = (0,0)
    (best_5,best_3) = (0,0)

    for set in sets.split(','):
        tempValue = set.split('-')
        tempValue[0] = int(tempValue[0])
        tempValue[1] = int(tempValue[1])
        
        if tempValue[0] > tempValue[1]:
            first_set = first_set = 1
        else:
            second_set = second_set + 1
        
        first_game = first_game + tempValue[0]
        second_game = second_game + tempValue[1]
    
    if first_set >= 3:
        best_5 = best_5 + 1
    elif first_set < 3:
        best_3 = best_3 +1

    for player in [first,second]:
        try:
            final_data[player]
        except:
            final_data[player] = [0,0,0,0,0,0]
        
        if player == first:
            final_data[player][0] = final_data[player][0] + best_5
            final_data[player][1] = final_data[player][1] + best_3
            final_data[player][2] = final_data[player][2] + first_set
            final_data[player][3] = final_data[player][3] + first_game
            final_data[player][4] = final_data[player][4] + second_set
            final_data[player][5] = final_data[player][5] + second_game

        if player == second:
            final_data[player][2] = final_data[player][2] + second_set
            final_data[player][3] = final_data[player][3] + second_game
            final_data[player][4] = final_data[player][4] + first_set
            final_data[player][5] = final_data[player][5] + first_game
        
    input_data = input()

final_data=sorted(final_data.items(),key=lambda t:t[1],reverse=True)

# for element in final_data:
#     print(element[0],element[0][1],element[0][2],element[0][3],element[0][4],element[0][5])
print(final_data)
    
