def find_common_participants(team_1=input().split(", "), team_2=input().split(", ")):
    repeat = [x for x in team_1 if x in team_2]
    repeat.sort()
    return repeat
print(find_common_participants())
