# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay_fact"
user_table_drop = "DROP TABLE IF EXISTS user_dim"
song_table_drop = "DROP TABLE IF EXISTS song_dim"
artist_table_drop = "DROP TABLE IF EXISTS artist_dim"
time_table_drop = "DROP TABLE IF EXISTS time_dim"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplay_fact
        (
            songplay_id serial,
            song_id varchar NOT NULL,
            artist_id varchar NOT NULL,
            session_id int, user_id int,
            level varchar, location varchar,
            start_time timestamp NOT NULL,
            user_agent varchar,
            CONSTRAINT songplay_fact_pkey PRIMARY KEY (songplay_id)
        );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS user_dim
        (
            user_id int NOT NULL,
            first_name varchar,
            last_name varchar,
            gender varchar,
            level varchar,
            CONSTRAINT user_dim_pkey PRIMARY KEY (user_id)
        );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS song_dim
        (
            song_id varchar NOT NULL,
            artist_id varchar NOT NULL,
            title varchar,
            year varchar,
            duration varchar,
            CONSTRAINT song_dim_pkey PRIMARY KEY (song_id)
        );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artist_dim
        (
            artist_id varchar NOT NULL,
            artist_name varchar NOT NULL,
            artist_location varchar,
            artist_latitude varchar,
            artist_longitude varchar,
            CONSTRAINT artist_dim_pkey PRIMARY KEY (artist_id)
        );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time_dim
        (
            start_time timestamp NOT NULL,
            year varchar,
            month varchar,
            week varchar,
            weakday varchar,
            day varchar,
            hour varchar,
            CONSTRAINT time_dim_pkey PRIMARY KEY (start_time)
        );
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplay_fact (song_id, artist_id, session_id, user_id, level, location, start_time, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """)

user_table_insert = ("""
    INSERT INTO user_dim (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT ON CONSTRAINT user_dim_pkey DO UPDATE SET level = EXCLUDED.level
    """)
 
song_table_insert = ("""
    INSERT INTO song_dim (artist_id, song_id, title, duration, year)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT ON CONSTRAINT song_dim_pkey DO NOTHING
    """)

artist_table_insert = ("""
    INSERT INTO artist_dim (artist_id, artist_name, artist_latitude, artist_longitude, artist_location)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT ON CONSTRAINT artist_dim_pkey DO NOTHING
    """)

time_table_insert = ("""
    INSERT INTO time_dim (start_time, year, month, week, weakday, day, hour)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT ON CONSTRAINT time_dim_pkey DO NOTHING
    """)

# FIND SONGS

song_select = ("""
    SELECT sd.song_id, ad.artist_id
      FROM song_dim sd
      JOIN artist_dim ad
        ON sd.artist_id = ad.artist_id
     WHERE sd.title = %s
       AND sd.duration = %s
       AND ad.artist_name = %s
    """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]