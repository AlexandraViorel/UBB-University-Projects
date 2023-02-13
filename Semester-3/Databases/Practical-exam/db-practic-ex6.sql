use [db-practic-bledea];

DROP TABLE IF EXISTS Delivery;
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS PizzaShop;
DROP TABLE IF EXISTS Drone;
DROP TABLE IF EXISTS DroneModel;
DROP TABLE IF EXISTS DroneManufacturer;

CREATE TABLE DroneManufacturer(
	dmid INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50)
);

CREATE TABLE DroneModel(
	dmodid INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50),
	batterylife INT,
	maxspeed INT,
	dmanuf INT REFERENCES DroneManufacturer(dmid)
);

CREATE TABLE Drone(
	did INT PRIMARY KEY IDENTITY(1, 1),
	dmid INT REFERENCES DroneModel(dmodid),
	serialnb INT
);

CREATE TABLE PizzaShop(
	psid INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50) UNIQUE,
	address VARCHAR(50)
);

CREATE TABLE Customer(
	cid INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50) UNIQUE,
	loyaltyscore INT
);

CREATE TABLE Delivery(
	delid INT PRIMARY KEY IDENTITY(1, 1),
	psid INT REFERENCES PizzaShop(psid),
	cid INT REFERENCES Customer(cid),
	did INT REFERENCES Drone(did),
	dateandtime DATETIME
);


INSERT INTO DroneManufacturer
	(name)
VALUES
	('dmanuf1'),
	('dmanuf2'),
	('dmanuf3'),
	('dmanuf4');

INSERT INTO DroneModel
	(name, dmanuf, maxspeed, batterylife)
VALUES
	('dm1', 1, 25, 1500),
	('dm2', 2, 25, 1500),
	('dm3', 3, 25, 1500),
	('dm4', 4, 25, 1500),
	('dm5', 1, 25, 1500),
	('dm6', 2, 25, 1500);

INSERT INTO Drone
	(dmid, serialnb)
VALUES
	(1, 150),
	(2, 151),
	(3, 152),
	(4, 153),
	(5, 154),
	(6, 155),
	(1, 156);

INSERT INTO PizzaShop
	(name, address)
VALUES
	('ps1', 'a1'),
	('ps2', 'a2'),
	('ps3', 'a3'),
	('ps4', 'a4');

INSERT INTO Customer
	(name, loyaltyscore)
VALUES
	('c1', 150),
	('c2', 151),
	('c3', 152),
	('c4', 153);

INSERT INTO Delivery
	(psid, cid, did)
VALUES
	(1, 1, 1),
	(1, 2, 5),
	(4, 3, 2),
	(3, 4, 6),
	(2, 1, 3);


-- 2.

DROP PROCEDURE IF EXISTS addDelivery 
GO

CREATE PROCEDURE addDelivery(@pizzashopid INT, @customerid INT, @droneid INT, @dateandt DATETIME)
AS
BEGIN
	IF EXISTS (SELECT * FROM PizzaShop WHERE psid = @pizzashopid) 
	AND EXISTS (SELECT * FROM Customer WHERE cid = @customerid)
	AND EXISTS (SELECT * FROM Drone WHERE did = @droneid)
		INSERT INTO Delivery
			(psid, cid, did, dateandtime)
		VALUES
			(@pizzashopid, @customerid, @droneid, @dateandt)
	ELSE
		raiserror('Pizza shop, customer or drone does not exist!', 12, 1)
END
GO

exec addDelivery @pizzashopid = 3, @customerid = 4, @droneid = 3, @dateandt = '2023-01-01 12:00pm'

SELECT * FROM Delivery


-- 3.

DROP VIEW IF EXISTS droneMauf
GO

CREATE VIEW droneManuf
AS
	SELECT DMA.name FROM DroneManufacturer DMA
	WHERE DMA.dmid IN
		(SELECT DM.dmanuf FROM DroneModel DM
		 INNER JOIN DRONE D ON D.dmid = DM.dmodid
		 INNER JOIN Delivery DE ON DE.did = D.did
		 GROUP BY DM.dmanuf
		 HAVING COUNT(*) >= ALL (SELECT COUNT(*) FROM DroneManufacturer DMA2
								 INNER JOIN DroneModel DM2 ON DM2.dmanuf = DMA2.dmid
								 INNER JOIN Drone D2 ON D2.dmid = DM2.dmodid
								 INNER JOIN Delivery DE2 ON DE2.did = D2.did
								 GROUP BY DMA2.dmid))
GO

SELECT * FROM droneManuf

SELECT * FROM DroneManufacturer
SELECT * FROM DroneModel
SELECT * FROM Drone
SELECT * FROM Delivery


-- 4. 

DROP FUNCTION IF EXISTS customersDel 
GO

CREATE FUNCTION customersDel(@D INT)
	RETURNS TABLE
AS
	RETURN 
		SELECT C.name FROM Customer C
		WHERE C.cid IN 
			(SELECT D.cid FROM Delivery D
			 GROUP BY D.cid
			 HAVING COUNT(*) >= @D)
GO

SELECT * FROM customersDel(2)