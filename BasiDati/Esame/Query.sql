-- Query 1
select p.nome, p.cognome, COUNT(distinct ap.progetto) as numero_progetti
from Persona p
join AttivitaProgetto ap on p.id = ap.persona
where p.posizione = 'Professore Ordinario'
group by p.id, p.nome, p.cognome;

-- Query 2: non risposto

-- Query 3
select p.id, p.nome, p.cognome, p.posizione, p.stipendio
from Persona p
where p.stipendio >= 60000;

-- Query 4

select p.nome, p.cognome,
       SUM(pr.budget) AS budget_totale
from Persona p
join AttivitaProgetto ap ON p.id = ap.persona
join Progetto pr ON ap.progetto = pr.id
where p.posizione = 'Professore Associato'
group by p.id, p.nome, p.cognome;

-- Query 5

select p.nome, p.cognome,
       (select COUNT(*)
        from Assenza a
        where a.persona = p.id and a.tipo = 'Maternita') as giorni_maternita
from Persona p
where p.posizione = 'Ricercatore';

-- Query 6

select AVG(budget) as budget_medio
from Progetto;

-- Query 7

select p.nome, p.cognome, 
       SUM(ap.oreDurata) as ore_totali_progetto_3
from Persona p
join AttivitaProgetto ap on p.id = ap.persona
where ap.progetto = 3
group by p.id;

-- Query 8

select p.nome, p.cognome, 
       SUM(ap.oreDurata) as ore_totali_svolte
from Persona p
join AttivitaProgetto ap on p.id = ap.persona
join WP w on ap.progetto = w.progetto and ap.wp = w.id
where p.posizione = 'Professore Ordinario'
  and w.progetto = 4
  and w.id = 3
group by p.id;


-- Query 9
select p.nome, p.cognome, p.stipendio
from Persona p
where p.posizione = 'Professore Ordinario'
  and p.stipendio >= 60000
  and exists (
      select 1
      from AttivitaProgetto ap
      where ap.persona = p.id
  );

-- Query 10

select p.nome, p.cognome, 
       AVG(anp.oreDurata) as ore_media_didattica
from Persona p
join AttivitaNonProgettuale anp on p.id = anp.persona
where anp.tipo = 'Didattica'
group by p.id;

