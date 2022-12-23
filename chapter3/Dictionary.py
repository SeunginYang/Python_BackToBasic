player = {
    'name' : 'Chris',
    'age' : 33,
    'alive' : True,
    'fav_food' : ["chicken", "Pizza"]
}

print(player)
print(player.get('age'))
print(player.get('fav_food'))

player.pop('age')
print(player)

player['exp'] = 1500
print(player)

player['fav_food'].append("Ramen")
print(player.get('fav_food'))

player['fav_food'].remove("Pizza")
print(player.get('fav_food'))