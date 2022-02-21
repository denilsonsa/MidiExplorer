MIDI Explorer
=============

Yet another MIDI monitoring, debugging and manipulating tool.

![GUI](GUIwithprobedata.png)

The intent is to be [specifications](https://www.midi.org/specifications) compliant to help debugging,
reverse-engineering and developing products based on the MIDI protocol while learning everything there is to know in the
process.

Language is currently Python to help with rapid prototyping and fast iteration. It may change at any time as I see fit.


Status
------

Proof of concept!

Currently, in the prototyping phase.


Features / TODO list
--------------------

- [ ] Platform support
  - [ ] **(WIP)** Microsoft Windows
  - [ ] Apple Mac OS X
  - [ ] GNU/Linux
- [ ] MIDI protocol
  - [x] v1.x
  - [ ] v2.0
- [ ] **(WIP)** Interactive GUI
  - [ ] Icons
  - [ ] About window
  - [X] Node editor window
    - [X] Inputs
    - [X] Outputs
    - [x] Modules
  - [ ] **(WIP)** Probe data window
  - [ ] **(WIP)** Generator data window
  - [x] Log window
  - [ ] Actions
    - [x] Toggle fullscreen (F11)
    - [x] Toggle log (F12)
    - [ ] **(WIP)** Save state (Buggy at the moment)
- [ ] I/O management
  - [ ] List MIDI I/O
    - [x] USB / IEEE-1394 (OS level)
    - [ ] Bluetooth Low Energy (BLE-MIDI)
    - [ ] RTP-MIDI / IETF RFC 6295
    - [ ] Virtual
  - [X] Effective connections
  - [ ] Refresh
    - [X] Manual
    - [ ] Auto with reconnect
  - [ ] Add/Remove
  - [ ] Virtual ports
  - [ ] Save state
- [ ] Modules (Plugins?)
  - [ ] Instances management (Add/Remove)
  - [x] Virtual Debug Probe
    - [x] Read raw input
    - [x] Table decode input
    - [x] Thru support
  - [ ] Generator
    - [ ] Generate raw output
    - [ ] Buffer/Clipboard any message (raw or decoded) to output
  - [ ] Translator/Filter
  - [ ] Hardware toolbox
- [ ] **(WIP)** Logging
  - [x] GUI
  - [ ] To file
    - [ ] Overwrite
    - [ ] Append

Legal notice
------------

### License

Copyright 2022 Raphaël Doursenaud

This software is released under the terms of the GNU General Public License, version 3.0 or later (GPL-3.0-or-later).

See [LICENSE](LICENSE).

### Dependencies & License Acknowledgment

- [Python](https://python.org) v3.10  
  Used under the terms of the PSF License Agreement.
- [RtMidi](https://github.com/thestk/rtmidi)  
  Copyright (c) 2003-2021 Gary P. Scavone  
  Used under the terms of the MIT License.
- via [python-rtmidi](https://github.com/SpotlightKid/python-rtmidi)  
  Copyright (c) 2012 - 2021 Christopher Arndt  
  Used under the terms of the MIT License.
- via [mido](https://github.com/mido/mido)  
  Copyright (c) 2013-infinity Ole Martin Bjørndalen    
  Used under the terms of the MIT License.
- [Dear ImGui](https://github.com/ocornut/imgui)  
  Copyright (c) 2014-2022 Omar Cornut  
  Used under the terms of the MIT License.
- via [Dear PyGui](https://github.com/hoffstadt/DearPyGui)  
  Copyright (c) 2021 Dear PyGui, LLC  
  Used under the terms of the MIT License.

### Trademarks

[MIDI](https://midi.org) is a trademark of the MIDI Manufacturers Association (MMA) in the United States of America.

This is not a registered trademark in the European Union and France where I reside.

#### Other

Other trademarks are property of their respective owners and used fairly for descriptive and nominative purposes only.