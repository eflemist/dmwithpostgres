# DROP TABLES

songplay_table_drop = "DROP table songplay_fact"
user_table_drop = "DROP table user_dim"
song_table_drop = "DROP table song_dim"
artist_table_drop = "DROP table artist_dim"
time_table_drop = "DROP table time_dim"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplay (song_title varchar, artist_name varchar, year int, album_name varchar, single varchar);""")

user_table_create = ("""
""")

song_table_create = ("""
""")

artist_table_create = ("""
""")

time_table_create = ("""
""")

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