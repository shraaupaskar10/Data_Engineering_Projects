import json
import boto3

def album(spotify_data):
    album_list=[]
    for row in spotify_data['items']:
        album_id=row['track']['album']['id']
        album_name=row['track']['album']['name']
        album_release_date=row['track']['album']['release_date']
        album_total_tracks=row['track']['album']['total_tracks']
        album_url=row['track']['album']['external_urls']['spotify']
        album_elements={'album_id':album_id, 'album_name':album_name, 'release_date':album_release_date, 'total_tracks':album_total_tracks,
                        'url':album_url}
        print(album_elements)
        album_list.append(album_elements)
    return album_list

def artist(spotify_data):
    artist_list = []
    for row in spotify_data['items']:
        for key,value in row.items():
            if key == "track":
                for artist in value['artists']:
                    artist_dict = {'artist_id' : artist['id'], 'artist_name':artist['name'], 'external_url':artist['href']}
                    artist_list.append(artist_dict)
    return artist_list

def song(spotify_data):
    song_list = []
    for row in spotify_data['items']:
        song_id = row['track']['id']
        song_name = row['track']['name']
        song_duration = row['track']['duration_ms']
        song_url = row['track']['external_urls']['spotify']
        song_popularity = row['track']['popularity']
        song_element = {'song_id':song_id, 'song_name':song_name, 'duration_ms':song_duration, 'url':song_url,
                        'popularity':song_popularity}
        song_list.append(song_element)
    return song_list
  
def lambda_handler(event, context):
    s3 = boto3.client('s3')
    Bucket ="spotify-etl-project-shraddha-092131577530-us-east-1-an"
    Key="raw_data/to_processed/"
    
    spotify_data_final = []
    spotify_key = []
    for file in s3.list_objects(Bucket=Bucket, Prefix=Key)['Contents']:
        file_key = file['Key']
        if file_key.split('.')[-1]=="json":
            responce = s3.get_object(Bucket=Bucket, Key=file_key)
            content = responce['Body']
            jsonObject= json.loads(content.read())

            spotify_data_final.append(jsonObject)
            spotify_key.append(file_key)

    for data in spotify_data_final:
        album_list = album(spotify_data)
        artist_list = artist(spotify_data)
        song_list = song(spotify_data)

        print(album_list)



    


    
