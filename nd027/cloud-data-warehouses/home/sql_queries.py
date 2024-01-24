import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES
staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
staging_events_table_create = ("""CREATE TABLE IF NOT EXISTS staging_events (
    artist VARCHAR,
    auth VARCHAR,
    firstName VARCHAR,
    gender VARCHAR,
    itemInSession INT,
    lastName VARCHAR,
    length FLOAT,
    level VARCHAR,
    location VARCHAR,
    method VARCHAR,
    page VARCHAR,
    registration FLOAT,
    sessionId INT sortkey,
    song VARCHAR,
    status INT,
    ts BIGINT,
    userAgent VARCHAR,
    userId INT distkey
    )
""")

staging_songs_table_create = ("""CREATE TABLE IF NOT EXISTS staging_songs (
    num_songs INT,
    artist_id VARCHAR,
    artist_latitude FLOAT,
    artist_longitude FLOAT,
    artist_location VARCHAR,
    artist_name VARCHAR distkey,
    song_id VARCHARy,
    title VARCHAR,
    duration FLOAT,
    year INT sortkey
    )
""")

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (
    songplay_id INT IDENTITY(0,1) PRIMARY KEY,
    start_time TIMESTAMP NOT NULL sortkey,
    user_id INT NOT NULL,
    level VARCHAR,
    song_id VARCHAR,
    artist_id VARCHAR,
    session_id INT distkey,
    location VARCHAR,
    user_agent VARCHAR
    )
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY distkey,
    first_name VARCHAR,
    last_name VARCHAR,
    gender VARCHAR,
    level VARCHAR
    )
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR PRIMARY KEY distkey,
    title VARCHAR,
    artist_id VARCHAR,
    year INT,
    duration FLOAT
    )
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR PRIMARY KEY distkey,
    name VARCHAR,
    location VARCHAR,
    latitude FLOAT,
    longitude FLOAT
    )
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
    start_time TIMESTAMP PRIMARY KEY sortkey distkey,
    hour INT,
    day INT,
    week INT,
    month INT,
    year INT,
    weekday INT
    )
""")

# STAGING TABLES
staging_events_copy = ("""COPY staging_events FROM '{}'
CREDENTIALS 'aws_iam_role={}'
JSON '{}' REGION 'us-west-2';
""").format(config['S3']['LOG_DATA'], config['IAM_ROLE']['ARN'], 
    config['S3']['LOG_JSONPATH'])

staging_songs_copy = ("""COPY staging_songs FROM '{}'
CREDENTIALS 'aws_iam_role={}'
JSON 'auto' REGION 'us-west-2';
""").format(config['S3']['SONG_DATA'], config['IAM_ROLE']['ARN'])

# FINAL TABLES
songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, 
    session_id, location, user_agent)
SELECT  
    TIMESTAMP 'epoch' + ts / 1000 * INTERVAL '1 second', 
    userId, 
    level, 
    song_id, 
    artist_id, 
    sessionId, 
    location, 
    userAgent
FROM staging_events
LEFT JOIN staging_songs ON (staging_events.artist = staging_songs.artist_name) 
    AND (staging_events.song = staging_songs.title)
WHERE staging_events.page = 'NextSong'
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
SELECT DISTINCT userId, firstName, lastName, gender, level
FROM staging_events
WHERE userId IS NOT NULL AND page = 'NextSong'
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
SELECT DISTINCT song_id, title, artist_id, year, duration
FROM staging_songs
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude)
SELECT DISTINCT 
    artist_id, artist_name, artist_location, artist_latitude, artist_longitude
FROM staging_songs
""")

time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
WITH temp_time AS (SELECT TIMESTAMP 'epoch' 
    + (ts / 1000 * INTERVAL '1 second') AS ts, page FROM staging_events)
SELECT DISTINCT 
    ts, 
    EXTRACT(hour FROM ts), 
    EXTRACT(day FROM ts), 
    EXTRACT(week FROM ts), 
    EXTRACT(month FROM ts), 
    EXTRACT(year FROM ts), 
    EXTRACT(weekday FROM ts) 
FROM temp_time
WHERE page = 'NextSong'
""")

# VALIDATE TABLES
count_staging_events = ("""SELECT COUNT(*) FROM staging_events""")
count_staging_songs = ("""SELECT COUNT(*) FROM staging_songs""")
count_songplays = ("""SELECT COUNT(*) FROM songplays""")
count_users = ("""SELECT COUNT(*) FROM users""")
count_songs = ("""SELECT COUNT(*) FROM songs""")
count_artists = ("""SELECT COUNT(*) FROM artists""")
count_time = ("""SELECT COUNT(*) FROM time""")

# QUERY LISTS
create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
validate_table_queries = [count_staging_events, count_staging_songs, count_songplays, count_users, count_songs, count_artists, count_time]
