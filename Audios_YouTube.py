import pafy


url = ''
video = pafy.new(url)

audiostreams = video.audiostreams
for i in audiostreams:
	print(i.bitrate, i.extension, i.get_filesize())

audiostreams[3].download()


# To download best audio
'''
bestaudio = video.getbestaudio()
bestaudio.download()
'''