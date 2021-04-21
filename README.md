# EDJumpAlerter
EDMC Plugin that provides information about an upcoming jump and system exploration data

The Jump Alerter is primarily intended for exploration to give CMDRs an ability to know more information about a system they are jumping into, especially regarding its discovery status, without having to open system maps or perform scans to get specific bits of information.

When starting a jump, the "StartJump" journal entry is recorded, indicating target system name, and star classification. Basic Info is provided inside EDMC. Some of this is duplicate to what was displayed on screen in game, but could disappear during a jump as the messages timeout. Having this information is purely convenience.

Once the systemname is populated, an EDSM call is performed against the EDSM api-logs api for the commander to determine if the system is recored at EDSM at all, and if the commander has visited that system before. The "Visited" field assumes that you have uploaded all of your journal files to EDSM. If EDSM doesn't have it, then we assume you haven't been there.

EDSM, nor journal data can give a complete picture of if a system will be a First Discovery in game or not. However, if the system is not in EDSM, then it will be listed as a possible first discovery. Once the main star is scanned, the journal will record if the system has a previous First Scanned tag already. If not, the First Disc field will inform the commander that they are currently the first to discover that system. 

Note: The First Discovered tag only indicates if no one has sold exploration data. You may see a First Discovered status, but another commander my beat you to selling the actual data and claiming the tag in game.


System:      System name of jump in progress
Star:        Star classification
Scoopable:   If star class is scoopable
Visited:     If your CMDR has visited this system before, according to EDSM.
EDSM:        If the system is already in EDSM.
First Disc:  If your CMDR is the first to scan the main star.
