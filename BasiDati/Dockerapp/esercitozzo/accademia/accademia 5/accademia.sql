
select wp.nome, wp.inizio, wp.fine
from wp, progetto p
where wp.progetto = p.id
	and p.nome = 'Pegasus'


select distinct s.nome, s.cognome, s.posizione
from attivitaprogetto ap, progetto p, persona s
where ap.progetto = p.id 
	and ap.persona = s.id
	and p.nome = 'Pegasus';


select distinct s.id, s.nome, s.cognome, s.posizione
from attivitaprogetto a1, attivitaprogetto a2, persona s, progetto p
where a1.id <> a2.id 
	and a1.progetto = a2.progetto
	and a1.persona = a2.persona
	and a1.persona = s.id
	and a1.progetto = p.id
	and p.nome = 'Pegasus';


select distinct s.id, nome, cognome, posizione 
from assenza a, persona s
where a.persona = s.id
	and tipo = 'Malattia' 
	and posizione = 'Professore Ordinario';



select distinct s.id, s.nome, s.cognome
from persona s, assenza a1, assenza a2
where a1.persona = s.id
        and a2.persona = s.id
        and a1.id <> a2.id
        and a1.tipo = 'Malattia'
        and a2.tipo = 'Malattia'
        and s.posizione = 'Professore Ordinario';



select distinct p.id, p.nome, p.cognome
from persona p, attivitanonprogettuale a
where p.id = a.persona
    and a.tipo = 'Didattica'
    and p.posizione = 'Ricercatore';



select s.id, s.nome,  s.cognome, s.posizione
from persona s,  attivitanonprogettuale anp1, attivitanonprogettuale anp2
where anp1.id <> anp2.id
    and anp1.tipo = 'Didattica'
    and anp2.tipo = 'Didattica'
    and anp1.persona = s.id
    and anp2.persone = s.id
    and s.posizione = 'Ricercatore';

select distinct p.id, p.nome, p.cognome
from persone.p, attivitanonprogetto ap, attivitanonprogettuale anp
where p.id = ap. persone
    and p.id = anp.persone
    and ap.giorno = anp.giorno


select distinct p.id




select distinct Persona.nome, Persona.cognome
from Persona, AttivitaProgetto, Assenza
where Persona.id = AttivitaProgetto.persona and Persona.id = Assenza.persona and AttivitaProgetto.giorno = Assenza.giorno;



select distinct Persona.nome, Persona.cognome, AttivitaProgetto.giorno, Progetto.nome progetto,
       Assenza.tipo causa_assenza, AttivitaProgetto.oreDurata
from Persona, AttivitaProgetto, Assenza, Progetto
where Persona.id = AttivitaProgetto.persona and Persona.id = Assenza.persona and AttivitaProgetto.progetto = Progetto.id and AttivitaProgetto.giorno = Assenza.giorno;




select WP1.nome, Progetto1.nome progetto1, Progetto2.nome progetto2
from WP WP1, Progetto Progetto1, WP WP2, Progetto Progetto2
where WP1.progetto = Progetto1.id and WP1.nome = WP2.nome AND WP1.progetto <> WP2.progetto and WP2.progetto = Progetto2.id;