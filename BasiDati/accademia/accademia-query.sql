select distinct cognome 
from Persona;

select  nome, cognome 
from Persona
where posizione = 'Ricercatore';

select *
From Persona
where cognome like 'V%';

select *
From Persona
where cognome like 'V%'  and (posizione = 'Professore Associato' or posizione = 'Professore Ordinario');

select *
From Progetto
where fine < CURRENT_DATE;

select *
From  Progetto
order by inizio asc;

select *
From WP
order by nome asc;

select distinct tipo
From Assenza;

select distinct tipo 
From AttivitaProgetto;

select distinct giorno
From AttivitaNonProgettuale
where tipo = 'Didattica'
order by  giorno asc;

