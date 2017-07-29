# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Sourced From Online Templates And Guides
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Thanks To: Google And Other Websites
# Author: Unknown
#------------------------------------------------------------


import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.barnsleyfc'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')
AddonPath = addon.get_path()
fanart = os.path.join(AddonPath + "/fanart.jpg")



YOUTUBE_CHANNEL_ID_1 = "PLqqOA74PFG9io2wNlIqis5dvOq7N7CdwQ"
YOUTUBE_CHANNEL_ID_2 = "PLqqOA74PFG9hO2tIZcfgwgyYhU1go1ys2"
YOUTUBE_CHANNEL_ID_3 = "PLqqOA74PFG9jVZcXNkwskkwybvHbWwWyb"
YOUTUBE_CHANNEL_ID_4 = "PLqqOA74PFG9jmTpwLnWkwb2EIm1Uoj8ez"
YOUTUBE_CHANNEL_ID_5 = "PLqqOA74PFG9h6RXUrrff4KQnrgNTEdJhI"
YOUTUBE_CHANNEL_ID_6 = "PLqqOA74PFG9i6mIJQ-TwAn1JwmN09TBnU"
YOUTUBE_CHANNEL_ID_7 = "PLqqOA74PFG9hidktEv04rUaa0xVSCYnpm"
YOUTUBE_CHANNEL_ID_8 = "PLqqOA74PFG9hvzVsrly7Ys4vxqVbr8ZRi"
YOUTUBE_CHANNEL_ID_9 = "PLqqOA74PFG9jKCZqJ2UEDVE5rJ2xl963N"
YOUTUBE_CHANNEL_ID_10 = "PLqqOA74PFG9gf-DgmFmd_4750UFTSuyd3"
YOUTUBE_CHANNEL_ID_11 = "PLqqOA74PFG9jGT2qB0wPeXZolkhNqQQh7"
YOUTUBE_CHANNEL_ID_12 = "PLqqOA74PFG9gLq3fNlwodah34tw8f9f7r"
YOUTUBE_CHANNEL_ID_13 = "PLqqOA74PFG9hadysSQJg_bcDcAOpUCwjH"
YOUTUBE_CHANNEL_ID_14 = "PLqqOA74PFG9iHGwJ5Q_pyUxidzPulRAkS"
YOUTUBE_CHANNEL_ID_15 = "PLqqOA74PFG9gO-0LIeSIOgWxFVR7d9LWX"

# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))
	
    plugintools.add_item( 
        #action="", 
        title="[COLOR red]Barnsley FC Season 2017/18 Highlights[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="http://tyketv.barnsleyfc.info/images/season17.png",
		fanart=fanart, folder=True )	

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]Barnsley FC Season 2016/17 Highlights[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="http://tyketv.barnsleyfc.info/images/season16.png",
		fanart=fanart, folder=True )	
	
    plugintools.add_item( 
        #action="", 
        title="[COLOR red]Barnsley FC Season 2015/16 Highlights[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://tyketv.barnsleyfc.info/images/season15.png",
		fanart=fanart, folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]Barnsley FC Season 2014/15 Highlights[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://tyketv.barnsleyfc.info/images/season14.png",
        fanart=fanart, folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]Barnsley FC Season 2013/14 Highlights[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://tyketv.barnsleyfc.info/images/season13.png",
        fanart=fanart, folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="[COLOR white]JPT Trophy Winners 2016 - Road to Wembley[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://tyketv.barnsleyfc.info/images/jpt.png",
        fanart=fanart, folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="[COLOR red]Full Matches[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="http://tyketv.barnsleyfc.info/images/full.png",
        fanart=fanart, folder=True )		
		
    plugintools.add_item( 
        #action="", 
        title="[COLOR white]Season Reviews[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="http://tyketv.barnsleyfc.info/images/reviews.png",
        fanart=fanart, folder=True )
				
    plugintools.add_item( 
        #action="", 
        title="[COLOR red]Premier League Highlights[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://tyketv.barnsleyfc.info/images/prem.png",
        fanart=fanart, folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="[COLOR white]Random Extended Highlights[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="http://tyketv.barnsleyfc.info/images/ext.png",
        fanart=fanart, folder=True )		
		
    plugintools.add_item( 
        #action="", 
        title="[COLOR red]FA Cup Classics[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://tyketv.barnsleyfc.info/images/facup.png",
        fanart=fanart, folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]Memorable Games[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="http://tyketv.barnsleyfc.info/images/great.png",
        fanart=fanart, folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]Documentaries[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="http://tyketv.barnsleyfc.info/images/docu.png",
        fanart=fanart, folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="[COLOR white]Goals Goals Goals[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://tyketv.barnsleyfc.info/images/goals.png",
        fanart=fanart, folder=True )	

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]Players Videos[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="http://tyketv.barnsleyfc.info/images/players.png",
        fanart=fanart, folder=True )
		
run()
