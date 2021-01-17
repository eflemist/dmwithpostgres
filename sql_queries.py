# DROP TABLES

songplay_table_drop = "DROP table songplay_fact"
user_table_drop = "DROP table user_dim"
song_table_drop = "DROP table song_dim"
artist_table_drop = "DROP table artist_dim"
time_table_drop = "DROP table time_dim"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplay_fact (songplay_id int, song_id int, artist_id int, session_id int, user_id int, level varchar, location varchar, start_time varchar, user_agent varchar);""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS user_dim (user_id int, first_name varchar, last_name varchar, gender varchar, level varchar);""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS song_dim (song_id int, artist_id int, title varchar, year varchar, duration varchar);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artist_dim (artist_id int, name varchar, location varchar, latitude varchar, longitude varchar);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time_dim (start_time varchar, year varchar, month varchar, week varchar, weakday varchar, day varchar, hour varchar);""")


# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]