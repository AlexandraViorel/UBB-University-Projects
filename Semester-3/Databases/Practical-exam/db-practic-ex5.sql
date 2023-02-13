use [db-practic-ex5];

DROP TABLE IF EXISTS CinemaProductionActors;
DROP TABLE IF EXISTS CinemaProduction;
DROP TABLE IF EXISTS Actor;
DROP TABLE IF EXISTS Movie;
DROP TABLE IF EXISTS Company;
DROP TABLE IF EXISTS StageDirector;

CREATE TABLE StageDirector (
	dirId INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50),
	nbOfAwards INT
);

CREATE TABLE Company(
	companyId INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50)
);

CREATE TABLE Movie (
	movieId INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50),
	releaseDate DATE,
	companyId INT REFERENCES Company(companyId),
	directorId INT REFERENCES StageDirector(dirId)
);

CREATE TABLE Actor(
	actorId INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50),
	ranking INT
);

CREATE TABLE CinemaProduction (
	prodId INT PRIMARY KEY IDENTITY(1, 1),
	title VARCHAR(50),
	movieId INT REFERENCES Movie(movieId),
);

CREATE TABLE CinemaProductionActors (
	prodId INT REFERENCES CinemaProduction(prodId),
	actorId INT REFERENCES Actor(actorId),
	PRIMARY KEY(prodId, actorId),
	entryMom DATE
);


INSERT INTO StageDirector
	(name, nbOfAwards)
VALUES 
	('dir1', 10),
	('dir2', 20),
	('dir3', 30),
	('dir4', 40),
	('dir5', 50);

INSERT INTO Company
	(name)
VALUES
	('c1'),
	('c2'),
	('c3'),
	('c4'),
	('c5');

INSERT INTO Movie
	(name, releaseDate, companyId, directorId)
VALUES
	('m1', '2022-05-06', 1, 1),
	('m2', '2015-05-06', 2, 2),
	('m3', '2019-05-06', 3, 3),
	('m4', '2018-05-06', 4, 4),
	('m5', '2010-05-06', 5, 5);

INSERT INTO Actor
	(name, ranking)
VALUES
	('a1', 1),
	('a2', 2),
	('a3', 3),
	('a4', 4);

INSERT INTO CinemaProduction
	(title, movieId)
VALUES
	('prod1', 1),
	('prod2', 2),
	('prod3', 3),
	('prod4', 4);

INSERT INTO CinemaProductionActors	
	(prodId, actorId, entryMom)
VALUES
	(1, 1, GETDATE()),
	(1, 2, GETDATE()),
	(1, 3, GETDATE()),
	(2, 1, GETDATE()),
	(3, 1, GETDATE()),
	(4, 1, GETDATE());

-- 2.
DROP PROCEDURE IF EXISTS addActor 
GO


CREATE PROCEDURE addActor(@actorId INT, @entryMom DATE, @prodId INT)
AS
BEGIN
	IF EXISTS (SELECT * FROM Actor WHERE actorId = @actorId) AND EXISTS (SELECT * FROM CinemaProduction WHERE prodId = @prodId)
		INSERT INTO CinemaProductionActors
		VALUES (@prodId, @actorId, @entryMom)
	ELSE 
		raiserror('Actor or company does not exist!', 12, 1)
END
GO

exec addActor @actorId = 4, @entryMom = '2022-01-01', @prodId = 3

SELECT * FROM CinemaProductionActors

-- 3. 

DROP VIEW IF EXISTS showActors
GO

CREATE VIEW showActors
AS
	SELECT A.name FROM Actor A
	WHERE A.actorId IN
		(SELECT actorId FROM CinemaProductionActors
		 GROUP BY actorId
		 HAVING COUNT(prodId) = (SELECT COUNT(*) FROM CinemaProduction))
GO

SELECT * FROM showActors


-- 4. 

DROP FUNCTION IF EXISTS showMovie 
GO

CREATE FUNCTION showMovies (@P INT)
	RETURNS TABLE 
AS
	RETURN 
		SELECT * FROM Movie
		WHERE movieId IN
			(SELECT A1.movieId FROM
				(SELECT A.movieId, A.nb FROM 
					(SELECT movieId, COUNT(movieId) AS nb FROM CinemaProduction
					 GROUP BY movieId) A
				GROUP BY A.nb, A.movieId
				HAVING A.nb >= 1) A1)
GO

SELECT * FROM showMovies(1)