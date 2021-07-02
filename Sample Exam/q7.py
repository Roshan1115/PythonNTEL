input_Line = input()
input_List = []

while input_Line:
    input_List.append(input_Line)
    input_Line = input()

for sentence in input_List[2:len(input_List):3]:
    print(sentence)



