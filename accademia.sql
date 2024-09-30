
select distinct WP.nome, WP.inizio, WP.fine
from WP, Progetto
where WP.progetto = Progetto.id and Progetto.nome = 'Pegasus';


select distinct Persona.nome, Persona.cognome, Persona.posizione
from Persona, AttivitaProgetto, Progetto
where Persona.id = AttivitaProgetto.persona and AttivitaProgetto.progetto = Progetto.id and Progetto.nome = 'Pegasus'
ORDER BY Persona.cognome DESC;


select Persona.nome, Persona.cognome, Persona.posizione
from Persona, AttivitaProgetto, Progetto
where Persona.id = AttivitaProgetto.persona and AttivitaProgetto.progetto = Progetto.id and Progetto.nome = 'Pegasus' 
group by Persona.nome, Persona.cognome, Persona.posizione having count(AttivitaProgetto.id) > 1;



select distinct Persona.nome, Persona.cognome, Persona.posizione
from Persona, Assenza
where Persona.id = Assenza.persona and Persona.posizione = 'Professore Ordinario' and Assenza.tipo = 'Malattia';



select Persona.nome, Persona.cognome, Persona.posizione
from Persona, Assenza
where Persona.id = Assenza.persona and Persona.posizione = 'Professore Ordinario' and Assenza.tipo = 'Malattia' 
group by Persona.nome, Persona.cognome, Persona.posizione having count(Assenza.id) > 1;



select distinct Persona.nome, Persona.cognome, Persona.posizione
from Persona, AttivitaNonProgettuale
where Persona.id = AttivitaNonProgettuale.persona and Persona.posizione = 'Ricercatore' and AttivitaNonProgettuale.tipo = 'Didattica';



select Persona.nome, Persona.cognome, Persona.posizione
from Persona, AttivitaNonProgettuale
where Persona.id = AttivitaNonProgettuale.persona and Persona.posizione = 'Ricercatore' and AttivitaNonProgettuale.tipo = 'Didattica'
group by Persona.nome, Persona.cognome, Persona.posizione having count(AttivitaNonProgettuale.id) > 1;



select distinct Persona.nome, Persona.cognome
from Persona, AttivitaProgetto, AttivitaNonProgettuale
where Persona.id = AttivitaProgetto.persona and Persona.id = AttivitaNonProgettuale.persona and AttivitaProgetto.giorno = AttivitaNonProgettuale.giorno;



select distinct Persona.nome, Persona.cognome, AttivitaProgetto.giorno, Progetto.nome,
       AttivitaNonProgettuale.tipo, AttivitaProgetto.oreDurata oreProg, AttivitaNonProgettuale.oreDurata oreNonProg
from Persona, AttivitaProgetto, AttivitaNonProgettuale, Progetto
where Persona.id = AttivitaProgetto.persona and Persona.id = AttivitaNonProgettuale.persona and AttivitaProgetto.progetto = Progetto.id and AttivitaProgetto.giorno = AttivitaNonProgettuale.giorno;




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
