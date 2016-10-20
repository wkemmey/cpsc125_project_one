from collections import defaultdict

trains = [
        ['Vancouver', 'Seattle'], 
        ['Vancouver', 'Calgary'], 
        ['Calgary', 'Seattle'], 
        ['Calgary', 'Winnipeg'], 
        ['Calgary', 'Helena'], 
        ['Helena', 'Seattle'], 
        ['Portland', 'Seattle'], 
        ['Portland', 'San Francisco'], 
        ['Portland', 'Salt Lake City'], 
        ['Salt Lake City', 'San Francisco'], 
        ['Los Angeles', 'San Francisco'], 
        ['Los Angeles', 'Las Vegas'], 
        ['Los Angeles', 'Phoenix'], 
        ['Las Vegas', 'Salt Lake City'], 
        ['Salt Lake City', 'Helena'], 
        ['Helena', 'Winnipeg'], 
        ['Helena', 'Denver'], 
        ['Salt Lake City', 'Denver'], 
        ['Phoenix', 'Santa Fe'], 
        ['Los Angeles', 'El Paso'], 
        ['Phoenix', 'El Paso'], 
        ['El Paso', 'Santa Fe'], 
        ['Santa Fe', 'Denver'], 
        ['Helena', 'Duluth'], 
        ['Helena', 'Omaha'], 
        ['Winnipeg', 'Duluth'], 
        ['Winnipeg', 'Sault St Marie'], 
        ['Denver', 'Omaha'], 
        ['Denver', 'Kansas City'], 
        ['Denver', 'Oklahoma City'], 
        ['Santa Fe', 'Oklahoma City'], 
        ['El Paso', 'Oklahoma City'], 
        ['El Paso', 'Dallas'], 
        ['El Paso', 'Houston'], 
        ['Houston', 'Dallas'], 
        ['Dallas', 'Oklahoma City'], 
        ['Oklahoma City', 'Kansas City'], 
        ['Omaha', 'Kansas City'], 
        ['Omaha', 'Duluth'], 
        ['Duluth', 'Sault St Marie'], 
        ['Duluth', 'Toronto'], 
        ['Duluth', 'Chicago'], 
        ['Omaha', 'Chicago'], 
        ['Dallas', 'Little Rock'], 
        ['Oklahoma City', 'Little Rock'], 
        ['Houston', 'New Orleans'], 
        ['New Orleans', 'Little Rock'], 
        ['Little Rock', 'Saint Louis'], 
        ['Kansas City', 'Saint Louis'], 
        ['Little Rock', 'Nashville'], 
        ['Nashville', 'Saint Louis'], 
        ['Saint Louis', 'Chicago'], 
        ['Sault St Marie', 'Toronto'], 
        ['Sault St Marie', 'Montreal'], 
        ['Montreal', 'Toronto'], 
        ['Montreal', 'Boston'], 
        ['Montreal', 'New York'], 
        ['Toronto', 'Pittsburgh'], 
        ['Toronto', 'Chicago'], 
        ['Boston', 'New York'], 
        ['New York', 'Pittsburgh'], 
        ['New York', 'Washington'], 
        ['Pittsburgh', 'Chicago'], 
        ['Pittsburgh', 'Saint Louis'], 
        ['Pittsburgh', 'Nashville'], 
        ['Pittsburgh', 'Raleigh'], 
        ['Pittsburgh', 'Washington'], 
        ['Washington', 'Raleigh'], 
        ['Raleigh', 'Nashville'], 
        ['Nashville', 'Atlanta'], 
        ['Atlanta', 'Raleigh'], 
        ['Raleigh', 'Charleston'], 
        ['Atlanta', 'New Orleans'], 
        ['Atlanta', 'Charleston'], 
        ['Miami', 'Charleston'], 
        ['Miami', 'Atlanta'], 
        ['Miami', 'New Orleans']
        ]

tickets = [
        ['Los Angeles',    'New York',      21], 
        ['Duluth',         'Houston',        8], 
        ['Sault St Marie', 'Nashville',      8], 
        ['New York',       'Atlanta',        6], 
        ['Portland',       'Nashville',     17], 
        ['Vancouver',      'Montreal',      20], 
        ['Duluth',         'El Paso',       10], 
        ['Toronto',        'Miami',         10], 
        ['Portland',       'Phoenix',       11], 
        ['Dallas',         'New York',      11], 
        ['Calgary',        'Salt Lake City', 7], 
        ['Calgary',        'Phoenix',       13], 
        ['Los Angeles',    'Miami',         20], 
        ['Winnipeg',       'Little Rock',   11], 
        ['San Francisco',  'Atlanta',       17], 
        ['Kansas City',    'Houston',        5], 
        ['Los Angeles',    'Chicago',       16], 
        ['Denver',         'Pittsburgh',    11], 
        ['Chicago',        'Santa Fe',       9], 
        ['Vancouver',      'Santa Fe',      13], 
        ['Boston',         'Miami',         12], 
        ['Chicago',        'New Orleans',    7], 
        ['Montreal',       'Atlanta',        9], 
        ['Seattle',        'New York',      22], 
        ['Denver',         'El Paso',        4], 
        ['Helena',         'Los Angeles',    8], 
        ['Winnipeg',       'Houston',       12], 
        ['Montreal',       'New Orleans',   13], 
        ['Sault St Marie', 'Oklahoma City',  9],
        ['Seattle',        'Los Angeles',    9]
        ]

# this will initialize board as an empty dictionary, where each value is a set
board = defaultdict(set)

def convert_to_graph(board, trains):
  for train in trains:
    first_city = train[0]
    second_city =  train[1]
    board[first_city].add(second_city)
    board[second_city].add(first_city)

def find_path(board, first_city, second_city):
  return True    # replace this line with your code

def calculate_score(board, tickets):
  score = 0
  for ticket in tickets:
    if find_path(board, ticket[0], ticket[1]):
      score = score + ticket[2]
    else:
      score = score - ticket[2]
  return score

# main

convert_to_graph(board, trains)
score = calculate_score(board, tickets)
print("The score is: {0}".format(score))
