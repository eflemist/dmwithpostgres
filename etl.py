import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """ extracts data from file and populates the song and artist dimension tables """
    
    # open song file
    dataset = pd.read_json(filepath, lines=True)
    df = pd.DataFrame(dataset, columns=['artist_id', 'song_id', 'title', 'duration', 'year', 'artist_name', 'artist_latitude', 'artist_longitude', 'artist_location'])
    sng_result_arr = df[['artist_id', 'song_id', 'title', 'duration', 'year']].to_numpy()

    # insert song record
    song_data = sng_result_arr.tolist()
    cur.execute(song_table_insert, song_data[0])
    
    # insert artist record
    art_result_arr = df[['artist_id', 'artist_name', 'artist_latitude', 'artist_longitude', 'artist_location']].to_numpy()
    artist_data = art_result_arr.tolist()
    cur.execute(artist_table_insert, artist_data[0])


def process_log_file(cur, filepath):
    """ extracts data from file and populates the time and user dimension tables
        and the songplay fact table  """    
    
    # open log file
    dataset = pd.read_json(filepath, lines=True)
    df = pd.DataFrame(dataset)

    # filter by NextSong action
    df = df[df['page']=='NextSong']

    # convert timestamp column to datetime
    df['ts'] = pd.to_datetime(df['ts'], unit='ms')
    df['starttime'] = df['ts'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df['year'] = df['ts'].dt.year
    df['month'] = df['ts'].dt.month
    df['week'] = df['ts'].dt.isocalendar().week 
    #df['week'] = df['ts'].dt.week
    df['weekday'] = df['ts'].dt.weekday
    df['day'] = df['ts'].dt.day
    df['hour'] = df['ts'].dt.hour
    
    # insert time data records
    time_data = [df['starttime'], df['year'], df['month'], df['week'], df['weekday'], df['day'], df['hour']]
    column_labels = (['start_time', 'year', 'month', 'week', 'weekday', 'day', 'hour'])

    time_df = pd.concat(time_data, axis=1, keys=column_labels)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]
    user_df = user_df.drop_duplicates() 

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, str(row.length), row.artist))
        #print(song_select)
        #print(row.song, str(row.length), row.artist)
        
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (songid, artistid, row.sessionId, row.userId, row.level, row.location, row.starttime, row.userAgent) 
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """ reads thru directory and process data in ech file
        the func parameter is the name of function that is
        called on each file """    
    
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))

        #if i == 2:
        #    break

def main():
    """
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - process data in the files located in song_data directory.  
    
    - process data in the files located in log_data directory. 
    
    - closes the connection. 
    """
    
    #conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=postgres password=postgres")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()

if __name__ == "__main__":
    main()