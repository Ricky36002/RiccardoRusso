
-- quali sono i voli (codice e nome della compagnia) la cui durata supera le 3 ore?
-- 2. Quali sono le compagnie che hanno voli che superano le 3 ore?
-- 3. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto con
-- codice ‘CIA’ ?
-- 4. Quali sono le compagnie che hanno voli che arrivano all’aeroporto con codice
-- ‘FCO’ ?
-- 5. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto ‘FCO’
-- e arrivano all’aeroporto ‘JFK’ ?
-- 6. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’ e atter-
-- rano all’aeroporto ‘JFK’ ?
-- 7. Quali sono i nomi delle compagnie che hanno voli diretti dalla città di ‘Roma’ alla
-- città di ‘New York’ ?
-- 8. Quali sono gli aeroporti (con codice IATA, nome e luogo) nei quali partono voli
-- della compagnia di nome ‘MagicFly’ ?
-- 9. Quali sono i voli che partono da un qualunque aeroporto della città di ‘Roma’ e
-- atterrano ad un qualunque aeroporto della città di ‘New York’ ? Restituire: codice
-- del volo, nome della compagnia, e aeroporti di partenza e arrivo.
-- 10. Quali sono i possibili piani di volo con esattamente un cambio (utilizzando solo
-- voli della stessa compagnia) da un qualunque aeroporto della città di ‘Roma’ ad un
-- qualunque aeroporto della città di ‘New York’ ? Restituire: nome della compagnia,
-- codici dei voli, e aeroporti di partenza, scalo e arrivo.
-- 11. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’, atter-
-- rano all’aeroporto ‘JFK’, e di cui si conosce l’anno di fondazione?

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
where a.partenza in (select Aeroporto from LuogoAeroporto where città = 'Roma') and a.arrivano in (select Aeroporto from LuogoAeroporto where città = 'New York');