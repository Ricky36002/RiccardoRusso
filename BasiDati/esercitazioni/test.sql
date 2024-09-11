create database accademia;
create type Struttorato as enum
    ('Ricercatore', 'Professore Associato', 'Professore Ordinario');
create type LavoroProggetto as enum
    ('Ricerca e Sviluppo', 'Dimostrazione', 'Management', 'Altro');
create type LavoroNonProgettuale as enum
    ('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro Accademico', 'Altro');
create type  CausaAssenza as enum
    ('Chiusura Universitaria', 'Maternita', 'Malattia');
create domain PosInteger as Integer
    check (value >= 0);
create domain StringaM as varchar (100);

create domain NumeroOre Integer
    check (value >= 0 and value <= 8 );
create domain Denaro as real
    check (value >= 0);

create table Persona ( id PosInteger, nome StringaM, cognome StringaM, posizione Struttorato, stipendio Denaro,
primary key(id));
create table Progetto (id PosInteger, nome StringaM, inizio date, fine date check (inizio<fine), budget Denaro, primary key (id), unique (nome));

create table WP (progetto PosInteger, id PosInteger, nome StringaM, inizio date, fine date check (inizio<fine),
primary key(id, progetto), unique(progetto, nome), foreign key (progetto) references Progetto(id));
create table AttivitaProgetto (id PosInteger, persona PosInteger, progetto PosInteger, wp PosInteger, giorno date, tipo LavoroProggetto, oreDurata NumeroOre,
primary key (progetto), foreign key(persona) references Persona(id), foreign key(Progetto) references Progetto(id));
create table AttivitaNonProgettuale (id PosInteger, persona PosInteger,  tipo LavoroNonProgettuale, giorno date, oreDurate NumeroOre,
primary key (id), foreign key(persona) references Persona(id));
create table Assenza (id PosInteger, persona PosInteger, tipo CausaAssenza, giorno date, 
primary key(id), foreign key(persona) references Persona(id), unique(persona, giorno));

 










