### Run Swiss system tournament

1. If necessary, [install Python 2](https://www.python.org/downloads/), PostgreSQL, and the psql command line interface
2. Alternativly you can download Vagrant and the [fullstack-nanodegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm) from Udacity as you dev environment. This environment has everything you need already pre-installed
3. Run psql and install the database and tables with the inluded sql file (\i tournament.sql)
4. The tournament.py file includes all functions to record and manage games, and to find the next pairings
5. You can test the functionality of the tournament.py file by running the tournament_test.py file


### tournament.py functions

1. registerPlayer(name)
Adds a player to the tournament by putting an entry in the database. The database should assign an ID number to the player. Different players may have the same names but will receive different ID numbers.

2. countPlayers()
Returns the number of currently registered players. This function should not use the Python len() function; it should have the database count the players.

3. deletePlayers()
Clear out all the player records from the database.

4. reportMatch(winner, loser)
Stores the outcome of a single match between two players in the database.

5. deleteMatches()
Clear out all the match records from the database.

6. playerStandings()
Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has.

7. swissPairings()
Given the existing set of registered players and the matches they have played, generates and returns a list of pairings according to the Swiss system. Each pairing is a tuple (id1, name1, id2, name2), giving the ID and name of the paired players. For instance, if there are eight registered players, this function should return four pairings. This function should use playerStandings to find the ranking of players.


### Included files

1. tournament.sql  - this file will be used to create the databases and tables needed.
2. tournament.py - this file included a librabry of function to control the came
3. tournament_test.py - this is a client program which tests the tournament.py file.
