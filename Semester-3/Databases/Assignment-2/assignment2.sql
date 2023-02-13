use "tennis-tournament";

-- INSERT

INSERT INTO Player
	(id, name, age, rank, points, country, date_of_birth)
VALUES
	(1, 'Simona Halep', 31, 3, 1740, 'Romania', '1991-09-27'),
	(2, 'Serena Williams', 41, 5, 1650, 'USA', '1981-09-26'),
	(3, 'Maria Sharapova', 35, 2, 1820, 'Russia', '1987-04-19'),
	(4, 'Angelique Kerber', 34, 4, 1690, 'Germany', '1988-01-18'),
	(5, 'Ashleigh Barty', 26, 1, 2120, 'Australia', '1996-04-26'),
	(6, 'Karolina Pliskova', 30, 6, 1600, 'Czech Republic', '1992-03-21'),
	(7, 'Madison Keys', 27, 7, 1580, 'USA', '1995-02-17'),
	(8, 'Sorana Cirstea', 32, 8, 1450, 'Romania', '1990-04-07');



INSERT INTO Coach
	(id, name, player_id, age, country)
VALUES
	(1, 'Darren Cahill', 1, 18, 'Australia'),
	(2, 'Andre Agassi', 4, 37, 'USA'),
	(3, 'Boris Becker', NULL, 46, 'Germany'),
	(4, 'Nick Bollettieri', 3, 32, 'USA'),
	(5, 'Patrick Mouratoglou', 2, 35, 'Russia'),
	(6, 'Andrei Popescu', NULL, 23, 'Romania'),
	(7, 'Mara Valean', 8, 20, 'Romania'),
	(8, 'Ilinca Petrila', 1, 20, 'Romania');

INSERT INTO Playing_category
	(id, category)
VALUES
	(1, 'women singles'),
	(2, 'women doubles');


INSERT INTO Tournament_type
	(id, type_name, points)
VALUES
	(1, 'Grand Slam', 2000),
	(2, 'WTA Premier Mandatory', 1000),
	(3, 'WTA Premier 5', 900),
	(4, 'Premier', 470),
	(5, 'WTA 250', 280);


INSERT INTO Tournament
	(id, name, country, tournament_type_id)
VALUES
	(1, 'Australian Open', 'Australia', 1),
	(2, 'Roland Garros', 'France', 1),
	(3, 'Indian Wells', 'USA', 2),
	(4, 'Miami Open', 'USA', 2),
	(5, 'Transylvania Open', 'Romania', 5),
	(6, 'Qatar Open', 'Qatar', 3),
	(7, 'Dubai Tennis Championships', 'Dubai', 4);


INSERT INTO Tournament_registration
	(player_id, tournament_id)
VALUES
	(8, 1),
	(1, 2),
	(7, 5),
	(1, 7),
	(3, 1),
	(2, 7),
	(6, 5),
	(4, 3),
	(5, 4),
	(1, 5),
	(1, 3),
	(3, 3),
	(3, 7),
	(7, 7),
	(7, 6);

INSERT INTO Tournament_registration
VALUES 
	(9, 1); -- violates referential integrity constraints


INSERT INTO Tournament_playing_category
	(tournament_id, playing_category_id)
VALUES
	(1, 1),
	(1, 2),
	(2, 1),
	(3, 1),
	(4, 2), 
	(5, 1),
	(6, 1), 
	(7, 1);


INSERT INTO Fan
	(id, name, age, country, nb_of_matches_attended)
VALUES
	(1, 'Alexandra', 19, 'Romania', 10),
	(2, 'Mara', 25, 'Germany', 2),
	(3, 'Dan', 20, 'USA', 9),
	(4, 'Andrei', 30, 'Romania', 15);


INSERT INTO Fanclub
	(id, name, number_of_fans, capacity, site_link)
VALUES
	(1, 'Sharapova Fanclub', 20, 50, 'www.a.ro'),
	(2, 'Halep Fanclub', 145, 150, 'www.halepfanclub.ro'),
	(3, 'Barty Fanclub', 100, 100, 'www.bartyfanclub.com'),
	(4, 'Pliskova Fanclub', 35, 150, NULL),
	(5, 'Kerber Fanclub', 50, 100, NULL);


INSERT INTO Fan_of_player
	(fan_id, player_id, fanclub_id)
VALUES 
	(1, 1, 2),
	(4, 1, 2),
	(2, 4, 5),
	(3, 6, 4);

SELECT * FROM Player;
SELECT * FROM Tournament;
SELECT * FROM Coach;
SELECT * FROM Tournament_registration;
SELECT * FROM Fan;
SELECT * FROM Fanclub;

-- UPDATE

-- increase the capacity for fanclubs with capacity=nb of fans or the difference between the 2 in (1,5)

UPDATE Fanclub
	SET capacity += 50
WHERE capacity = number_of_fans OR capacity-number_of_fans IN (1, 2, 3, 4, 5);


-- award the fans without award and nb of matches attended between 9 and 50

UPDATE Fan
	SET award = 'yes'
WHERE (nb_of_matches_attended BETWEEN 9 AND 50) AND award IS NULL;


-- set site_link to NULL for fanclubs having sites with name formed from 1 character

UPDATE Fanclub
	SET site_link = NULL
WHERE site_link LIKE 'www._.ro';

-- DELETE 

-- delete the coaches without players

DELETE FROM Coach
WHERE player_id IS NULL;

-- delete the doubles playing category for tournaments having id between 1 and 3

DELETE FROM Tournament_playing_category
WHERE tournament_id BETWEEN 1 AND 3 AND playing_category_id = 2;


-- a) 2 queries with the union operation; use UNION [ALL] and OR;

-- all players and coaches born in september 

SELECT name+' H', date_of_birth FROM Player
WHERE date_of_birth LIKE '%-09-%'
UNION 
SELECT name, date_of_birth FROM Coach
WHERE date_of_birth LIKE '%-09-%';

-- all players from Romania and USA

SELECT name, country FROM Player 
WHERE country = 'Romania' OR country = 'USA';

-- b) 2 queries with the intersection operation; use INTERSECT and IN;

-- all players with coaches younger than them 

SELECT DISTINCT P.name, P.rank+1 FROM Player P
WHERE P.id IN
	(SELECT C.player_id FROM Coach C)
INTERSECT 
SELECT P.name, P.rank FROM Player P
WHERE P.id IN
	(SELECT C.player_id FROM Coach C
	 WHERE C.age < P.age)
	ORDER BY P.rank+1 ASC;

-- all players that attended 'Transilvania Open' or 'Roland Garros'

SELECT P.name FROM Player P
WHERE P.id IN
	(SELECT R.player_id FROM Tournament_registration R
	 WHERE R.tournament_id = 5 OR R.tournament_id = 2)
	 ORDER BY P.name DESC;

-- c) 2 queries with the difference operation; use EXCEPT and NOT IN;

-- countries with tournaments but not players

SELECT country FROM Tournament
EXCEPT
SELECT country FROM Player;


-- tournaments without registrations

SELECT T.name FROM Tournament T
WHERE T.id NOT IN
	(SELECT R.tournament_id FROM Tournament_registration R);

-- d) 4 queries with INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN (one query per operator); 
-- one query will join at least 3 tables, while another one will join at least two many-to-many 
-- relationships;

-- INNER JOIN 

-- get top 5 tournament registrations with player name, name of the player's coach, tournament name and fan names of 
-- players having fans from the same country as the tournament
-- joins 2 many to many tables

SELECT DISTINCT TOP 5 P.name AS player, R.player_id, C.name AS coach, T.name AS tournament, R.tournament_id, F.name AS fan FROM Tournament_registration R
INNER JOIN Player P ON P.id = R.player_id
INNER JOIN Coach C ON C.id = P.id
INNER JOIN Tournament T ON T.id = R.tournament_id
INNER JOIN Fan_of_player FP ON FP.player_id = P.id
INNER JOIN Fan F ON F.id = FP.fan_id
WHERE T.country = F.country;

-- top 5 players sorted by rank registered at tournaments with coaches and tournament playing category
--SELECT TOP 50 P.name AS player, R.player_id, C.name AS coach, T.name AS tournament, R.tournament_id, PC.category AS category FROM Tournament_registration R
--INNER JOIN Player P ON P.id = R.player_id
--INNER JOIN Coach C ON C.id = P.id
--INNER JOIN Tournament T ON T.id = R.tournament_id
--INNER JOIN Tournament_playing_category TPC ON TPC.tournament_id = R.tournament_id
--INNER JOIN Playing_category PC ON PC.id = TPC.playing_category_id
--ORDER BY P.rank ASC;

-- LEFT JOIN
-- get tournaments with their type and points where players can win >= 900 points

SELECT T.name AS tournament, TT.type_name AS type, TT.points AS points FROM Tournament T
LEFT JOIN Tournament_type TT ON T.tournament_type_id = TT.id
WHERE TT.points >= 900;

-- RIGHT JOIN
-- get tournaments having doubles playing category

SELECT T.name AS tournament, PC.category AS category FROM Tournament_playing_category TPC
RIGHT JOIN Tournament T ON T.id = TPC.tournament_id
RIGHT JOIN Playing_category PC ON PC.id = TPC.playing_category_id
WHERE TPC.playing_category_id = 2;

-- FULL JOIN
-- get top 20 fans along with their favourite players and fanclubs sorted ascending by fan name
-- joins 4 tables

SELECT TOP 20 F.name AS fan, P.name AS player, FC.name AS fanclub FROM Fan_of_player FP
FULL JOIN Player P ON P.id = FP.player_id
FULL JOIN Fan F ON F.id = FP.fan_id
FULL JOIN Fanclub FC ON FC.id = FP.fanclub_id
ORDER BY F.name ASC;


-- e) 2 queries with the IN operator and a subquery in the WHERE clause; in at least one case, 
-- the subquery must include a subquery in its own WHERE clause;

-- coaches that train players that have at least 3 tournament registrations

SELECT C.name FROM Coach C
WHERE C.player_id IN
	(SELECT P.id FROM Player P
	 INNER JOIN Tournament_registration R ON P.id = R.player_id
	 GROUP BY P.id 
	 HAVING COUNT(*) >= 3);

-- players at registered at tournaments having doubles playing category

SELECT P.name FROM Player P
WHERE P.id IN
	(SELECT R.player_id FROM Tournament_registration R
	 WHERE R.tournament_id IN 
		(SELECT TPC.tournament_id FROM Tournament_playing_category TPC
		 WHERE TPC.playing_category_id = 2));

-- f) 2 queries with the EXISTS operator and a subquery in the WHERE clause;

-- players having fans

SELECT P.name FROM Player P
WHERE EXISTS
	(SELECT * FROM Fan_of_player FP
	 WHERE FP.player_id = P.id);

-- fanclubs having known fans

SELECT FC.name FROM Fanclub FC
WHERE EXISTS	
	(SELECT * FROM Fan_of_player FP
	 WHERE FP.fanclub_id = FC.id);

-- g) 2 queries with a subquery in the FROM clause;

-- players with less than 1500 points registered at tournaments where they can win 

SELECT DISTINCT A.name FROM
	(SELECT P.name FROM Tournament_registration R
	 INNER JOIN Player P ON P.id = R.player_id
	 WHERE P.points < 1500) A;

-- tournaments of 2000 points having doubles category

SELECT A.name FROM
	(SELECT T.name FROM Tournament_playing_category TPC
	 INNER JOIN Tournament T ON TPC.tournament_id = T.id
	 INNER JOIN Playing_category PC ON TPC.playing_category_id = PC.id
	 INNER JOIN Tournament_type TT ON TT.id = T.tournament_type_id
	 WHERE TPC.playing_category_id = 2 AND TT.points = 2000) A;

-- h) 4 queries with the GROUP BY clause, 3 of which also contain the HAVING clause; 2 of the latter will also have a 
-- subquery in the HAVING clause; use the aggregation operators: COUNT, SUM, AVG, MIN, MAX;

-- countries with at least two players

SELECT P.country, COUNT(*) AS nb_of_players FROM Player P
GROUP BY P.country
HAVING COUNT(*) > 1;

-- players with the most fans

SELECT P.name, COUNT(*) AS fans FROM Player P
INNER JOIN Fan_of_player FP ON FP.player_id = P.id
GROUP BY P.name
HAVING COUNT(*) = (
	SELECT MAX(A.C) FROM 
		(SELECT COUNT(*) C FROM Player P
		 INNER JOIN Fan_of_player FP ON FP.player_id = P.id
		 GROUP BY P.id) A
	);

-- youngest coach

SELECT C.age, C.name FROM Coach C
GROUP BY C.age, C.name
HAVING C.age = 
	(SELECT MIN(A.age) FROM
		(SELECT C.age FROM Coach C) A
	);

-- month with most players born

SELECT P.date_of_birth, P.name FROM Player P
GROUP BY P.date_of_birth, P.name
HAVING MONTH(P.date_of_birth) = 
	(SELECT MAX(MONTH(A.date_of_birth)) FROM
		(SELECT COUNT(*) AS C, P.date_of_birth FROM Player P
		 GROUP BY P.date_of_birth) A
	);

-- i) 4 queries using ANY and ALL to introduce a subquery in the WHERE clause (2 queries per operator); 
-- rewrite 2 of them with aggregation operators, and the other 2 with IN / [NOT] IN.

-- players better than all players from Romania

SELECT P.name, P.rank, P.points FROM Player P
WHERE P.points > ALL	
	(SELECT P1.points FROM Player P1
	 WHERE P1.country = 'Romania')
	ORDER BY P.rank ASC;

-- players better than all players from Romania with aggregation operator >

SELECT P.name, P.rank, P.points FROM Player P
WHERE P.points >	
	(SELECT MAX(P1.points) FROM Player P1
	 WHERE P1.country = 'Romania')
	ORDER BY P.rank ASC;

-- players with fans younger with at least 5 years 

SELECT P.name, P.age FROM Player P
WHERE P.age - 5 >= ANY
	(SELECT F.age FROM Fan_of_player
	 INNER JOIN Fan F ON F.id = Fan_of_player.fan_id
	 INNER JOIN Player P1 ON P1.id = Fan_of_player.player_id
	 WHERE P.id = P1.id);

-- players with fans younger with at least 5 years with aggregation operator

SELECT P.name, P.age FROM Player P
WHERE P.age - 5 >=
	(SELECT MIN(F.age) FROM Fan_of_player FP
	 INNER JOIN Fan F ON F.id = FP.fan_id
	 INNER JOIN Player P1 ON P1.id = FP.player_id
	 WHERE P1.id = P.id);

-- players from a country without coaches and with at least 1 fan

SELECT P.name, P.country FROM Player P
WHERE P.country <> ALL	
	(SELECT C.country FROM Coach C)
AND P.id IN
	(SELECT FP.player_id FROM Fan_of_player FP);

-- players from a country without coaches and with at least 1 fan with NOT IN

SELECT P.name, P.country FROM Player P
WHERE P.country NOT IN
	(SELECT C.country FROM Coach C)
AND P.id IN
	(SELECT FP.player_id FROM Fan_of_player FP);

-- fanclubs of Simona Halep or Karolina Pliskova with = capacity than any other, with at least 30 fans and a site link

SELECT FC.name FROM Fanclub FC
WHERE FC.capacity = ANY
	(SELECT FC1.capacity FROM Fanclub FC1)
AND FC.number_of_fans >= 30 AND FC.site_link IS NOT NULL AND (FC.name LIKE 'Halep%' OR FC.name LIKE 'Pliskova%');

-- fanclubs of Simona Halep or Karolina Pliskova with = capacity than any other, with at least 30 fans and a site link WITH IN

SELECT FC.name FROM Fanclub FC
WHERE FC.capacity IN
	(SELECT FC1.capacity FROM Fanclub FC1)
AND FC.number_of_fans >= 30 AND FC.site_link IS NOT NULL AND (FC.name LIKE 'Halep%' OR FC.name LIKE 'Pliskova%');

 