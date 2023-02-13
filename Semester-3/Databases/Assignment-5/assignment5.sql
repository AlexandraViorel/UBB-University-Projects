use [tennis-tournament]


DROP TABLE IF EXISTS JuniorTournamentRegistration;
DROP TABLE IF EXISTS JuniorPlayer;
DROP TABLE IF EXISTS JuniorTournament;


-- Ta(aid, a2, …) => aid = jpID, a2 = rank
CREATE TABLE JuniorPlayer(
	jpID INT NOT NULL PRIMARY KEY,
	rank INT UNIQUE NOT NULL,
	name VARCHAR(50) NOT NULL
);



--Tb(bid, b2, …) => bid = jtID, b2 = points
CREATE TABLE JuniorTournament(
	jtID INT NOT NULL PRIMARY KEY,
	points INT NOT NULL,
	name VARCHAR(50) NOT NULL
);


-- Tc(cid, aid, bid, …) => cid = jtrID, aid = jpID, bid = jtID
CREATE TABLE JuniorTournamentRegistration(
	jtrID INT NOT NULL PRIMARY KEY,
	jpID INT NOT NULL REFERENCES JuniorPlayer(jpID) ON DELETE CASCADE ON UPDATE CASCADE,
	jtID INT NOT NULL REFERENCES JuniorTournament(jtID) ON DELETE CASCADE ON UPDATE CASCADE
);


-- insert random data in Ta

DROP PROCEDURE IF EXISTS insertIntoJuniorPlayer;
GO

CREATE PROCEDURE insertIntoJuniorPlayer (@rows INT) AS
BEGIN
	DECLARE @junior INT = 1;
	DECLARE @rank INT = 1;
	DECLARE @name VARCHAR(50) = 'Default Name';

	WHILE @rows > 0
	BEGIN
		INSERT INTO JuniorPlayer (jpID, rank, name)
		VALUES (@junior, @rank, @name);

		SET @junior = @junior + 1;
		SET @rank = @rank + 1;
		SET @rows = @rows - 1;
	END
	
END
GO


-- insert random data in Tb

DROP PROCEDURE IF EXISTS insertIntoJuniorTournament;
GO

CREATE PROCEDURE insertIntoJuniorTournament (@rows INT) AS
BEGIN
	DECLARE @tournament INT = 1;
	DECLARE @points INT = 1000;
	DECLARE @name VARCHAR(50) = 'Default Tournament';

	WHILE @rows > 0
	BEGIN
		INSERT INTO JuniorTournament (jtID, points, name)
		VALUES (@tournament, @points, @name);

		SET @tournament = @tournament + 1;
		SET @points = @points + 100;
		IF @points > 1500
			SET @points = 1000;
		SET @rows = @rows - 1;
	END

END
GO


-- insert random data in Tc

DROP PROCEDURE IF EXISTS insertIntoJuniorTournamentRegistration;
GO

CREATE PROCEDURE insertIntoJuniorTournamentRegistration (@rows INT) AS
BEGIN
	DECLARE @registration INT = 1;
	DECLARE @player INT = 1;
	DECLARE @tournament INT = 1;

	WHILE @rows > 0
	BEGIN
		INSERT INTO JuniorTournamentRegistration (jtrID, jpID, jtID)
		VALUES (@registration, @player, @tournament);

		SET @registration = @registration + 1;
		SET @player = @player + 1;
		SET @tournament = @tournament + 1;
		SET @rows = @rows - 1;
	END

END
GO


-- populate the tables

DELETE FROM JuniorTournamentRegistration;
DELETE FROM JuniorPlayer;
DELETE FROM JuniorTournament;

EXEC insertIntoJuniorPlayer 10000;
EXEC insertIntoJuniorTournament 10000;
EXEC insertIntoJuniorTournamentRegistration 10000;


-----------------------------------------------------------------------------------------------
/*
a. Write queries on Ta such that their execution plans contain the following operators:

	- clustered index scan;
	- clustered index seek;
	- nonclustered index scan;
	- nonclustered index seek;
	- key lookup.
*/

EXEC sp_helpindex JuniorPlayer;

-- PK: jpID => automatically created clustered index
-- unique: rank => automatically created unclustered index

-- clustered index scan => touch every row in the table

SELECT * FROM JuniorPlayer;

-- clustered index seek => returns a specific subset from the clustered index

SELECT * FROM JuniorPlayer
WHERE jpID < 1000;

-- nonclustered index scan => scan the entire nonclustered index

SELECT rank FROM JuniorPlayer;

-- nonclustered index seek => returns a specific subset from the nonclustered index

SELECT rank FROM JuniorPlayer
WHERE rank < 100;

-- key lookup => nonclustered index seek + additional data needed

SELECT name, rank FROM JuniorPlayer
WHERE rank = 1234;


-----------------------------------------------------------------------------------------------
/*
b. Write a query on table Tb with a WHERE clause of the form WHERE b2 = value and analyze its execution plan. 
Create a nonclustered index that can speed up the query. Examine the execution plan again.
*/

-- first it's a clustered index scan 
SELECT points FROM JuniorTournament
WHERE points = 1400;

DROP INDEX IF EXISTS JuniorTournamentNonclustered ON JuniorTournament

CREATE NONCLUSTERED INDEX JuniorTournamentNonclustered ON JuniorTournament(points)

-- now we have a nonclustered index seek, which is more efficient
SELECT points FROM JuniorTournament
WHERE points = 1400;


-----------------------------------------------------------------------------------------------
/*
c. Create a view that joins at least 2 tables. Check whether existing indexes are helpful; 
if not, reassess existing indexes / examine the cardinality of the tables.
*/

DROP VIEW IF EXISTS view1;
GO

CREATE VIEW view1 AS
	SELECT C.jtrID, C.jtID, B.points, B.name FROM JuniorTournamentRegistration C
	INNER JOIN JuniorTournament B ON C.jtID = B.jtID
	WHERE B.points > 1100;
GO

DECLARE @start1 DATETIME = GETDATE();
SELECT * FROM view1
DECLARE @end1 DATETIME = GETDATE();

PRINT 'WITHOUT INDEXES: start: ' + CONVERT(NVARCHAR(MAX), @start1) + ', end: ' + CONVERT(NVARCHAR(MAX), @end1) 
		+ ', total time: ' + CONVERT(NVARCHAR(MAX), DATEDIFF(millisecond, @start1, @end1)) + ' milliseconds';


DROP INDEX IF EXISTS Nonclustered1 ON JuniorTournament

CREATE NONCLUSTERED INDEX Nonclustered1 ON JuniorTournament(points)

DROP INDEX IF EXISTS Nonclustered2 ON JuniorTournament

CREATE NONCLUSTERED INDEX Nonclustered2 ON JuniorTournament(name)


DROP VIEW IF EXISTS view2;
GO

CREATE VIEW view2 AS
	SELECT C.jtrID, C.jtID, B.points, B.name FROM JuniorTournamentRegistration C
	INNER JOIN JuniorTournament B ON C.jtID = B.jtID
	WHERE B.points > 1100;
GO

DECLARE @start2 DATETIME = GETDATE();
SELECT * FROM view2
DECLARE @end2 DATETIME = GETDATE();

PRINT 'WITH INDEXES: start: ' + CONVERT(NVARCHAR(MAX), @start2) + ', end: ' + CONVERT(NVARCHAR(MAX), @end2) 
		+ ', total time: ' + CONVERT(NVARCHAR(MAX), DATEDIFF(millisecond, @start2, @end2)) + ' milliseconds';