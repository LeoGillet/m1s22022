CREATE TABLE Amours (
	DragonAimant varchar(30) PRIMARY KEY
							 REFERENCES dragons(dragon),
	DragonAime varchar(30) REFERENCES dragons(dragon),
	Force varchar(13) CONSTRAINT Force CHECK (Force = 'un peu' or Force = 'beaucoup' or Force = 'passionnement' or Force = 'a la folie')
);