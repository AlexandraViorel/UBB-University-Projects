use [db-practic-ex1];

-- 1.

DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS ATM;
DROP TABLE IF EXISTS Card;
DROP TABLE IF EXISTS BankAccount;
DROP TABLE IF EXISTS Customer;

CREATE TABLE Customer (
	idC INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50),
	dateOfBirth DATE
);

CREATE TABLE BankAccount (
	idBA INT PRIMARY KEY IDENTITY(1, 1),
	IBAN VARCHAR(25),
	ballance INT,
	customerId INT REFERENCES Customer(idC)
);

CREATE TABLE Card (
	cardId INT PRIMARY KEY IDENTITY(1, 1),
	number VARCHAR(12),
	CVV INT,
	bankAccountId INT REFERENCES BankAccount(idBA)
);

CREATE TABLE ATM (
	atmId INT PRIMARY KEY IDENTITY(1, 1),
	address VARCHAR(50)
);

CREATE TABLE Transactions (
	transactionId INT PRIMARY KEY IDENTITY(1, 1),
	cardId INT REFERENCES Card(cardId),
	atmId INT REFERENCES ATM(atmId),
	moneySum INT,
	dateAndTime DATETIME
);


INSERT INTO Customer
	(name, dateOfBirth)
VALUES
	('customer1', '2000-02-19'),
	('customer2', '2002-11-22'),
	('customer3', '1999-05-05');

INSERT INTO BankAccount
	(IBAN, ballance, customerId)
VALUES
	('RO123', 1000, 1),
	('RO456', 5000, 2),
	('RO198', 800, 3),
	('RO999', 2500, 2);

INSERT INTO Card
	(number, CVV, bankAccountId)
VALUES
	('414049703694', 694, 1),
	('414049705482', 482, 1),
	('414049705830', 830, 2),
	('414049705704', 704, 3),
	('414049705684', 684, 4);

INSERT INTO ATM
	(address)
VALUES
	('str.A,nr.1'),
	('str.B,nr.2'),
	('str.C,nr.3'),
	('str.D,nr.4');

INSERT INTO Transactions
	(cardId, atmId, moneySum, dateAndTime)
VALUES
	(1, 2, 350, '2023-01-01 10:30am'),
	(2, 1, 2050, '2023-01-02 10:30pm'),
	(3, 1, 500, '2023-01-01 11:00pm'),
	(1, 4, 100, '2023-01-04 9:00pm'),
	(1, 1, 100, '2023-01-05 9:00pm'),
	(1, 3, 100, '2023-01-03 9:00pm'),
	(2, 1, 50, '2023-01-02 10:30pm'),
	(2, 1, 60, '2023-01-02 10:31pm'),
	(2, 1, 70, '2023-01-02 10:32pm');


SELECT * FROM Customer;
SELECT * FROM BankAccount;
SELECT * FROM Card;
SELECT * FROM ATM;
SELECT * FROM Transactions;

-- 2. Implement a stored procedure that receives a card and deletes all the transactions related to that card.

DROP PROCEDURE IF EXISTS uspDeleteTransactions
GO

CREATE PROCEDURE uspDeleteTransactions (@cardNumber VARCHAR(12))
AS
BEGIN
	DECLARE @cardId INT = (SELECT cardId FROM Card WHERE number = @cardNumber);
	IF @cardId IS NOT NULL
		DELETE FROM Transactions WHERE cardId = @cardId
	ELSE
		raiserror('Card does not exist!', 12, 1)
END
GO


--exec uspDeleteTransactions @cardNumber = '414049703694'
--GO

-- 3. Create a view that shows the card numbers which were used in transactions at all ATMs.

DROP VIEW IF EXISTS allATMCards
GO

CREATE VIEW allATMCards
AS
	SELECT C.number FROM Card C
	WHERE C.cardId IN
		(SELECT sq.cardId FROM
			(SELECT DISTINCT T.cardID, T.atmId FROM Transactions T) AS sq
			GROUP BY sq.cardId
			HAVING COUNT(*) = (SELECT COUNT(*) FROM ATM))
		  
GO

SELECT * FROM allATMCards

-- 4. Implement a function that lists the cards(number and CVV code) that have the total transactions sum 
-- greater than 2000 lei.

DROP FUNCTION IF EXISTS ufCardsTransactions
GO
CREATE FUNCTION ufCardsTransactions(@total INT)
	RETURNS TABLE 
AS
	RETURN
		SELECT C.number, C.CVV FROM Card C
		WHERE C.cardId IN
			(SELECT T.cardId FROM Transactions T
			 GROUP BY T.cardId
			 HAVING SUM(T.moneySum) > @total)
GO

SELECT * FROM ufCardsTransactions(2000)