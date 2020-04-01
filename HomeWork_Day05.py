file = open("epldata_final.csv", encoding='utf-8')
s = file.read()
dataList = s.split("\n")[1:-1]
data = []
for player in dataList:
    data.append(player.split(","))
#now, data variable is a list of list
print(data)

#-------   1.	Create a list of unique club for this dataset. Then, create a dictionary to show how many players each club has.\
my_list = list(map(lambda x: x[1], data))
print(my_list)

print('=== Tạo 1 dictionay chứa tên câu lạc bộ, không bị trùng ===')
club_dictionay = dict.fromkeys(my_list)
print(club_dictionay)


dictionay_club_with_playes = club_dictionay.copy()
print('=== Đếm số lượng cầu thủ trong câu lạc bộ ===')
for item in dictionay_club_with_playes:
  dictionay_club_with_playes[item] = 0
  for raw_data in data:
    if item == raw_data[1]:
      dictionay_club_with_playes[item] = dictionay_club_with_playes[item] + 1
print(dictionay_club_with_playes)

#-------  2.	Who is the youngest, oldest player ?
# chuyển đổi thành list các tuổi và tìm min
list_age_of_players = list(map(lambda x: int(x[2]), data))

min_age_of_players = min(list_age_of_players)
max_age_of_players = max(list_age_of_players)
#2.2 Who is the youngest player?
players_with_min_age = list(filter(lambda x: int(x[2]) == min_age_of_players, data))
print('The youngest player is:')
for player in players_with_min_age:
  print(' + {} from {}, {} years old'.format(player[0], player[1], player[2]))

#2.2 Who is the oldest player?
players_with_max_age = list(filter(lambda x: int(x[2]) == max_age_of_players, data))
print('The oldest player is:')
for player in players_with_max_age:
  print(' + {} from {}, {} years old'.format(player[0], player[1], player[2]))
  
# using sort
data.sort(key = lambda(x:int(x[2])))
  
#-------  3.	What is the average age of all players in this dataset. What is the average age for each club ?   --------
avg = sum(list_age_of_players) /len(list_age_of_players)
print(list_age_of_players)
print("The average is ", round(avg,2)) 

#3.1 What is the average age for each club ?  
dictionay_club_with_age_of_player = club_dictionay.copy()
for item in dictionay_club_with_age_of_player:
  dictionay_club_with_age_of_player[item] = [0, 0, 0, 0.0] # total_age, total_players, average, market_value 
  for raw_data in data:
    if item == raw_data[1]:
      dictionay_club_with_age_of_player[item][0] = dictionay_club_with_age_of_player[item][0] + int(raw_data[2]) #total_age
      dictionay_club_with_age_of_player[item][1] = dictionay_club_with_age_of_player[item][1] + 1 #total_players
      dictionay_club_with_age_of_player[item][2] = 0 #average, will be calculate later
      dictionay_club_with_age_of_player[item][3] = dictionay_club_with_age_of_player[item][3] + float(raw_data[5]) #market_value
      
print('The average age for each club: ')

for item in dictionay_club_with_age_of_player:
  club_name = item
  total_age, total_players,_, _ = dictionay_club_with_age_of_player[item]
  avg = total_age / total_players
  dictionay_club_with_age_of_player[item][2] = round(avg, 2)
  print('  + {}: {}'.format(club_name, round(avg, 2)))

#--------- 4.	Sort the club by their average age ?
def sortByAverageAge(lst):
  total_age, total_players, avg, _ = lst[1]
  return avg
  
my_list = list(dictionay_club_with_age_of_player.items())
my_list.sort(key=sortByAverageAge)

print('The average age for each club after do sort ')
for item in my_list:
  club_name = item[0]
  total_age, total_players, avg, _ = item[1]
  print('  + {}: {}'.format(club_name, avg))

#-----------5.	What is the total market value of all players in big 6 club ? What is the total market value of all players not in big 6 club ?
def sortByMarketValue (lst):
  _, _, _, marketValue = lst[1]
  return marketValue
  
my_list.sort(key=sortByMarketValue, reverse=True)
lst_of_marketValue = list(map(lambda x: x[1][3], my_list))
total_market_value_from_6_big_clubs = sum(lst_of_marketValue[0:5])
print('The total market value of all players in big 6 clubs is: {}'.format(total_market_value_from_6_big_clubs))

#5.1	What is the total market value of all players not in big 6 club ?
total_market_value_from_others_clubs = sum(lst_of_marketValue[6:])
print('The total market value of all players from clubs is: {}'.format(total_market_value_from_others_clubs))

