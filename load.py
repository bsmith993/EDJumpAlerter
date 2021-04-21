import tkinter as tk
import logging
import l10n
import functools
import os
import sys
import requests
import json
import myNotebook as nb  # noqa: N813
from typing import Optional, Tuple, Dict, Any
from config import config, appname
from theme import theme

plugin_name = os.path.basename(os.path.dirname(__file__))
logger = logging.getLogger(f'{appname}.{plugin_name}')

def plugin_start3(plugin_dir: str) -> str:
  logger.debug('Jump Alerter started')
  return "JumpAlerter"

def plugin_stop() -> None:
  pass

def plugin_app(parent: tk.Frame) -> tk.Frame:
  global frame, targetstar_text, starclass_text, scoopable_text, visited_text, edsm_text, fd_text
  targetstar_text = tk.StringVar()
  starclass_text = tk.StringVar()
  scoopable_text = tk.StringVar()
  visited_text = tk.StringVar()
  edsm_text = tk.StringVar()
  fd_text = tk.StringVar()

  targetstar_text.set("Waiting...")
  starclass_text.set("Waiting...")
  scoopable_text.set("Waiting...")
  visited_text.set("Waiting...")
  edsm_text.set("Waiting...")
  fd_text.set("Waiting...")

  
  frame = tk.Frame(parent)

  ja_header = tk.Label(frame, text="Jump Alerter", foreground="red").grid(row=0, column=0, sticky=tk.W)

  targetstar_widget = tk.Label(frame, text="System:").grid(row=1, column=0, sticky=tk.W)
  targetstar_label = tk.Label(frame, textvariable = targetstar_text).grid(row=1, column=2, sticky=tk.W)
  
  starclass_widget = tk.Label(frame, text="Star:").grid(row=2, column=0, sticky=tk.W)
  starclass_label = tk.Label(frame, textvariable = starclass_text).grid(row=2, column=2, sticky=tk.W)

  scoopable_widget = tk.Label(frame, text="Scoopable:").grid(row=3, column=0, sticky=tk.W)
  scoopable_label = tk.Label(frame, textvariable = scoopable_text).grid(row=3, column=2, sticky=tk.W)

  visited_widget = tk.Label(frame, text="Visited:").grid(row=4, column=0, sticky=tk.W)
  visited_label = tk.Label(frame, textvariable = visited_text).grid(row=4, column=2, sticky=tk.W)

  edsm_widget = tk.Label(frame, text="EDSM:").grid(row=5, column=0, sticky=tk.W)
  edsm_label = tk.Label(frame, textvariable = edsm_text).grid(row=5, column=2, sticky=tk.W)

  fd_widget = tk.Label(frame, text="First Disc:").grid(row=6, column=0, sticky=tk.W)
  fd_label = tk.Label(frame, textvariable = fd_text).grid(row=6, column=2, sticky=tk.W)

  frame.columnconfigure(6, weight=1)
  theme.update(frame)

  return frame


def journal_entry(cmdr, is_beta, system, station, entry, state):


  if entry['event'] == "StartJump":
    targetstar_text.set("...")
    starclass_text.set("...")
    scoopable_text.set("...")
    visited_text.set("...")
    edsm_text.set("...")
    fd_text.set("...")

    cmdrs = config.get('edsm_usernames')
    idx = cmdrs.index(cmdr)
    edsmapi = config.get('edsm_apikeys')
    edsmuser = config.get('edsm_usernames')
    targetstar_text.set(entry['StarSystem'])
    sc = entry['StarClass']
    if sc.startswith("D"):
      starclass_label = tk.Label(frame, textvariable = starclass_text, foreground="red").grid(row=2, column=2, sticky=tk.W)
      starclass_text.set("CAUTION: White Dwarf!")
    elif sc.startswith("N"):
      starclass_label = tk.Label(frame, textvariable = starclass_text, foreground="blue").grid(row=2, column=2, sticky=tk.W)
      starclass_text.set("Neutron Star")
    else:
      starclass_label = tk.Label(frame, textvariable = starclass_text).grid(row=2, column=2, sticky=tk.W)
      starclass_text.set("Class " + sc + " Star")

    if entry['StarClass'] in ["F", "O", "A", "B", "G", "K", "M"]:
      scoopable_text.set("Scoopable")
    else:
      scoopable_text.set("No")

    theme.update(frame)

    targetsystem = entry['StarSystem']
    targeturl = "https://www.edsm.net/api-logs-v1/get-logs?commanderName=" + edsmuser[idx] + "&apiKey=" + edsmapi[idx] + "&systemName=" + targetsystem
    response = requests.request("GET", targeturl)
    responsej = json.loads(response.text)
    if responsej['msg'] == "System not in database":
      edsm_text.set("No")
      visited_text.set("No")
      fd_text.set("Possible first...")
    elif responsej['msg'] == "OK" and len(responsej['logs']) == 0:
      edsm_text.set("Yes")
      visited_text.set("No")
      fd_text.set("No")
    elif responsej['msg'] == "OK" and len(responsej['logs']) > 0:
      edsm_text.set("Yes")
      visited_text.set("Yes")
      fd_text.set("No")

  if entry['event'] == "Scan" and entry['DistanceFromArrivalLS'] == 0 and not entry['WasDiscovered']:
    fd_text.set("FIRST")
  elif entry['event'] == "Scan" and entry['DistanceFromArrivalLS'] == 0 and entry['WasDiscovered']:
    fd_text.set("No")
    
