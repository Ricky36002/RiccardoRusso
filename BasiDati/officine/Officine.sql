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
create table Staff (
    persona CodFis not null,
    primary key (persona),
    foreign key (persona) references Persona(cf)
);

create table Dipendente (
    staff CodFis not null,
    officina integer not null,
    primary key (staff),
    foreign key (officina) references Officina(id),
);

create table Direttore (
    staff CodFis not null,
    nascita date not null,
    primary key (staff),
    foreign key (staff) references Staff(persona)
);

create table Lavorare (
    dipendente CodFis not null,
    id Integer not null,
    assunzione date not null,
    primary key (dipendente, id),
    foreign key (dipendente) references Dipendente(staff),
    foreign key (officina) references Officina(id)
);

create table Officina (
    id Integer not null,
    nome StringaM not null,
    indirizzo Indirizzo not null,
    direttore CodFis not null,
    citta StringaM not null,
    primary key (id),
    foreign key (direttore) references Direttore(staff),
    foreign key (citta) references Citta(nome, regione, nazione)
);

commit;