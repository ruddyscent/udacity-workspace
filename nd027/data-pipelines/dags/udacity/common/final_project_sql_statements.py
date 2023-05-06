class SqlQueries:
    # create_staging_events_table = ("""
    #     CREATE TABLE IF NOT EXISTS staging_events (
    #         artist VARCHAR(256),
    #         auth VARCHAR(256),
    #         firstName VARCHAR(256),
    #         gender VARCHAR(1),
    #         itemInSession INTEGER,
    #         lastName VARCHAR(256),
    #         length FLOAT,
    #         level VARCHAR(10),
    #         location VARCHAR(256),
    #         method VARCHAR(256),
    #         page VARCHAR(256),
    #         registration FLOAT,
    #         sessionId INTEGER,
    #         song VARCHAR(256),
    #         status INTEGER,
    #         ts BIGINT,
    #         userAgent VARCHAR(256),
    #         userId INTEGER
    #     );
    # """)

    # create_staging_songs_table = ("""
    #     CREATE TABLE IF NOT EXISTS staging_songs (
    #         num_songs INTEGER,
    #         artist_id VARCHAR(256),
    #         artist_latitude FLOAT,
    #         artist_longitude FLOAT,
    #         artist_location VARCHAR(512),
    #         artist_name VARCHAR(512),
    #         song_id VARCHAR(256),
    #         title VARCHAR(256),
    #         duration FLOAT,
    #         year INTEGER
    #     );
    # """)

    # songplay_table_create = ("""
    #     CREATE TABLE IF NOT EXISTS songplays (
    #         songplay_id VARCHAR(256),
    #         start_time TIMESTAMP,
    #         user_id INTEGER,
    #         level VARCHAR(10),
    #         song_id VARCHAR(18),
    #         artist_id VARCHAR(18),
    #         session_id INTEGER,
    #         location VARCHAR(256),
    #         user_agent VARCHAR(255)
    #     );
    # """)

    # user_table_create = ("""
    #     CREATE TABLE users (
    #         user_id INTEGER,
    #         first_name VARCHAR(256),
    #         last_name VARCHAR(256),
    #         gender CHAR(1),
    #         level VARCHAR(10)
    #     );
    # """)

    # song_table_create = ("""
    #     CREATE TABLE songs (
    #         song_id VARCHAR(256),
    #         title VARCHAR(256),
    #         artist_id VARCHAR(256),
    #         year INTEGER,
    #         duration FLOAT
    #     );
    # """)

    # artist_table_create = ("""
    #     CREATE TABLE artists (
    #         artist_id VARCHAR(256),
    #         name VARCHAR(512),
    #         location VARCHAR(512),
    #         latitude FLOAT,
    #         longitude FLOAT
    #     );
    # """)

    # time_table_create = ("""
    #     CREATE TABLE time (
    #         start_time TIMESTAMP,
    #         hour INT,
    #         day INT,
    #         week INT,
    #         month INT,
    #         year INT,
    #         weekday INT
    #     );
    # """)
    
    songplay_table_insert = ("""
        SELECT
                md5(events.sessionid|| events.start_time) songplay_id,
                events.start_time, 
                events.userid, 
                events.level, 
                songs.song_id, 
                songs.artist_id, 
                events.sessionid, 
                events.location, 
                events.useragent
                FROM (SELECT TIMESTAMP 'epoch' + ts/1000 * interval '1 second' AS start_time, *
            FROM staging_events
            WHERE page='NextSong') events
            LEFT JOIN staging_songs songs
            ON events.song = songs.title
                AND events.artist = songs.artist_name
                AND events.length = songs.duration
    """)

    user_table_insert = ("""
        SELECT distinct userid, firstname, lastname, gender, level
        FROM staging_events
        WHERE page='NextSong'
    """)

    song_table_insert = ("""
        SELECT distinct song_id, title, artist_id, year, duration
        FROM staging_songs
    """)

    artist_table_insert = ("""
        SELECT distinct artist_id, artist_name, artist_location, artist_latitude, artist_longitude
        FROM staging_songs
    """)

    time_table_insert = ("""
        SELECT start_time, extract(hour from start_time), extract(day from start_time), extract(week from start_time), 
               extract(month from start_time), extract(year from start_time), extract(dayofweek from start_time)
        FROM songplays
    """)
