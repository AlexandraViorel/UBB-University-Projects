use [trains-practical-seminar];

DROP TABLE IF EXISTS RoutesStations;
DROP TABLE IF EXISTS Routes;
DROP TABLE IF EXISTS Station;
DROP TABLE IF EXISTS Trains;
DROP TABLE IF EXISTS TrainTypes;

CREATE TABLE TrainTypes (
	TTid INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50),
	description VARCHAR(100)
);

CREATE TABLE Trains (
	Tid INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50),
	TTid INT REFERENCES TrainTypes(TTid)
);

CREATE TABLE Station (
	Sid INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50) UNIQUE
);

CREATE TABLE Routes (
	Rid INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50),
	Tid INT REFERENCES Trains(Tid)
);

CREATE TABLE RoutesStations (
	Rid INT REFERENCES Routes(Rid),
	Sid INT REFERENCES Station(Sid),
	PRIMARY KEY(Rid, Sid),
	arrivalTime TIME,
	departureTime TIME
);



INSERT INTO TrainTypes
	(name, description)
VALUES
	('tt1', 'd1'),
	('tt2', 'd2');

INSERT INTO Trains
	(name, TTid)
VALUES
	('t1', 1),
	('t2', 2),
	('t3', 1);

INSERT INTO Station
	(name)
VALUES
	('s1'),
	('s2'),
	('s3');

INSERT INTO Routes
	(name, Tid)
VALUES
	('r1', 1),
	('r2', 2),
	('r3', 3);

INSERT INTO RoutesStations
	(Rid, Sid, arrivalTime, departureTime)
VALUES
	(1, 1, '9:00am', '9:05am'),
	(1, 2, '9:30am', '9:35am'),
	(1, 3, '10:00am', '10:05am'),
	(2, 1, '5:00pm', '5:10pm'),
	(2, 2, '7:00pm', '7:10pm'),
	(3, 1, '9:00pm', '9:05pm'),
	(3, 3, '11:00pm', '11:15pm');

SELECT * FROM Trains;
SELECT * FROM TrainTypes;
SELECT * FROM Station;
SELECT * FROM Routes;
SELECT * FROM RoutesStations;


DROP PROCEDURE IF EXISTS updateAddRouteStation
GO

CREATE PROCEDURE updateAddRouteStation (@route VARCHAR(50), @station VARCHAR(50), 
		@arrivalTime TIME, @departureTime TIME)
AS
BEGIN
	DECLARE @routeID INT = (SELECT Rid FROM Routes WHERE name = @route);
	DECLARE @stationID INT = (SELECT Sid FROM Station WHERE name = @station);

	IF @routeID IS NOT NULL AND @stationID IS NOT NULL
		IF NOT EXISTS (SELECT * FROM RoutesStations WHERE Rid = @routeID AND Sid = @stationID)
			INSERT INTO RoutesStations VALUES (@routeID, @stationID, @arrivalTime, @departureTime)
		ELSE
			UPDATE RoutesStations
			SET arrivalTime = @arrivalTime, departureTime = @departureTime
			WHERE Rid = @routeID AND Sid = @stationID
	ELSE
		raiserror('Station or Route not found!', 12, 1);
END
GO

exec updateAddRouteStation @route = 'r1', @station = 's1', @arrivalTime = '9:05am', @departureTime = '9:10am'
GO

DROP VIEW IF EXISTS routesNames
GO

CREATE VIEW routesNames
AS
	SELECT R.name FROM Routes R
	WHERE R.Rid IN
		(SELECT Rid FROM RoutesStations
		 GROUP BY Rid
		 HAVING count(*) = (SELECT COUNT(*) FROM Station)
		)
GO

SELECT * FROM routesNames
GO

DROP FUNCTION IF EXISTS ufReturnStationNames
GO

CREATE FUNCTION ufReturnStationNames (@R INT)
	RETURNS TABLE 
AS
	RETURN 
		SELECT S.name FROM Station S
		WHERE S.Sid IN
			(SELECT RS.Sid FROM RoutesStations RS
			 GROUP BY RS.Sid
			 HAVING COUNT(*) > @R)

GO

SELECT * FROM ufReturnStationNames(1);