# -*- coding: utf-8 -*-
import os, urllib, xbmc, zipfile, xbmcgui
import time

dialog = xbmcgui.Dialog()

def ExtractAll(_in, _out):
	try:
		zin = zipfile.ZipFile(_in, 'r')
		zin.extractall(_out)
	except Exception, e:
		print str(e)
		return False

	return True

def updatwalls():

    time.sleep(5)	
    xbmc.executebuiltin('UpdateLibrary(video)')
    time.sleep(180)	
    xbmc.executebuiltin('UpdateLibrary(video)')	
	
def wallupdate():
		
	url = "https://github.com/kobiko3030/kodi-senyor/blob/master/senyorwall/userdata.zip?raw=true"
	addonsDir = xbmc.translatePath(os.path.join('special://home')).decode("utf-8")
	packageFile = os.path.join(addonsDir,'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass	

	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos") 
	#updatwalls()
	
	
