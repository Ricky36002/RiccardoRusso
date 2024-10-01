select posizione, count(posizione)
from persone
group by posizione;


select count(*)
from persona
where stipendio >= 40000;


select count(*)
from progetto
where budget > 50000 and fine < CURRENT_DATE;


select cast(avg(ap.oreDurata) as decimal(10,2)) as media, max(ap.oreDurata) as massimo, min(ap.oreDurata) as minimo
from attivitaProgetto ap, progetto p
where ap.progetto = p.id and p.nome = 'Pegasus';

select cast(avg(ap.oreDurata) as decimal(10,2)) as media, max(ap.oreDurata) as massimo, min(ap.oreDurata) as minimo
from attivitaProgetto ap, progetto p
where ap.progetto = p.id and p.nome = 'Pegasus';


select u.id, u.nome, u.cognome, sum(anp.oreDurata) as ore_didattica
from attivitaNonProgettuale anp, persona u
where anp.tipo = 'Didattica' and anp.persona = u.id
group by u.id;


select cast(avg(stipendio) as decimal(10,2)) as media, max(stipendio) as massimo, min(stipendio) as minimo
from persona
where posizione = 'Ricercatore';


select posizione, cast(avg(stipendio) as decimal(10,2)) as media, max(stipendio) as massimo, min(stipendio) as minimo
from persona
group by posizione;


select p.id, p.nome, sum(ap.oreDurata) as totale_ore
from progetto p, attivitaProgetto ap, persona u
where ap.persona = u.id and u.nome = 'Ginevra' and u.cognome = 'Riva' and ap.progetto = p.id
group by p.id;


select p.id, p.nome
from progetto p, attivitaProgetto ap, persona u
where ap.persona = u.id and ap.progetto = p.id
group by p.id
having count(u.id)>2;
