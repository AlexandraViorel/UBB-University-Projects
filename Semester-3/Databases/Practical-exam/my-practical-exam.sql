use [examen-practic];

DROP TABLE IF EXISTS Playlog;
DROP TABLE IF EXISTS PlaylistSong;
DROP TABLE IF EXISTS Playlist;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Song;
DROP TABLE IF EXISTS Artist;

CREATE TABLE Artist(
	aid INT PRIMARY KEY IDENTITY(1, 1),
	firstname VARCHAR(50),
	lastname VARCHAR(50),
	debutdate DATE
);

CREATE TABLE Song(
	songid INT PRIMARY KEY IDENTITY(1, 1),
	title VARCHAR(50),
	duration INT,
	genre VARCHAR(50),
	artist INT REFERENCES Artist(aid)
);

CREATE TABLE Users(
	userid INT PRIMARY KEY IDENTITY(1, 1),
	username VARCHAR(50) UNIQUE,
	email VARCHAR(50) UNIQUE,
	dateofbirth DATE
);

CREATE TABLE Playlist(
	pid INT PRIMARY KEY IDENTITY(1, 1),
	name VARCHAR(50),
	datetimecreation DATETIME,
	userid INT REFERENCES Users(userid)
);

CREATE TABLE PlaylistSong(
	psid INT PRIMARY KEY IDENTITY(1, 1),
	playlist INT REFERENCES Playlist(pid),
	song INT REFERENCES Song(songid)
);

CREATE TABLE Playlog(
	plid INT PRIMARY KEY IDENTITY(1, 1),
	userid INT REFERENCES Users(userid),
	song INT REFERENCES Song(songid),
	timepl TIME
);


INSERT INTO Artist
	(firstname)
VALUES
	('a1'),
	('a2'),
	('a3'),
	('a4'),
	('a5');

INSERT INTO Song
	(genre, artist)
VALUES
	('pop', 1),
	('rock', 2),
	('jazz', 3),
	('electronic', 4),
	('pop', 5),
	('rock', 1),
	('jazz', 1),
	('electronic', 1),
	('pop', 3),
	('rock', 3),
	('jazz', 3),
	('electronic', 3);

INSERT INTO Users
	(email, username)
VALUES	
	('e1', 'u1'),
	('e2', 'u2'),
	('e3', 'u3'),
	('e4', 'u4'),
	('e5', 'u5');

INSERT INTO Playlist
	(name, userid)
VALUES
	('p1', 1),
	('p2', 2),
	('p3', 3),
	('p4', 4),
	('p5', 5);

INSERT INTO PlaylistSong
	(playlist, song)
VALUES
	(1, 1),
	(1, 5),
	(1, 9),
	(2, 2),
	(2, 6),
	(2, 10),
	(3, 2),
	(3, 6),
	(3, 10),
	(5, 2),
	(5, 6),
	(5, 10);

INSERT INTO Playlog
	(userid, song, timepl)
VALUES
	(1, 1, '01:00am'),
	(2, 1, '01:00am'),
	(3, 2, '01:00am'),
	(4, 2, '01:00am'),
	(5, 3, '10:01am'),
	(1, 3, '10:02am'),
	(5, 4, '09:09am');

-- 2.

DROP PROCEDURE IF EXISTS ex2proc
GO

CREATE PROCEDURE ex2proc(@userid INT, @songid INT)
AS
BEGIN
	IF EXISTS (SELECT * FROM Users WHERE userid = @userid) AND EXISTS (SELECT * FROM Song WHERE songid = @songid)
		INSERT INTO Playlog
			(userid, song, timepl)
		VALUES
			(@userid, @songid, GETDATE())
	ELSE
		raiserror('User or song does not exist!', 12, 1)
END
GO

SELECT * FROM Playlog;

exec ex2proc @userid = 1, @songid = 10

-- 3.

DROP VIEW IF EXISTS ex3view
GO

CREATE VIEW ex3view
AS
	SELECT TOP 3 * FROM Song S
	WHERE S.songid IN
		(SELECT PL.song FROM Playlog PL
		 WHERE PL.timepl = '1:00am'
		 GROUP BY PL.song
		 HAVING COUNT(*) <= (SELECT TOP 1 COUNT(S1.songid) AS nbplayed FROM Song S1
							 INNER JOIN Playlog PL1 ON PL1.song = S1.songid
							 GROUP BY S1.songid
							 ORDER BY nbplayed DESC))
GO

SELECT * FROM ex3view

-- 4. 

DROP FUNCTION IF EXISTS ex4function
GO

CREATE FUNCTION ex4function(@X INT, @Y VARCHAR(50))
	RETURNS TABLE 
AS
	RETURN
		SELECT COUNT(PL.pid) AS nbofplaylists FROM Playlist PL
		WHERE PL.pid IN
			(SELECT A.playlist FROM
				(SELECT COUNT(*) as nb, P.playlist FROM PlaylistSong P
				INNER JOIN Song S ON S.songid = P.song
				WHERE S.genre = @Y
				GROUP BY S.genre, P.playlist) A
			WHERE A.nb > @X)
GO

SELECT * FROM ex4function(2, 'rock')
