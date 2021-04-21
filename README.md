# EDJumpAlerter
EDMC Plugin that provides information about an upcoming jump and system exploration data.

The Jump Alerter is primarily intended for exploration to give CMDRs an ability to know more information about a system they are jumping into, especially regarding its discovery status, without having to open system maps or perform scans to get specific bits of information.
If you are the type of commander that is purely looking for new, first discovery systems, or at least doesn't want to hit the system map to know if someone else has been there, this plugin will hopefully shave a few seconds off your system jumps.

# Installation
Just a standard EDMC plugin installation. Extract folder within zip file into your EDMC plugins folder and start EDMC. You should have a new section in the main window with "Jump Alerter" and 6 rows of data.

# Configuration
EDSM Plugin CMDR and API configuration: This plugin uses EDSM api calls, and more specifically uses the api-logs call which requires an EDSM API key to be configured. Rather than configuring another config page, this plugin pulls from the builtin EDSM plugin configuration to collect CMDR name and API for EDSM calls. If you do not have the EDSM plugin page configured and working properly, this will not work.

# Process
When starting a jump, (After the warm up, when the countdown starts) the "StartJump" journal entry is recorded, indicating target system name, and star classification. Basic Info is provided inside the EDMC main window to give you a preview of what you are jumping to. Some of this is duplicate to what was displayed on screen in game, but that information could disappear during a jump as the messages timeout. Having this information is purely convenience. (ie... "Wait, did that say White Dwarf??")

Once the system name is collected, an EDSM call is performed against the EDSM api-logs api for your commander to determine if the system is recored at EDSM at all, and if your commander has visited that system before. This is all according to EDSM only! The "Visited" field assumes that you have uploaded all of your journal files to EDSM. If EDSM doesn't have it, then we assume you haven't been there.

EDSM, nor journal data can give a complete picture of if a system will be a First Discovery in game or not. However, if the system is not in EDSM, then during your jump it will be listed as a "possible" first discovery. Once the main star is scanned, the journal will record if the system has a previous First Scanned tag already. If not, the First Disc field will inform the commander that they are currently the first to discover that system. 

NOTE: The First Discovered tag only indicates if no one has sold exploration data. You may see a First Discovered status, but another commander my beat you to selling the actual data and claiming the tag in game.

# Display Details

System:      System name of jump in progress
Star:        Star classification
Scoopable:   If star class is scoopable
Visited:     If your CMDR has visited this system before, according to EDSM.
EDSM:        If the system is already in EDSM.
First Disc:  If your CMDR is the first to scan the main star.
