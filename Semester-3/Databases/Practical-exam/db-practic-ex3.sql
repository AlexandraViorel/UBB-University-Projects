use [db-practic-ex3];

DROP TABLE IF EXISTS Visit;
DROP TABLE IF EXISTS Visitor;
DROP TABLE IF EXISTS FoodQuota;
DROP TABLE IF EXISTS Food;
DROP TABLE IF EXISTS Animal;
DROP TABLE IF EXISTS Zoo;

CREATE TABLE Zoo(
	zooId INT PRIMARY KEY IDENTITY(1, 1),
	administrator VARCHAR(50),
	name VARCHAR(50)
);

CREATE TABLE Animal (
	animalId INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50),
	dateOfBirth DATE,
	zooId INT REFERENCES Zoo(zooId)
);

CREATE TABLE Food (
	foodId INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50)
);

CREATE TABLE FoodQuota (
	animalId INT REFERENCES Animal(animalId),
	foodId INT REFERENCES Food(foodId),
	PRIMARY KEY(animalId, foodId),
	quantity INT
);

CREATE TABLE Visitor (
	visitorId INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50),
	age INT
);

CREATE TABLE Visit (
	visitId INT PRIMARY KEY IDENTITY(1, 1),
	dayy INT,
	price INT,
	visitorId INT REFERENCES Visitor(visitorId),
	zooId INT REFERENCES Zoo(zooId)
);


INSERT INTO Zoo	
	(administrator, name)
VALUES
	('admin1', 'zoo1'),
	('admin2', 'zoo2'),
	('admin3', 'zoo3'),
	('admin4', 'zoo4');

INSERT INTO Animal
	(name, dateOfBirth, zooId)
VALUES
	('animal1', GETDATE(), 1),
	('animal2', GETDATE(), 4),
	('animal3', GETDATE(), 2),
	('animal4', GETDATE(), 3),
	('animal5', GETDATE(), 1),
	('animal6', GETDATE(), 1);

INSERT INTO Food
	(name)
VALUES
	('f1'),
	('f2'),
	('f3'),
	('f4'),
	('f5');


INSERT INTO FoodQuota
	(animalId, foodId, quantity)
VALUES
	(1, 1, 5),
	(1, 2, 4),
	(2, 5, 1),
	(3, 4, 5);

INSERT INTO Visitor
	(name, age)
VALUES
	('visitor1', 20),
	('visitor2', 20),
	('visitor3', 20),
	('visitor4', 20),
	('visitor5', 20);

INSERT INTO Visit
	(dayy, price, visitorId, zooId)
VALUES
	(2, 20, 1, 1),
	(3, 15, 2, 2),
	(5, 32, 3, 1);

-- 2. 

DROP PROCEDURE IF EXISTS uspDeleteFoodQuotas
GO

CREATE PROCEDURE uspDeleteFoodQuotas(@animalId INT, @foodId INT)
AS
BEGIN
	IF EXISTS (SELECT * FROM FoodQuota WHERE animalId = @animalId AND foodId = @foodId)
		DELETE FROM FoodQuota
		WHERE animalId = @animalId AND foodId = @foodId
	ELSE
		raiserror('Food quota does not exist!', 12, 1)
END
GO

-- 3.

DROP VIEW IF EXISTS showZoos
GO

CREATE VIEW showZoos
AS
	SELECT Z.zooId FROM Zoo Z
	LEFT JOIN Visit V ON Z.zooId = V.zooId
	GROUP BY Z.zooId
	HAVING COUNT(Z.zooId) = (SELECT TOP 1 COUNT(Z.zooId) AS nbVisits FROM Zoo Z
					   LEFT JOIN Visit V ON Z.zooId = V.visitId
					   GROUP BY Z.zooId
					   ORDER BY nbVisits)
GO
SELECT * FROM Visit
SELECT * FROM showZoos 

-- 4.

DROP FUNCTION IF EXISTS showVisitors 
GO

CREATE FUNCTION showVisitors (@N INT)
	RETURNS TABLE
AS 
	RETURN 
		SELECT V.visitorId from Visit V
		WHERE V.zooId IN
			(SELECT Z.zooId FROM Zoo Z
			 INNER JOIN Animal A ON A.zooId = Z.zooId
			 GROUP BY Z.zooId
			 HAVING COUNT(*) >= @N)
GO

SELECT * FROM showVisitors(1)