# Write your win_percentage function here:
def win_percentage(wins, loses):
  total = wins + loses
  won_games = (wins/total) * 100
  
  return won_games

print(win_percentage(5, 5))
print(win_percentage(10, 0))