# Instructions 

First, cd to the population-database folder and run the `create_cities_db.py` program. The program will create a database named cities.db. The cities.db database will have a table named `Cities`, with the following columns:


| Column Name | Data Type |
| ----------- | --------- |
| CityID | INTEGER PRIMARY KEY |
| CityName | TEXT |
| Population | REAL |

The `CityName` column stores the name of a city and the `Population` column stores the population of that city. After you run the `create_cities_db.py` program, the `Cities` table will contain 20 rows with various cities and their populations. Next, write a program that connects to the `cities.db` database, and allows the user to select any of the following operations:

* Display a list of cities sorted by population, in ascending order. 
* Display a list of cities sorted by population, in descending order.
* Display a list of cities sorted by name.
* Display the total population of all the cities.
* Display the average population of all the cities.
* Display the city with the highest population.
* Display the city with the lowest population.

Review [Getting Started with the Population Database Problem](https://mediaplayer.pearsoncmg.com/assets/gaddis_sowp6e_getting_started_with_population_db_prob) VideoNotes. You will see the output you should have for this programming challenge as well as the code.