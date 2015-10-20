-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament;
-- Connect to database
\c tournament;

-- Players and Matches table,
-- Players table stores name of players
-- Matches table stores the result of a match

DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS players;

CREATE TABLE players (
	id serial primary key,
	name text
);

CREATE TABLE matches (
	id serial primary key,
	winner int references players(id),
	loser int references players(id)
);
