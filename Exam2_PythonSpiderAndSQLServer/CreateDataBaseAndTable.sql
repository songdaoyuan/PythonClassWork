CREATE DATABASE PySpiderData
GO
USE PySpiderData
GO
SELECT * FROM MoviesTop250
GO
CREATE TABLE MoviesTop250(
    mvRank int NOT NULL PRIMARY KEY,
	mvName varchar(50) NULL,
	mvBriefIntroduction varchar(200) NULL,
	mvGrade float NULL,
)
GO
