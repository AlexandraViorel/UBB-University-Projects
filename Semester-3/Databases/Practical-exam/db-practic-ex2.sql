use [db-practic-ex2];

DROP TABLE IF EXISTS WomanShoes;
DROP TABLE IF EXISTS ShoesShop;
DROP TABLE IF EXISTS Shoe;
DROP TABLE IF EXISTS ShoeModel;
DROP TABLE IF EXISTS PresentationShop;
DROP TABLE IF EXISTS Woman;



CREATE TABLE Woman (
	womanId INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50),
	maxAmount INT
);

CREATE TABLE PresentationShop (
	pShopId INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50),
	city VARCHAR(50)
);

CREATE TABLE ShoeModel (
	shoeMId INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50),
	season VARCHAR(50)
);

CREATE TABLE Shoe (
	shoeId INT PRIMARY KEY IDENTITY(1, 1),
	price INT,
	shoeModelId INT REFERENCES ShoeModel(shoeMId)
);

CREATE TABLE ShoesShop (
	shoeId INT REFERENCES Shoe(shoeId),
	pShopId INT REFERENCES PresentationShop(pShopId),
	PRIMARY KEY(shoeId, pShopId),
	nbAvailable INT
);

CREATE TABLE WomanShoes (
	womanId INT REFERENCES Woman(womanId),
	shoeId INT REFERENCES Shoe(shoeId),
	PRIMARY KEY(womanId, shoeId),
	nbShoes INT, 
	moneySpent INT
);


INSERT INTO Woman
	(name, maxAmount)
VALUES 
	('w1', 1000),
	('w2', 3000),
	('w3', 3000),
	('w4', 4000);

INSERT INTO PresentationShop
	(name, city)
VALUES
	('shop1', 'city1'),
	('shop2', 'city2'),
	('shop3', 'city3'),
	('shop4', 'city4');

INSERT INTO ShoeModel	
	(name, season)
VALUES
	('model1', 'season1'),
	('model2', 'season2'),
	('model3', 'season3'),
	('model4', 'season4');

INSERT INTO Shoe
	(price, shoeModelId)
VALUES
	(130, 1),
	(100, 2),
	(150, 3),
	(110, 4),
	(190, 2),
	(230, 1),
	(90, 2);

INSERT INTO ShoesShop
	(shoeId, pShopId, nbAvailable)
VALUES
	(1, 1, 10),
	(2, 4, 10),
	(3, 1, 10),
	(4, 1, 10),
	(1, 3, 10),
	(1, 2, 10);

INSERT INTO WomanShoes
	(womanId, shoeId, nbShoes, moneySpent)
VALUES
	(1, 1, 3, 260),
	(2, 6, 1, 230),
	(1, 3, 5, 150),
	(3, 4, 2, 220);

-- 2. Create a stored procedure that receives a shoe, a presentation shop and the number of shoes and adds the
-- shoe to the presentation shop.

DROP PROCEDURE IF EXISTS uspAddUpdateShoesToPresShop
GO

CREATE PROCEDURE uspAddShoesToPresShop(@shoeId INT, @pShopId INT, @nbOfShoes INT)
AS
BEGIN
	DECLARE @sId INT = (SELECT shoeId FROM Shoe WHERE shoeId = @shoeId)
	DECLARE @psId INT = (SELECT pShopId FROM PresentationShop WHERE pShopId = @pShopId)
	IF @sId IS NOT NULL AND @psId IS NOT NULL
		IF NOT EXISTS (SELECT * FROM ShoesShop WHERE shoeId = @shoeId AND pShopId = @pShopId)
			INSERT INTO ShoesShop
				(shoeId, pShopId, nbAvailable)
			VALUES
				(@shoeId, @pShopId, @nbOfShoes)
		ELSE 
			UPDATE ShoesShop
			SET nbAvailable = @nbOfShoes
	ELSE
		raiserror('No shoe or presentation shop!', 12, 1)
END
GO

exec uspAddShoesToPresShop 1, 4, 10
GO


-- 3.Create a view that shows the women that bought at least 2 shoes from a given shoe model.

DROP VIEW IF EXISTS womenBought2
GO

CREATE VIEW womenBought2 
AS
	SELECT * FROM Woman
	WHERE womanId IN
		(SELECT womanId FROM WomanShoes
		 WHERE nbShoes > 2)
GO

SELECT * FROM womenBought2
GO

-- 4. Create a function that lists the shoes that can be found in at least T presentation shops, where
-- T>=1 is a function parameter.

DROP FUNCTION IF EXISTS shoesInShop
GO

CREATE FUNCTION shoesInShop (@T INT)
	RETURNS TABLE
AS 
	RETURN 
		SELECT * FROM Shoe
		WHERE shoeId IN
			(SELECT shoeId FROM ShoesShop
			 GROUP BY shoeId
			 HAVING COUNT(*) >= @T)
GO

SELECT * FROM shoesInShop(2)