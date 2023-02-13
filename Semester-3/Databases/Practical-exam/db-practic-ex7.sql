use [db-practic-cipri];

DROP TABLE IF EXISTS Reservation;
DROP TABLE IF EXISTS Payment;
DROP TABLE IF EXISTS Passenger;
DROP TABLE IF EXISTS Flight;
DROP TABLE IF EXISTS Airplane;

CREATE TABLE Airplane(
	aid INT PRIMARY KEY IDENTITY(1, 1),
	modelnb INT,
	registrationnb INT UNIQUE,
	capacity INT
);

CREATE TABLE Flight(
	flightnb INT PRIMARY KEY IDENTITY(1, 1),
	departureairport VARCHAR(50),
	arrivalairport VARCHAR(50),
	departuredatetime DATETIME,
	arrivaldatetime DATETIME,
	airplaneid INT REFERENCES Airplane(aid)
);

CREATE TABLE Passenger(
	pid INT PRIMARY KEY IDENTITY(1, 1),
	firstname VARCHAR(50),
	lastname VARCHAR(50),
	emailaddress VARCHAR(50) UNIQUE
);

CREATE TABLE Payment(
	pid INT PRIMARY KEY IDENTITY(1, 1),
	amount INT,
	dateandtime DATETIME,
	method VARCHAR(50)
);

CREATE TABLE Reservation(
	rid INT PRIMARY KEY IDENTITY(1, 1),
	passenger INT REFERENCES Passenger(pid),
	flight INT REFERENCES Flight(flightnb),
	payment INT REFERENCES Payment(pid)
);

INSERT INTO Airplane
	(modelnb, registrationnb, capacity)
VALUES
	(1, 1, 100),
	(2, 2, 200),
	(3, 3, 300),
	(4, 4, 400);

INSERT INTO Flight
	(departureairport, arrivalairport, airplaneid)
VALUES
	('Madrid', 'Cluj', 1),
	('Cluj', 'Viena', 2),
	('Madrid', 'Viena', 3),
	('Madrid', 'Bucuresti', 4);

INSERT INTO Passenger
	(firstname, lastname, emailaddress)
VALUES
	('f1', 'l1', 'm1'),
	('f2', 'l2', 'm2'),
	('f3', 'l3', 'm3'),
	('f4', 'l4', 'm4');

INSERT INTO Payment
	(amount, method)
VALUES
	(100, 'card'),
	(200, 'cash'),
	(1000, 'card');

INSERT INTO Reservation
	(flight, passenger, payment)
VALUES
	(1, 1, NULL),
	(1, 2, 1),
	(2, 3, 3);

-- 2. 

DROP PROCEDURE IF EXISTS updateRes 
GO

CREATE PROCEDURE updateRes(@paymentId INT, @reservationId INT)
AS
BEGIN
	IF EXISTS (SELECT * FROM Payment WHERE pid = @paymentId) AND EXISTS (SELECT * FROM Reservation WHERE rid = @reservationId)
		IF (SELECT payment FROM Reservation WHERE payment = @paymentId) IS NOT NULL
			raiserror('Payment already exists for given reservation!', 12, 1)
		ELSE
			UPDATE Reservation
			SET payment = @paymentId
			WHERE rid = @reservationId
	ELSE
		raiserror('Payment or reservation does not exist!', 12, 1)
END
GO

exec updateRes @paymentId = 2, @reservationId = 1

-- 3.

DROP VIEW IF EXISTS resMadrid
GO

CREATE VIEW resMadrid
AS
	SELECT P.firstname, P.lastname FROM Passenger P
	WHERE P.pid IN
		(SELECT R.passenger FROM Reservation R
		 INNER JOIN Flight F ON R.flight = F.flightnb
		 WHERE F.departureairport = 'Madrid'
		 )
GO

SELECT * FROM resMadrid

-- 4.

DROP FUNCTION IF EXISTS listFlights 
GO

CREATE FUNCTION listFlights(@X INT, @startTime DATETIME, @endTime DATETIME)
	RETURNS TABLE
AS
	RETURN 
		SELECT * FROM Flight F
		WHERE F.departuredatetime >= @startTime AND F.departuredatetime <= @endTime AND F.flightnb IN
			(SELECT R.flight FROM Reservation R
			 WHERE R.payment IS NOT NULL
			 GROUP BY R.flight
			 HAVING COUNT(*) > @X)
GO

SELECT * FROM listFlights(2, '2022-10-10 12:00am', '2023-01-01 12:00am')