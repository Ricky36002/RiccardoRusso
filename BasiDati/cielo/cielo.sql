select v.codice, v.comp
from Volo v
where durataMinuti > 180;

select distinct  v.comp 
from Volo v
where durataMinuti > 180;

select v.codice, v.comp 
from Volo v, ArrPart a
where  a.codice = v.codice and a.partenza = 'CIA';

select distinct v.comp 
from Volo v, ArrPart a
where a.codice = v.codice and v.comp = a.comp and a.arrivo = 'FCO';

select distinct v.codice, v.comp
from Volo v, ArrPart a
where  a.codice = v.codice and v.comp = a.comp and a.arrivo = 'JFK' and a.partenza ='FCO';

select distinct v.comp
from  Volo v, ArrPart a
where a.codice = v.codice and v.comp = a.comp and a.arrivo = 'JFK' and a.partenza ='FCO';
--7. Quali sono i nomi delle compagnie che hanno voli diretti dalla città di ‘Roma’ alla città di ‘New York’ ?
select distinct a.comp
from ArrPart a
where a.partenza in (select aeroporto from LuogoAeroporto where città = 'Roma') and a.arrivano in (select aeroporto from LuogoAeroporto where città = 'New York');

select distinct a.codice, a.nome, l.città 
from Aeroporto a, LuogoAeroporto l 
where a.codice = l.aeroporto and a codice in(select distinct partenza from ArrPart where comp = 'Magicfly');

select *
from ArrPart
where partenza in (select aeroporto from LuogoAeroporto where città = 'Roma') and arrivo in(select aeroporto from LuogoAeroporto where città = 'New York');