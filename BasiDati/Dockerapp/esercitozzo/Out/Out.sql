create domain CodFis as varchar(16);
create type Denaro as (
    value decimal(10, 2),
    currency varchar(3)
);

create type Indirizzo as (
    via varchar(30),
    civico varchar(5),
    cap varchar(5)
);

create table Nazione(
    nome varchar(100) not null,
    primary key(nome)
);
create table  Regione(
    nome varchar(100) not null,
    nazione varchar(100) not null,
    primary key(nome, nazione),
    foreign key (nazione) references Nazione(nome)
);
create table Città(
    id integer not null,
    nome varchar(100) not null,
    regione varchar(100) not null,
    nazione varchar(100) not null,
    primary key(id),
    unique (nome, regione, nazione),
    foreign key (regione, nazione) references Regione(nome, nazione)
);
create table Sede(
    indirizzo Indirizzo not null,
    nome varchar(100) not null,
    citta varchar(100) not null,
    regione varchar(100) not null,
    nazione varchar(100) not null,
    id integer not null,
    primary key (id),
    foreign key (citta, regione, nazione) references Città(nome, regione, nazione)
);
create table Sala(
    nome varchar(100) not null,
    sede integer not null,
    primary key (nome, sede),
    foreign key (sede) references Sede(id)
);
create table Genere(
    nome varchar(100) not null,
    primary key(nome)
);
create table TipoSpettacolo(
    nome varchar(100) not null,
    primary key (nome)
);
create table Artista(
    id  integer not null,
    nome varchar(100) not null,
    cognome varchar(100) not null,
    nome_arte varchar(100),
    primary key (id)
);
create table Utente(
    nome varchar(100) not null,
    cognome varchar(100) not null,
    cf CodFis not null,
    primary key (cf)
);
create table Spettacolo(
    nome varchar(100) not null,
    dutata_minuti integer not null,
    tipo varchar(100) not null,
    genere varchar(100) not null,
    id integer not null,
    primary key (id),
    foreign key (tipo) references TipoSpettacolo(nome),
    foreign key (genere)  references Genere(nome)
    -- v. incl. (id) occorre in Partecipa(spettacolo)
);

create table Partecipa (
    spettacolo integer not null,
    artista integer not null,
    foreign key (spettacolo) references Spettacolo(id),
    foreign key (artista) references Artista(id),
    primary key (spettacolo, artista)
);

create table Evento(
    data_evento Date not null,
    orario time not null,
    sala varchar(100)not null,
    id integer not null,
    sede  integer not null,
    spettacolo  integer not null,
    primary key (id)
    foreign key (sala, sede) references Sala(nome, sede),
    foreign key (spettacolo) references Spettacolo (id),
);


create table Settore(
    id serial primary key not null,
    nome varchar(100) not null,
    sala varchar(100) not null,
    sede integer not null,
    unique(nome, sala, sede),
    foreign key (sala, sede) references Sala(nome, sede)
);
create table Posto(
    fila integer not null,
    colonna integer not null,
    settore integer not null,
    foreign key (settore)  references Settore(id),
    primary key (fila, colonna, settore)
);



create table TipoTariffa(
    nome  varchar(100) not null,
    primary key (nome)
);

create table Tariffa(
    prezzo Denaro not null,
    settore integer not null,
    evento integer not null,
    tipo varchar(100) not null,
    primary key  (settore, evento, tipo),
    foreign key (settore) references Settore(id),
    foreign key (evento) references Evento(id),
    foreign key (tipo) references TipoTariffa(nome)
);


create table Prenotazione(
    id integer not null,
    utente CodFis not null,
    evento integer not null,
    primary key (id),
    foreign key (utente) references Utente(cf),
    foreign key (evento) references Evento(id)
);

create table pre_posto(
    tipotariffa varchar(100) not null,
    settore integer not null,
    fila integer not null,
    colonna integer not null,
    prenotazione  integer not null,
    foreign key (prenotazione) references Prenotazione(id),
    foreign key (settore, fila, colonna) references Posto(settore, fila, colonna),
    foreign key (tipotariffa) references TipoTariffa(nome)
);
-- foreign key (settore) references Settore(id),