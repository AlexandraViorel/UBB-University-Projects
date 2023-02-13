use [db-practic-ex4];

DROP TABLE IF EXISTS OrderCake;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS ChefSpecialization;
DROP TABLE IF EXISTS Chef;
DROP TABLE IF EXISTS Cake;
DROP TABLE IF EXISTS CakeType;

CREATE TABLE CakeType (
	typeId INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50),
	descripiton VARCHAR(50)
);

CREATE TABLE Cake (
	cakeId INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50),
	shape VARCHAR(50),
	weight INT,
	price INT,
	typeId INT REFERENCES CakeType(typeId)
);

CREATE TABLE Chef(
	chefId INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50),
	gender VARCHAR(10),
	dateOfBirth DATE
);

CREATE TABLE ChefSpecialization(
	chefId INT REFERENCES Chef(chefId),
	cakeId INT REFERENCES Cake(cakeId),
	PRIMARY KEY(chefId, cakeId)
);

CREATE TABLE Orders(
	orderId INT PRIMARY KEY IDENTITY(1, 1),
	datee DATE
);

CREATE TABLE OrderCake(
	orderId INT REFERENCES Orders(orderId),
	cakeId INT REFERENCES Cake(cakeId),
	PRIMARY KEY(orderId, cakeId),
	quantity INT,
);


INSERT INTO CakeType
	(name, descripiton)
VALUES
	('t1', 'd1'),
	('t2', 'd2'),
	('t3', 'd3'),
	('t4', 'd4'),
	('t5', 'd5');

INSERT INTO Cake
	(name, shape, weight, price, typeId)
VALUES
	('n1', 's1', 1000, 50, 1),
	('n2', 's2', 2000, 60, 2),
	('n3', 's3', 3000, 70, 3),
	('n4', 's4', 4000, 80, 4),
	('n5', 's5', 5000, 90, 5);


INSERT INTO Chef
	(name, gender, dateOfBirth)
VALUES
	('c1', 'g1', GETDATE()),
	('c2', 'g1', GETDATE()),
	('c3', 'g2', GETDATE()),
	('c4', 'g2', GETDATE()),
	('c5', 'g2', GETDATE());

INSERT INTO ChefSpecialization
	(chefId, cakeId)
VALUES
	(1, 1),
	(1, 2),
	(3, 4),
	(5, 5),
	(2, 2),
	(2, 3),
	(4, 3);

INSERT INTO Orders
	(datee)
VALUES
	('2022-11-22'),
	('2022-07-23'),
	('2022-08-15'),
	('2022-09-26'),
	('2022-10-09');

INSERT INTO OrderCake
	(orderId, cakeId, quantity)
VALUES 
	(1, 1, 3),
	(1, 5, 2),
	(2, 4, 10);

-- 2. Implement a stored procedure that receives an orderId, a cake name and P representing the ordered 
-- pieces and adds the cake to the order. If it already exists it updates P.

DROP PROCEDURE IF EXISTS addUpdateOrderCakes
GO

CREATE PROCEDURE addUpdateOrderCakes (@orderId INT, @cakeName VARCHAR(50), @P INT)
AS
BEGIN
	DECLARE @cakeId INT = (SELECT cakeId FROM Cake WHERE name = @cakeName)
	IF EXISTS (SELECT * FROM Orders WHERE orderId = @orderId) AND @cakeId IS NOT NULL
		IF EXISTS (SELECT * FROM OrderCake WHERE orderId = @orderId AND cakeId = @cakeId)
			UPDATE OrderCake
			SET quantity = @P
			WHERE orderId = @orderId AND cakeId = @cakeId
		ELSE
			INSERT INTO OrderCake VALUES (@orderId, @cakeId, @P)
	ELSE 
		raiserror('Cake or order does not exist', 12, 1)

END
GO

exec addUpdateOrderCakes @orderId = 1, @cakeName = 'n5', @P = 20

SELECT * FROM OrderCake

-- 3. Implement a function that lists the names of the chefs that are specialized in preparing all the cakes.

DROP FUNCTION IF EXISTS showChefs
GO

CREATE FUNCTION showChefs()
	RETURNS TABLE
AS
	RETURN
		SELECT C.name FROM Chef C
		WHERE C.chefId IN
			(SELECT S.chefId FROM ChefSpecialization S
			 GROUP BY S.chefId
			 HAVING COUNT(S.cakeId) = (SELECT COUNT(*) FROM Cake))
GO

SELECT * FROM showChefs()