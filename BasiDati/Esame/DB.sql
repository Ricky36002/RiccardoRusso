create domain PosInteger as integer check (value >= 0);

create domain StringaM as varchar(100);

create domain Email as Email;

create domain DataOra as Timestamp;

create domain Sconto as
  real check (value >= 0 and value <= 1);

create table Cliente(
    nome StringaM not null,
    cognome StringaM not null,
    email Email not null,
    primary key (email)
);

create table Ristorante(
    nome StringaM not null,
    partitaIVa StringaM not null,
    primary key (nome),
    foreign key (id) references Prenotazione,
);

create table Promozione(
    nome StringaM not null,
    sconto Sconto not null,
    n_coperti PosInteger not null,
    primary key (nome)
    foreign key (id) references Prenotazione,
);

create table Prenotazione(
    id PosInteger not null,
    istante_pren DataOra not null,
    istante_app DataOra not null,
    n_coperti PosInteger not null,
    istanteUt DataOra not null,
    tipo Tipo not null,
    primary key (id)
    foreign key (nome) references Cliente,
);