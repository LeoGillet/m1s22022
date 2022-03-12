CREATE TABLE Repas (
	Dragon varchar(30) REFERENCES dragons(Dragon),
	Produit varchar(30) REFERENCES nourritures(Produit),
	Quantite int CONSTRAINT Quantite CHECK (Quantite > 0),
	PRIMARY KEY (Dragon, Produit)	
);