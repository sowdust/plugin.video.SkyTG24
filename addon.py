import re
import xbmcgui
import requests

url = 'http://videoplatform.sky.it/player/json/get_livestream_1.json'
res = requests.get(url)

try:
	streaming_url = 'https://' + re.findall('"streaming_url":"https{0,1}://(.*?)"', res.text)[0]
	thumb_url = 'https://' + re.findall('"img":"https{0,1}://(.*?)"', res.text)[1]
	listitem = xbmcgui.ListItem('SkyTG24')
	listitem.setInfo('video', {'Title': 'Diretta SkyTG24'})
	listitem.setArt({ 'thumb': thumb_url})
	xbmc.Player().play(streaming_url, listitem)

except Exception as ex:
	message = 'Eccezione: %s' % ex
	listitem = xbmcgui.ListItem('SkyTG24 - Errore')
	listitem.setInfo('video', {'Title': 'Errore nell\' avvio del plugin SkyTG24'})
	listitem.setInfo('video', { 'plot': message })
