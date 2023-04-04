-- modifier la valeur de l’age de Betty de 23 ans a 20 ans.
update etudiants
    -> set age =20
    -> where prenom = 'Betty';

-- Afficher à nouveau les informations de Betty

select *
    -> from etudiants;