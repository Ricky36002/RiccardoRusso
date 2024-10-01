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
    nazione  varchar(100) not null,
    primary key(nome, regione),
    foreign key (regione, nazione) references Regione(nome, nazione),
);
create table  TipoVeicolo(
    nome varchar(100) not null,
    primary key(nome),
);
create table  Marca(
    nome varchar(100) not null,
    primary key (nome),
);
create table  Modello(
    nome varchar(100) not null,
    marca varchar(100) not null,
    tipoveicolo varchar(100) not null,
    primary key(nome, marca),
    foreign key (marca),
    foreign key (tipoveicolo),
    references Marca(nome),
    references TipoVeicolo(nome),
);
create table  Veicolo(
    targa Targa not null,
    immatricolazione intger not null,
    foreign key (targa) references Modello,
);
create table Riparazione(
    riconsegna timestamp not null,
    codice integer not null,
    inizio timestamp not null,
    primary key (codice),
);
create table Persona(
    cf CodiceFiscale not null,
    nome varchar (100) not null,
    indirizzo Indirizzo not null,
    telefono varchar(20)not null,
    primary key (cf),
    foreign key (citta) references Città (nome, regione, nazione)
);
create table Cliente(
    persona CodFis not null
    primary key (persona),
    foreign key (persona)  references Persona (cf)
);


















create table  Officina(
    nome varchar(100) not null,
    indirizzo Indirizzo not null,
    id integer not null,
    primary key(id),
    foreign key 
)