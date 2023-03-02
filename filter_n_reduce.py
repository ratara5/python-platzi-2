numbers = [1, 2, 3, 4, 5]
new_numbers = filter(lambda x: x % 3 == 0, numbers) #when works with integers, filter doesn't mofidy the original list, map doesn't do it too

print(list(new_numbers))

foods=[
    {
        'name': 'meat',
        'type': 'no vegetarian'
    },
    {
        'name': 'popcorn',
        'type': 'vegetarian'
    },
    {
        'name': 'potato',
        'type': 'vegetarian'
    }
]

new_foods = filter(lambda food: food['type'] == 'vegetarian', foods)
print(list(new_foods))

###############################
matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

matches_win = list(filter(lambda match: match['home_team_result'] == 'Win', matches)) #when works with dictionaries, filter doesn't mofidy the original list,
teams_win = map(lambda match_win: match_win['home_team'], matches_win) 
print(list(teams_win))

######################
print('\nReduce')
import functools
numbers = [1, 2, 3, 4]

result = functools.reduce(lambda counter, item: counter + item, numbers )
print(result)

"""+----------+------+----+------+
   |ITERATION COUNTER ITEM RETURN| // ITEM is the respective element of numbers by the iteration
   +----------+------+----+------+
    1           0       1   0+1=1 -> It's assigned to counter
    2           1       2   1+2=3
    3           3       3   3+3=6
    4           6       4   6+4=10 -> It's the final result
"""