CREATE TABLE Nourritures (
	Produit varchar(30) PRIMARY KEY,
	Calories int CONSTRAINT Calories CHECK (CALORIES > 0)
);