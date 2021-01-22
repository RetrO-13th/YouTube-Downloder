import pytube

def downloader(link, resolution, Path):
    video = pytube.YouTube(link)
    itag = getResolution(resolution)
    fileFormat = video.streams.get_by_itag(itag)
    fileFormat.download(Path)

    return fileFormat.default_filename

def links(links, resolution, Path):
    for link in links:
        downloader(link, resolution, Path)

def getResolution(resolution):

    if resolution in ["low", "360p"]:
        itag = 18
    elif resolution in ["medium", "720p"]:
        itag = 22
    elif resolution in ["high", "1080p"]:
        itag = 137
    elif resolution in ["very high", "2160p"]:
        itag = 313
    else:
        itag = 18

    return itag

def getlinks():
    print('Enter links of videos(end with "."): ')

    links = []
    link = ''

    while link != '.':
        link = input()
        links.append(link)

    links.pop()

    return links
