from django.contrib.auth.models import User
from adventure.models import Player, Room

import random


Room.objects.all().delete()

room_templates = [
  {"title": "Foyer", "description": """Dim light filters in from the south. Dusty passages run north and east."""},
  {"title": "Narrow Passage", "description": """The narrow passage bends here from west to north. The smell of gold permeates the air."""},
  {"title": "Treasure Chamber", "description": """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied byearlier adventurers. The only exit is to the south."""},
  {"title": "Torture Room", "description": """ Here can be heard screams and cries from living souls ready to join the underworld."""},
  {"title": "The Banquet Room", "description": """Come fill up your bellies, here can be found all you need to replenish your energy level"""},
  {"title": "Armory", "description": """Here you can find any kind of weapons:knives, swords, hammers, bazookas, ... Enough to kill your opponent or even yourself in the process"""},
  {"title": "Single room", "description": """Can accommodate 1 person"""},
  {"title": "Double room", "description": """Can accommodate 2 person"""},
  {"title": "Triple room", "description": """Can accommodate 3 person"""},
  {"title": "Quad room", "description": """Can accommodate 4 person"""},
]

rooms = []

for i in range(10):

  if i == 0:
    first_row = []
    for j in range(10):

      choice = random.sample(room_templates, 1)[0]
      # print(choice['title'])
      # print(choice['description'])
      room = Room(title=choice['title'], description=choice['description'])
      # print(room)
      first_row.append(room)
      room.save()
      if j == 0:
        continue
      else:
        first_row[j].connectRooms(first_row[j-1], "w")
        first_row[j-1].connectRooms(first_row[j], "e")
    print(first_row)
    rooms.append(first_row)
    print(rooms)
  else:
    ith_row = []
    for j in range(10):
      choice = random.sample(room_templates, 1)[0]
      room = Room(title=choice['title'], description=choice['description'])
      ith_row.append(room)
      room.save()
      if j == 0:
        ith_row[j].connectRooms(rooms[i-1][j], "s")
        rooms[i-1][j].connectRooms(ith_row[j], "n")
      else:
        ith_row[j].connectRooms(ith_row[j-1], "w")
        ith_row[j-1].connectRooms(ith_row[j], "e")
        ith_row[j].connectRooms(rooms[i-1][j], "s")
        rooms[i-1][j].connectRooms(ith_row[j], "n")
    rooms.append(ith_row)

#Entrance to the network of rooms - most South
r_outside = Room(title="Outside Cave Entrance", description="North of you, the cave mount beckons")

r_outside.connectRooms(rooms[0][0], "n")
rooms[0][0].connectRooms(r_outside, "s")

#Overlook to the outside - Most North
r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

r_overlook.connectRooms(rooms[9][9], "s")
rooms[9][9].connectRooms(r_overlook, "n")



players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()

