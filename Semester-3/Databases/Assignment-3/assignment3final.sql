--USE [tennis-tournament];


-- a. modify the type of a column;
-- modify player age from int to tiny int
CREATE OR ALTER PROCEDURE setPlayerAgeToTinyInt 
AS
	ALTER TABLE Player 
		ALTER COLUMN age TINYINT
GO

-- reverse operation: modify player age from tiny int to int

CREATE OR ALTER PROCEDURE setPlayerAgeToInt 
AS
	ALTER TABLE Player 
		ALTER COLUMN age INT
GO

-- b. add / remove a column;
-- add best rank to player

CREATE OR ALTER PROCEDURE addBestRankToPlayer 
AS
	ALTER TABLE Player 
		ADD best_rank INT
GO

-- remove best rank from player

CREATE OR ALTER PROCEDURE removeBestRankFromPlayer 
AS
	ALTER TABLE Player
		DROP COLUMN best_rank
GO

-- c. add / remove a DEFAULT constraint;
-- add default rank 1000 to player

CREATE OR ALTER PROCEDURE addDefaultToRankFromPlayer 
AS
	ALTER TABLE Player
		ADD CONSTRAINT default_rank
			DEFAULT 1000 FOR rank
GO

-- remove default rank from player

CREATE OR ALTER PROCEDURE removeDefaultFromRankFromPlayer
AS
	ALTER TABLE Player
		DROP CONSTRAINT default_rank
GO

-- g. create / drop a table.
-- create table Physiotherapist

CREATE OR ALTER PROCEDURE addTablePhysiotherapist
AS
	CREATE TABLE Physiotherapist (
		id INT,
		name VARCHAR(50),
		salary INT,
		player_id INT
	)
GO

-- drop table Physiotherapist

CREATE OR ALTER PROCEDURE dropTablePhysiotherapist
AS
	DROP TABLE IF EXISTS Physiotherapist
GO


-- d. add / remove a primary key;
-- set id from Physiotherapist as primary key

CREATE OR ALTER PROCEDURE addPrimaryKeyPhysiotherapist
AS
	ALTER TABLE Physiotherapist
	ADD CONSTRAINT pk_id PRIMARY KEY(id)
GO

-- remove id primary key from Physiotherapist

CREATE OR ALTER PROCEDURE removePrimaryKeyPhysiotherapist
AS
	ALTER TABLE Physiotherapist
	DROP CONSTRAINT IF EXISTS pk_id
GO

-- e. add / remove a candidate key;
-- add candidate key to fan

CREATE OR ALTER PROCEDURE addCandidateKeyToFan
AS
	ALTER TABLE Fan
		ADD CONSTRAINT fan_ck UNIQUE (name, age, country)
GO

-- remove candidate key from fan

CREATE OR ALTER PROCEDURE removeCandidateKeyFromFan
AS
	ALTER TABLE Fan
		DROP CONSTRAINT IF EXISTS fan_ck
GO

-- f. add / remove a foreign key;
-- add player_id from Physiotherapist as foreign key

CREATE OR ALTER PROCEDURE addForeignKey
AS
	ALTER TABLE Physiotherapist
		ADD CONSTRAINT fk_playerId
			FOREIGN KEY(player_id) REFERENCES Player(id) ON DELETE CASCADE
GO

-- remove foreign key player_id from Physiotherapist

CREATE OR ALTER PROCEDURE removeForeignKey
AS
	ALTER TABLE Physiotherapist
		DROP CONSTRAINT IF EXISTS fk_playerId
GO

-- versions table
/*
CREATE TABLE versionsTable (
	version INT
)

INSERT INTO versionsTable VALUES (1) --the initial version

CREATE TABLE proceduresTable (
	fromVersion INT,
	toVersion INT,
	PRIMARY KEY(fromVersion, toVersion),
	procedureName VARCHAR(100)
)

INSERT INTO proceduresTable
	(fromVersion, toVersion, procedureName)
VALUES
	(1, 2, 'setPlayerAgeToTinyInt'),
	(2, 1, 'setPlayerAgeToInt'),
	(2, 3, 'addBestRankToPlayer'),
	(3, 2, 'removeBestRankFromPlayer'),
	(3, 4, 'addDefaultToRankFromPlayer'),
	(4, 3, 'removeDefaultFromRankFromPlayer'),
	(4, 5, 'addTablePhysiotherapist'),
	(5, 4, 'dropTablePhysiotherapist'),
	(5, 6, 'addPrimaryKeyPhysiotherapist'),
	(6, 5, 'removePrimaryKeyPhysiotherapist'),
	(6, 7, 'addCandidateKeyToFan'),
	(7, 6, 'removeCandidateKeyFromFan'),
	(7, 8, 'addForeignKey'),
	(8, 7, 'removeForeignKey');
*/

CREATE OR ALTER PROCEDURE goToVersion(@newVersion INT) 
AS
	DECLARE @curr INT
	DECLARE @procedureName VARCHAR(100)
	SELECT @curr = version FROM versionsTable

	IF  @newVersion > (SELECT MAX(toVersion) FROM proceduresTable)
		RAISERROR ('Bad version', 10, 1)
	ELSE
	BEGIN
		IF @newVersion = @curr
			PRINT('Already on this version!');
		ELSE
		BEGIN
			IF @curr > @newVersion
			BEGIN
				WHILE @curr > @newVersion
				BEGIN
					SELECT @procedureName = procedureName FROM proceduresTable 
					WHERE fromVersion = @curr AND toVersion = @curr - 1
					PRINT('executing: ' + @procedureName);
					EXEC(@procedureName)
					SET @curr = @curr - 1
				END
			END

			IF @curr < @newVersion
			BEGIN
				WHILE @curr < @newVersion
					BEGIN
						SELECT @procedureName = procedureName FROM proceduresTable
						WHERE fromVersion = @curr AND toVersion = @curr + 1
						PRINT('executing: ' + @procedureName);
						EXEC (@procedureName)
						SET @curr = @curr + 1
					END
			END

			UPDATE versionsTable SET version = @newVersion
		END
	END
GO


EXEC goToVersion 1


--SELECT * FROM proceduresTable;
SELECT * FROM versionsTable;
--SELECT * FROM Player;
