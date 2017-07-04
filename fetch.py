from subprocess import call
import os
import sys

def stripEndAmps(url):
    print "To Strip : " + url
    ind = url.find("&")
    finalUrl = url[:ind]
    print "Striped : " + finalUrl
    return finalUrl


def download(songURLFile):
    with open(songURLFile) as f:
        for line in f:
            if len(line.strip()) != 0: # avoiding newlines      
                url = stripEndAmps(line) 
                print "\t-- Downloading -- "
                print url
                sys.stdout.flush()
                call(["D:\\Youtube-DL\\youtube-dl.exe", 
                      "--extract-audio", 
                      "--audio-format", 
                      "mp3", 
                      url])
                print "\t-- Done -- \n"
                sys.stdout.flush()
            sys.stdout.flush()
    sys.stdout.flush()

def setup():
    print "Downloading songs now..."
    songURLFile = "D:\\Youtube-DL\\SongURL.txt"
    musicLocation = "C:\\Users\\sumit\\Google Drive\\Music\\000_latest"
    os.chdir(musicLocation)
    sys.stdout.flush()
    download(songURLFile)
    # clear the file now
    print "-- Trying to clear the contents of the URL file -- "
    open(songURLFile, 'w').close()
    print "-- All contents cleared -- "
    print "-- All downloads complete at: " + musicLocation + " -- "
    print "!!!! ********* ENJOY ********* !!!!"

setup()
