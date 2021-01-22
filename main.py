# Downloading copyrighted videos from YouTube is illegal!!
# Not responsible for downloads! it's just for learning. 
# RetrO_13th (Sadra Gholami)

import pytube
import Downloader


links = Downloader.getlinks()
Path = input('Enter downloaded videos path: ')
quality = input('choose your quality(low, medium, high, very high or resolution): ')

for link in links:
    try:
        print('Downloading...')
        Downloader.downloader(link, quality, Path)  
    except:
        print('Invalid links or connection lost!')