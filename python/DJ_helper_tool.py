songs_db = [{
 'artist': 'Led Zeppelin', 
 'title': 'Stairways to heaven', 
 'playback': '09:20' 
}, {
 'artist': 'Metallica', 
 'title': 'Master of puppets', 
 'playback': '04:30' 
}, {
 'artist': 'Nirvana', 
 'title': 'The Man who sold the world', 
 'playback': '03:10' 
}, {
 'artist': 'Stepan Galyabarda', 
 'title': 'Lyst do mamy', 
 'playback': '02:20' 
}]

def get_song(db, len_seconds):
    time_list = []  #the playback list of songs in seconds
    k = False       #the playback of the longest song
    for i in db:
        time = sum(x*int(t) for x, t in zip([60, 1], i['playback'].split(":")))
        time_list.append(time)
    for j in sorted(time_list):
        if j > len_seconds:
            break
        k = j
    if k:
        return "Best possible song: {}/{}".format(
            db[time_list.index(k)]['artist'],
            db[time_list.index(k)]['title'])
    return k

print(get_song(songs_db, 145))
print(get_song(songs_db, 0))