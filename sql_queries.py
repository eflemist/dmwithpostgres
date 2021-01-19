# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay_fact"
user_table_drop = "DROP TABLE IF EXISTS user_dim"
song_table_drop = "DROP TABLE IF EXISTS song_dim"
artist_table_drop = "DROP TABLE IF EXISTS artist_dim"
time_table_drop = "DROP TABLE IF EXISTS time_dim"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplay_fact (songplay_id serial, song_id varchar, artist_id varchar, session_id int, user_id int, level varchar, location varchar, start_time varchar, user_agent varchar);""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS user_dim (user_id int, first_name varchar, last_name varchar, gender varchar, level varchar);""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS song_dim (song_id varchar, artist_id varchar, title varchar, year varchar, duration varchar);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artist_dim (artist_id varchar, artist_name varchar, artist_location varchar, artist_latitude varchar, artist_longitude varchar);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time_dim (start_time varchar, year varchar, month varchar, week varchar, weakday varchar, day varchar, hour varchar);""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplay_fact (song_id, artist_id, session_id, user_id, level, location, start_time, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""")

user_table_insert = ("""INSERT INTO user_dim (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)""")
 
song_table_insert = ("""INSERT INTO song_dim (artist_id, song_id, title, duration, year) VALUES (%s, %s, %s, %s, %s)""")

artist_table_insert = ("""INSERT INTO artist_dim (artist_id, artist_name, artist_latitude, artist_longitude, artist_location) VALUES (%s, %s, %s, %s, %s)""")

time_table_insert = ("""INSERT INTO time_dim (start_time, year, month, week, weakday, day, hour) VALUES (%s, %s, %s, %s, %s, %s, %s)""")

# FIND SONGS

song_select = ("""SELECT sd.song_id, ad.artist_id FROM song_dim sd JOIN artist_dim ad ON sd.artist_id = ad.artist_id WHERE sd.title = %s AND sd.duration = %s AND ad.artist_name = %s """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]