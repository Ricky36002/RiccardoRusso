create table Nazione(
    nome varchar(100) not null,
    primary key(nome),
);
create table  Regione(
    nome varchar(100) not null,
    nazione varchar(100) not null,
    primary key(nome, nazione),
    foreign key nazione references Nazione(nome),
);
create table  Città(
    nome varchar(100) not null,
    regione varchar(100) not null,
    nazione varchar(100) not null,
    primary key(nome, regione),
    foreign key (regione, nazione) references Regione(nome, nazione),
);
create table Sede(
    indirizzo Indirizzo not null,
    nome varchar(100) not null,
    regione varchar(100) not null,
    nazione varchar(100) not null,
    foreign key (regione, nazione) references Città(nome, regione, nazione)
);
create table Sala(
    nome varchar(100) not null,
    primary key (nome),
    foreign key (nome) references Sede(nome)
);