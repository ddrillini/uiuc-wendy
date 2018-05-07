import random
import msvcrt

# Holds a song's name and difficulty rating
class songItem:
	def __init__(self, s, r):
		self.songName = s
		self.rating = r

# Holds a song item and the name of the entrant who selected it
class hatItem:
	def __init__(self, i, e):
		self.song = i
		self.entrantName = e
		
# Full songlist. A song's "ID Number" is its index in this list.
songList = [songItem("A Castle Under Siege", 12),
 songItem("Act Beloved", 11),
 songItem("Arcadian (Castilian II)", 11),
 songItem("Arcanum Guardian", 14),
 songItem("Avalanche", 12),
 songItem("Bass 2 Bass (escalated scale mix)", 10),
 songItem("Beyond Her Garden", 11),
 songItem("Beyond the Boundary", 15),
 songItem("Blazing", 12),
 songItem("Castle on the Moon", 14),
 songItem("Chili Under", 12),
 songItem("Cirno's Perfect Math Class", 12),
 songItem("Cool Friends (Original Mix)", 10),
 songItem("Dance with Liquor", 12),
 songItem("Dawgs In Da House", 11),
 songItem("Deconstruction Star", 14),
 songItem("Disconnected Hardkore", 14),
 songItem("Djedefre", 10),
 songItem("Doppelganger", 13),
 songItem("Esoteric Symbolism", 11),
 songItem("Eternal Festival of Fantasy (Returning Home From The Sky ~ Sky Dream)", 14),
 songItem("Evil Railway", 14),
 songItem("Footquake", 15),
 songItem("For Lovers Not Fighters (Tsukasa Remix)", 11),
 songItem("For You", 11),
 songItem("Four-Dimensional Warp Device", 11),
 songItem("Give Back", 12),
 songItem("Grubby Cake", 13),
 songItem("Hengan Jizai", 11),
 songItem("IT IS SO", 10),
 songItem("Kung-Fu Empire", 11),
 songItem("La Samba de la Vida", 10),
 songItem("Last Imouto", 12),
 songItem("Liberated Liberater", 10),
 songItem("Light", 10),
 songItem("Love to Rise in the Summer Morning", 13),
 songItem("Magic Girl !!", 10),
 songItem("Maihime -buki-", 13),
 songItem("MASCARADA", 12),
 songItem("Mess", 11),
 songItem("Moriya Set 03 (The Road of the Misfortune God)", 10),
 songItem("Ninja Boy", 12),
 songItem("Otemba de Jane-yo", 13),
 songItem("Pachuriko (katsu+sumijun R&B HOUSE Revival)", 9),
 songItem("Paint it For", 11),
 songItem("Phantomystic", 12),
 songItem("Picturing the Past", 13),
 songItem("Portal", 10),
 songItem("Programmed Universe", 10),
 songItem("REASON for RED", 12),
 songItem("Remix 4", 11),
 songItem("Run with the Devil", 11),
 songItem("SAMBA de ASPEL", 11),
 songItem("Savior of the Sky", 12),
 songItem("Scarlet Eyes", 11),
 songItem("Scratch", 13),
 songItem("Shakunetsu Beach Side Bunny", 14),
 songItem("Shiva Nataraja", 12),
 songItem("Sleepyhead (ArtAttack Remix)", 11),
 songItem("Spark303-8", 12),
 songItem("Spinner", 14),
 songItem("Spring Sun", 12),
 songItem("Tell Me A Story (Compendium Mix)", 12),
 songItem("The Man With The Tuxedo", 10),
 songItem("The Mystery in Your Town", 11),
 songItem("The Sky of Sadness", 11),
 songItem("The Vampire Saga", 13),
 songItem("Throw Your Cards Down (Nhato Remix)", 11),
 songItem("Thunderclap", 9),
 songItem("Twin Ferrets", 11),
 songItem("Twinkle Wonderland", 9),
 songItem("Underwater Regret", 10),
 songItem("Unemotional Skyscraper", 10),
 songItem("Unidentified Flying Dance Fantasy", 9),
 songItem("Vestigal Fusion Factory", 11),
 songItem("Voyage 1969", 11),
 songItem("Want U Back", 9),
 songItem("Wild Card", 13)]
 
# Holds all song picks from entrants
hat = [] 

# Used for card-draw style games		
def cardDraw(cardCount):
	cardDraws = []
	for x in range(0,cardCount):
		selectedSongID = random.randrange(0,len(songList))
			
		# Re-select until a unique song is chosen
		while selectedSongID in cardDraws:
			selectedSongID = random.randrange(0,len(songList))
			
		cardDraws.append(selectedSongID)
		print songList[selectedSongID].songName

	print ""		

# Helper method to determine if a chart of a specified difficulty is in the hat.
# Returns True if a hat item is available. False if not.
def checkForLevel(level):
	for item in hat:
		if item.song.rating == level:
			return True
	return False
 
# Draw a song from the full songlist with the specified level.
# Pass in 0 to draw from full songlist.
def getTiebreaker(level):
	selectItem = songItem("", 0)
	selectItem = songList[random.randrange(0,len(songList))]
	while selectItem.rating != level and level != 0:
		selectItem = songList[random.randrange(0,len(songList))]
	print "  " + (selectItem.songName)

# Randomly select a difficulty level using the given weights
# Weight arguments are in integer-based percentages (I.E. 1 = 1%)	
def getWeightedDifficulty(weight9, weight10, weight11, weight12, weight13):
	diffLevel = random.randrange(0,100)
	if diffLevel <= weight9 and weight9 != 0:
		return 9
	elif diffLevel <= weight9 + weight10 and weight10 != 0:
		return 10
	elif diffLevel <= weight9 + weight10 + weight11 and weight11 != 0:
		return 11
	elif diffLevel <= weight9 + weight10 + weight11 + weight12 and weight12 != 0:
		return 12
	elif weight13!= 0:
		return 13
	
# Draw a song from the hat with the specified difficulty level.
# Removes the pick and all picks of the same song from the hat afterwards.
def drawFromHat(level):
	if checkForLevel(level):
		selectItem = hatItem(songItem("", 0), "")

		# Draw random songs until one with the specified difficulty is picked.
		while selectItem.song.rating != level:
			selectItem = hat[random.randrange(0,len(hat))]
		songPicked = selectItem.song.songName
		print "  " + songPicked
			
		# Remove it and all selections of the same song from the hat.
		hat.remove(selectItem)		
		for item in hat:
			if (item.song.songName == songPicked):
				hat.remove(item)
		
		# Second pass needed due to list/for loop structure.
		for item in hat:
			if (item.song.songName == songPicked):
				hat.remove(item)		
	else:
		print "  Invalid difficulty level. No appropriate hat items exist."
	
# Add an entrant's song selections to the hat	
def addEntrant(entrantName, songID1, songID2):
	if songID1 < len(songList) and songID2 < len(songList):
		hat.append(hatItem(songList[songID1], entrantName))
		hat.append(hatItem(songList[songID2], entrantName))
		print "  Entrant added."
	else:
		print "  Invalid SongID. Entrant not added. Please try again."
	
# Removes all submissions by a given entrant. 
# Used when a competitor is eliminated from the tournament.	
def removeEntrant(e):
	i=0
	
	# Loop through and remove a song selected by the entrant
	for item in hat:
		if item.entrantName == e:
			hat.remove(item)
			i += 1
			break
			
	# Due to for loop and list structure, one pass will miss an entry
	# if they are placed consecutively (which they usually are).
	# Do another pass to make sure entries are removed.
	for item in hat:
		if item.entrantName == e:
			hat.remove(item)
			i += 1
			break
			
	print "  Player '{0}' eliminated. {1} hat items removed.".format(e,i)	
		
help = """
 Press 'a' to add to the hat. 
 Press 'r' to remove entrants from the hat. 
 Press 'v' to view the hat contents.
 
 Press 's' to view the songlist and ID numbers.
 
 Press '1', '2', '3', or '4' to generate songs for the appropriate round.
 Press 't' to generate a tiebreaker.
 Press 'c' for a card-draw round.
 
 Press 'q' to quit.
 """
 
print "DoubleScott: Random song generator for U of I tournament. Songlist current as of 11/06/2014."
print help
ch = 'a'

# Main menu
while True:
	print "Enter command (press 'h' for help): "
	ch = msvcrt.getch()
	diff = 0
	
	# 'a' - Add Entrant
	if ch == 'a':
		inName = raw_input(" Enter entrant name: ")
		inSong1 = int(raw_input(" Enter songID number for choice 1: "))
		inSong2 = int(raw_input(" Enter songID number for choice 2: "))
		addEntrant(inName, inSong1, inSong2)
		
	# 'r' - Remove Entrant
	elif ch == 'r':
		inName = raw_input(" Enter entrant name to remove: ")
		removeEntrant(inName)
		
	# '1', '2', '3', '4' - Generate hat pick for specified round
	# If no hat item exists in the appropriate range, pick within range randomly from full songlist
	elif ch == '1':
		diff = getWeightedDifficulty(50, 50, 0, 0, 0)
		if checkForLevel(9) or checkForLevel(10):
			while not (checkForLevel(diff)):
				diff = getWeightedDifficulty(50, 50, 0, 0, 0)
			drawFromHat(diff)
		else:
			print " No appropriate hat items for round 1 exist. Drawing from full songlist."
			getTiebreaker(diff)
	elif ch == '2':
		diff = getWeightedDifficulty(20, 30, 50, 0, 0)
		if checkForLevel(9) or checkForLevel(10) or checkForLevel(11):
			while not (checkForLevel(diff)):
				diff = getWeightedDifficulty(20, 30, 50, 0, 0)
			drawFromHat(diff)
		else:
			print " No appropriate hat items for round 2 exist. Drawing from full songlist."
			getTiebreaker(diff)
	elif ch == '3':
		diff = getWeightedDifficulty(0, 20, 30, 50, 0)
		if checkForLevel(10) or checkForLevel(11) or checkForLevel(12):
			while not (checkForLevel(diff)):
				diff = getWeightedDifficulty(0, 20, 30, 50, 0)
			drawFromHat(diff)
		else:
			print " No appropriate hat items for round 3 exist. Drawing from full songlist."
			getTiebreaker(diff)
	elif ch == '4':
		diff = getWeightedDifficulty(0, 0, 20, 30, 50)
		if checkForLevel(11) or checkForLevel(12) or checkForLevel(13):
			while not (checkForLevel(diff)):
				diff = getWeightedDifficulty(0, 0, 20, 30, 50)
			drawFromHat(diff)
		else:
			print " No appropriate hat items for round 4 exist. Drawing from full songlist."
			getTiebreaker(diff)
			
			
	# 't' - Draw Tiebreaker
	elif ch == 't':
	
		# Specify round weights to use. If tiebreaker is in final four, use 0 for unweighted random.
		inRound = int(raw_input(" Select round (0 for unweighted full songlist random): "))
		if inRound == 0:
			getTiebreaker(0)
		elif inRound == 1:
			getTiebreaker(getWeightedDifficulty(50, 50, 0, 0, 0))
		elif inRound == 2:
			getTiebreaker(getWeightedDifficulty(20, 30, 50, 0, 0))
		elif inRound == 3:
			getTiebreaker(getWeightedDifficulty(0, 20, 30, 50, 0))
		elif inRound == 4:
			getTiebreaker(getWeightedDifficulty(0, 0, 20, 30, 50))
	
	# 'c' - Card Draw
	elif ch == 'c':
		inCardCount = int(raw_input(" Specify number of cards to draw (Standard amounts are 5 and 7): "))
		cardDraw(inCardCount)
	
	# 'h' - Print Help
	elif ch == 'h':
		print help
		
	# 's' - Print Songlist	
	elif ch == 's':
		i=0
		for items in songList:
			print i, items.songName, items.rating
			i += 1
			
	# 'v' - View Hat
	elif ch == 'v':
		if len(hat) == 0:
			print " Hat is empty."
		else:
			for items in hat:
				print items.song.songName, items.song.rating, items.entrantName
				
	# 'q' - Quit
	elif ch == 'q':
	
		# Confirm
		print " THIS WILL CLEAR ALL HAT DATA. ARE YOU SURE? (Press y to quit)"
		if msvcrt.getch() == 'y':
			break
			