list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
polovina = len(list_players) // 2

first_team = list_players[:polovina]
second_team = list_players[polovina:]

print(first_team)
print(second_team)
