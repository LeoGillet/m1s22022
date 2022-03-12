CREATE TABLE Dragons (
    Dragon varchar(30) PRIMARY KEY,
    Sexe char(1) constraint Sexe check (Sexe = 'M' or Sexe = 'F'),
    Longueur int constraint Longueur check (Longueur > 0),
    Ecailles int constraint Ecailles check (Ecailles >= 0),
    CracheFeu char(1) constraint CracheFeu check (CracheFeu = 'O' or CracheFeu = 'N'),
    EnAmour varchar(7) constraint EnAmour check (EnAmour = 'macho' or EnAmour = 'timide' or EnAmour = 'sincère' or EnAmour = 'volage')
);