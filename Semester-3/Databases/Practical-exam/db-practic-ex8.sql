use [db-practic-flaviu];

DROP TABLE IF EXISTS Eval;
DROP TABLE IF EXISTS Judge;
DROP TABLE IF EXISTS Poem;
DROP TABLE IF EXISTS InternalCompetition;
DROP TABLE IF EXISTS Awards;
DROP TABLE IF EXISTS Users;

CREATE TABLE Users(
	userId INT PRIMARY KEY IDENTITY(1,1),
	name VARCHAR(50),
	penname VARCHAR(50) UNIQUE,
	yearofb INT
);

CREATE TABLE Awards(
	awardId INT PRIMARY KEY IDENTITY(1,1),
	name VARCHAR(50),
	userId INT REFERENCES Users(userId)
);

CREATE TABLE InternalCompetition(
	weekId INT PRIMARY KEY,
	year INT
);

CREATE TABLE Poem(
	poemId INT PRIMARY KEY IDENTITY(1, 1),
	title VARCHAR(50),
	textt VARCHAR(50),
	competitionId INT REFERENCES InternalCompetition(weekId),
	userId INT REFERENCES Users(userId)
);

CREATE TABLE Judge(
	judgeId INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50)
);

CREATE TABLE Eval(
	judgeId INT REFERENCES Judge(judgeId),
	poemId INT REFERENCES Poem(poemId),
	PRIMARY KEY(judgeId, poemId),
	points INT
);

INSERT INTO Users
	(name, penname)
VALUES
	('u1', 'p1'),
	('u2', 'p2'),
	('u3', 'p3'),
	('u4', 'p4'),
	('u4', 'p5');


-- b. Implement a procedure that receives a string value as parameter, representing the name of a judge.
-- It deletes all judges with specified name and their evaluations.

DROP PROCEDURE IF EXISTS deleteJudge 
GO

CREATE PROCEDURE deleteJudge(@judgeName VARCHAR(50))
AS
BEGIN
	DECLARE judgecursor CURSOR FOR
		SELECT judgeId FROM Judge
		WHERE name = @judgeName
	OPEN judgecursor
	DECLARE @jId INT
	FETCH judgecursor INTO @jId
	WHILE @@FETCH_STATUS = 0
	BEGIN
		DELETE FROM Eval WHERE judgeId = @jId
		DELETE FROM Judge WHERE judgeId = @jId
		FETCH judgecursor INTO @jId
	END
	CLOSE judgecursor
	DEALLOCATE judgecursor
END
GO

-- c. Create a view that shows the competitions (year and week nb) with at least 10 submitted poems that 
-- satisfies cond C = the poem received less than 5 points on each evaluation 

CREATE VIEW showCompetitions 
AS
	SELECT * FROM InternalCompetition C
	WHERE C.weekId IN
		(SELECT P.competitionId FROM Poem P
		 INNER JOIN Eval E ON P.poemId = E.poemId
		 WHERE )