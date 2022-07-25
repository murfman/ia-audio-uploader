import glob
import csv
from internetarchive import upload
from tinytag import TinyTag


# Variables that may need to be changed.
folderPath = '/run/media/brian/Backups/MUP/upload-test/'
fileExt = '.mp3'
creator1 = 'Miskatonic University Podcast Faculty'
collection = 'opensource_audio'


def remove(string):
    return string.replace(" ", "")

def get_metadata(audiofile):
    tag = TinyTag.get(audiofile)
    meta_title = tag.title
    meta_artist = tag.artist
    meta_genre = tag.genre
    meta_track = tag.track
    meta_comment = tag.comment
    meta_duration = tag.duration
    metalicense = 'http://creativecommons.org/licenses/by-nc-sa/4.0/'
    md = {'collection': collection, 'title': meta_title, 'creator': creator1, 'mediatype': 'audio', 'genre': meta_genre, 'length': meta_duration, 'track': meta_track, 'description': meta_comment, 'licenseurl': metalicense}
    bad_chars = [';', ':', '!', "*", " ", "'", "&", ",", "(", ")"]
    meta_id = ''.join(i for i in meta_title if not i in bad_chars)
    r = upload(meta_id, files={audiofile: audiofile}, metadata=md)
    print(meta_id + ' is done uploading.')

                                                                                                                                                                                                                                              
for i in glob.glob(folderPath + '*' + fileExt, recursive=True):                                                                                                                                                                               
    print(i)                                                                                                                                                                                                                                  
    get_metadata(i)                                                                                                                                                                                                                           
