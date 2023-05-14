use football;

/*1. Посчитать количество игроков каждой футбольной позиции(DEFENDER,
FORWARD и т.д)
таблица: PLAYERS*/

select role as `Позиция игрока`, count(player_id) as `Количество игроков`
from players
group by role;

/*2. Отсортировать эти позиции по убыванию количества игроков
таблица: PLAYERS*/

select role as `Позиция игрока`, count(player_id) as `Количество игроков`
from players
group by role
order by count(player_id) desc;

/*3. Найти самую популярную и самую непопулярную позицию
таблица: PLAYERS*/

select role as `Самая популярная позиция`, count(player_id) as `Количество игроков`
from players
group by role
order by count(player_id) desc
limit 1;

select role as `Самая непопулярная позиция`, count(player_id) as `Количество игроков`
from players
group by role
order by count(player_id) 
limit 1;

/*4. Найти игрока, который забил больше всего мячей
таблица: LINEUPS*/

select player_id, sum(goals)
from lineups
group by player_id
order by sum(goals) desc
limit 1;

/*5. Вывести полную информацию об этом игроке(ФИО, команда)*/

select concat(first_name, ' ', last_name) as `Игрок`, team as `Команда`
from games inner join lineups 
on games.game_id = lineups.game_id
inner join players 
on lineups.player_id = players.player_id
where players.player_id =  '10'; -- id игрока выяснили в предыдущем запросе
/*ИЛИ полный запрос 
select concat(first_name, ' ', last_name) as `Игрок`, team as `Команда`
from games inner join lineups 
on games.game_id = lineups.game_id
inner join players 
on lineups.player_id = players.player_id
where players.player_id =
(select player_id
from lineups
group by player_id
order by sum(goals) desc
limit 1) ; */

/*6. Найти игрока, который забил больше всего мячей и при этом получил желтую
карточку
Таблица: LINEUPS, поле: cards, значение: Y*/


select player_id, cards, sum(goals) as ` Сумма голов`
from lineups
where cards = 'Y'
group by player_id
order by sum(goals) desc
limit 1;

/*7. Вывести полную информацию об этом игроке(ФИО, команда)*/

select concat(first_name, ' ', last_name) as `Игрок`, team as `Команда`
from games inner join lineups 
on games.game_id = lineups.game_id
inner join players 
on lineups.player_id = players.player_id
where players.player_id =  '14'; -- id игрока выяснили в предыдущем запросе
/*ИЛИ полный запрос 
select concat(first_name, ' ', last_name) as `Игрок`, team as `Команда`
from games inner join lineups 
on games.game_id = lineups.game_id
inner join players 
on lineups.player_id = players.player_id
where players.player_id =
(select player_id
from lineups
where cards = 'Y'
group by player_id
order by sum(goals) desc
limit 1 ); 
*/


/*8. Вывести полную информацию про всех игроков(ФИО, команда, количество
забитых мячей)*/

select concat(first_name, ' ', last_name) as `Игрок`, team as `Команда`, lineups.goals as `Колличество забитых мячей`
from games inner join lineups 
on games.game_id = lineups.game_id
inner join players 
on lineups.player_id = players.player_id
order by lineups.goals desc ;

/*9. Объединить все таблицы и вывести полную информацию из них*/

select *
from games inner join lineups 
on games.game_id = lineups.game_id
inner join players 
on lineups.player_id = players.player_id



