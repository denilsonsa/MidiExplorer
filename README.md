[![MIDI Explorer Logo](https://raw.githubusercontent.com/EMATech/midiexplorer/main/data/assets/midiexplorer_logo.svg) MIDI Explorer](https://github.com/EMATech/midiexplorer)
=============================================================================================================================================================================

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/midiexplorer.svg)](https://pypi.org/project/midiexplorer)

[![Downloads](https://pepy.tech/badge/midiexplorer)](https://pepy.tech/project/midiexplorer)
[![PyPI - Version](https://img.shields.io/pypi/v/midiexplorer.svg)](https://pypi.org/project/midiexplorer)

Yet another MIDI monitor, analyzer, debugger and manipulation tool.

![GUI](https://raw.githubusercontent.com/EMATech/midiexplorer/main/data/screenshots/GUIwithgenerator.png)

The intent is to be [specifications](https://www.midi.org/specifications) compliant to help debugging,
reverse-engineering and developing products based on the MIDI protocol while learning everything there is to know in the
process.

The reference specifications used ard linked below and comes from the following standards bodies:

- [MIDI Association, ex MIDI Manufacturers Association (MMA)](https://wwwmidi.org) USA
- [Association of Musical Electronics Industry (AMEI)](https://www.amei.or.jp/) Japan
- [MIDI Standards Committee (MSC)](http://amei.or.jp/midistandardcommittee) Japan

There is two specification supplement types:

- Recommended Practices (RP) 001-054
- Confirmation of Approval for MIDI Standard (CA) 018-035

A nice [history list is provided by the MSC](http://amei.or.jp/midistandardcommittee/RP&CAj.html) [JP].  
I have made a translated and slightly updated
[Google Sheet](https://docs.google.com/spreadsheets/d/1bgeT7qCjVVMnmZvUY374y7f_tJt86wU_SkyOtL5ka3A/edit?usp=sharing)
for easier browsing.

Language is currently Python to help with rapid prototyping and fast iteration. It may change at any time as I see fit.

**Table of Contents**

- [Status](#status)
- [Installation](#installation)
- [Features / TODO list](#features--todo-list)
- [Prior art](#prior-art)
- [Legal notice](#legal-notice)
    - [License](#license)
    - [Dependencies & License Acknowledgment](#dependencies--license-acknowledgment)
    - [Trademarks](#trademarks)

Status
------

Basic features implemented.

First alpha released!

Testers welcome ;)


Installation
------------

### Install Python 3.10

From [python.org](https://www.python.org/downloads/windows/) (*recommended*) or your favorite package manager.

### Install PipX

Follow the instructions for your operating system.

#### Microsoft Windows

In a terminal

```console
py -m pip install --user pipx
py -m pipx ensurepath
```

*Close and reopen your terminal.*

#### Mac OS X / Linux

```console
python3 -m pip install --user pipx
```

### Install MIDI Explorer

```console
pipx install midiexplorer
```

Features / TODO list
--------------------

- [ ] Platform support
    - [ ] **(WIP)** Microsoft Windows
        - [x] WinMM aka [Windows Multimedia MME API](https://docs.microsoft.com/fr-fr/windows/win32/api/mmeapi/)
            - via mido's RtMidi backend
        - [ ] WinRt aka [UWP Windows Runtime API](https://docs.microsoft.com/en-us/uwp/api/windows.devices.midi)
            - [RtMidi related  issue](https://github.com/thestk/rtmidi/issues/145)
    - [ ] **(WIP)** Apple Mac OS X
        - [x] Core MIDI
            - via mido's RtMidi backend
        - [ ] [JACK MIDI](https://jackaudio.org/api/group__MIDIAPI.html) (Should work but untested ATM)
    - [ ] **(WIP)** GNU/Linux
        - [ ] **(WIP)** ALSA
            - [x] [Sequencer API](https://www.alsa-project.org/alsa-doc/alsa-lib/seq.html)
                - via mido's RtMidi backend
            - [ ] [RawMidi API](https://www.alsa-project.org/alsa-doc/alsa-lib/rawmidi.html)
        - [ ] [JACK MIDI](https://jackaudio.org/api/group__MIDIAPI.html) (Should work but untested ATM)
        - [ ] OSS?
- [ ] Documentation
    - [ ] Developers
        - [X] Comments
        - [x] Docstrings ([PEP257](https://peps.python.org/pep-0257))
        - [x] Type Hinting ([PEP484](https://peps.python.org/pep-0484))
    - [ ] Users
        - [ ] [Sphinx](https://www.sphinx-doc.org)
            - [ ] [autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
            - [ ] [Read The Docs](https://readthedocs.org)
- [ ] Linting
    - [ ] Code style checks? ([PEP8](https://peps.python.org/pep-0008) pycodestyle)
    - [ ] Docstrings? (darglint)
    - [ ] Typechecking? (mypy)
- [ ] Unit tests? (pytest)
    - [ ] Coverage
- [ ] [Packaging](https://packaging.python.org)
    - [ ] **(WIP)** [PyPi](https://pypi.org)
        - [x] Using [Hatch](https://hatch.pypa.io)
    - [ ] [PyInstaller](https://pyinstaller.org)
- [ ] Continuous Integration? (GitHub Actions workflow)
- [ ] MIDI protocols
    - [x] **(WIP)**
      [v1.0  
      includes RP-001/RP-002/RP-003/RP-004/RP-005/RP-006/RP-007/RP-008/RP-009/RP-010/RP-011/RP-012/RP-013/RP-014](https://www.midi.org/specifications/midi1-specifications)
      (1983 - February 1996)
        - using a [modified mido](https://github.com/mido/mido/pull/370)
    - [ ] [v2.0](https://www.midi.org/specifications/midi-2-0-specifications)
- [ ] **(WIP)** Interactive GUI
    - [x] Icons
    - [x] About window
    - [x] Fonts
    - [ ] Custom theme
    - [X] Node editor window
        - [X] Inputs
        - [X] Outputs
        - [x] Modules
    - [x] Monitor data window
    - [x] Generator data window
    - [x] Log window
    - [ ] **(WIP)** Actions
        - [x] Toggle full-screen (F11)
        - [x] Toggle log (F12)
        - [ ] Save state (Buggy at the moment)
- [ ] **(WIP)** I/O management
    - [ ] Select backend?
    - [ ] **(WIP)** List MIDI I/O
        - [x] [USB MIDI 1.0](https://www.midi.org/specifications/midi-transports-specifications/usb/usb-midi-1-0-2)
            - [x] OS Level
            - [ ] Direct Access?
        - [ ] [USB MIDI 2.0](https://www.midi.org/specifications/midi-transports-specifications/usb/usb-midi-2-0-2)
            - [ ] OS Level?
            - [ ] Direct Access?
        - [ ] IEEE-1394  
          [RP-027 (MMA)](https://www.midi.org/specifications/midi-transports-specifications/midi-transport-specification-for-ieee-1394-firewire-2)
          MIDI Media Adaptation Layer for IEEE-1394 v1.0  
          [RP-027 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/RP27v10spec.pdf)
          MIDI Media Adaptation Layer for IEEE-1394 v1.0
            - [ ] OS Level?
            - [ ] Direct Access?
        - [ ] Bluetooth Low Energy (BLE-MIDI)  
          [RP-052 (MMA)](https://www.midi.org/specifications/midi-transports-specifications/midi-over-bluetooth-low-energy-ble-midi)
          Specification for MIDI over Bluetooth Low Energy (BLE-MIDI) v1.0  
          [RP-052 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp52spec(ble-midi).pdf)
          Specification for MIDI over Bluetooth Low Energy (BLE-MIDI) v1.0
            - [ ] OS Level
                - Requires [WinRt MIDI](https://docs.microsoft.com/en-us/windows/uwp/audio-video-camera/midi) for
                  Microsoft Windows
            - [ ] Direct Access?
        - [ ] RTP-MIDI  
          [RTP Payload Format for MIDI (MMA)](https://www.midi.org/specifications/midi-transports-specifications/rtp-midi)  
          [IETF RFC 6295](https://www.rfc-editor.org/rfc/rfc6295.txt)
          RTP Payload Format for MIDI
            - [ ] OS Level
                - Requires [rtpMIDI](https://www.tobias-erichsen.de/software/rtpmidi.html) for Microsoft Windows
            - [ ] Direct Access?
        - [ ] Virtual
            - [ ] OS Level
                - Requires [loopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html) for Microsoft Windows
            - [ ] Native
                - Provided by RtMidi for Linux & Apple Mac OS X
        - [ ] Custom Hardware
            - [ ] 5-Pin DIN  
              [CA-033 (MMA)](https://www.midi.org/specifications/midi-transports-specifications/5-pin-din-electrical-specs)
              MIDI 1.0 Electrical Specification Update [2014]  
              [CA-033 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/ca33.pdf)
              MIDI 1.0 Electrical Specification Update [2014]
            - [ ] 2.5mm TRS Jack  
              [RP-054 (MMA)](https://www.midi.org/specifications/midi-transports-specifications/specification-for-use-of-trs-connectors-with-midi-devices-2)
              Specification for use of TRS Connectors with MIDI Devices  
              [RP-054 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp054.pdf)
              Specification for use of TRS Connectors with MIDI Devices
            - [ ] Mobile Musical Interface  
              [RP-048/amd1 (MMA)](https://www.midi.org/specifications/file-format-specifications/mobile-midi/mobile-musical-instrument-specification)
              Mobile Musical Interface Specification v1.0.6  
              [RP-048/Amd1 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp48amd1.pdf)
              Mobile Musical Instrument Specification v1.1 / Mobile Musical Interface Specification v1.0.6  
              [RP-048 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp48a(spec).pdf)
              Mobile Musical Interface Specification v1.0.2
    - [x] Input reading modes
        - [x] Polling
        - [x] Callback
    - [ ] Sort by ID/Name
    - [ ] **(WIP)** Connections
        - [x] Port to probe
        - [x] Probe to port
        - [x] Port to port
        - [ ] Port to any module
        - [ ] Any module to port
        - [ ] Module to module
    - [ ] **(WIP)** Refresh
        - [X] Manual
        - [ ] Auto with reconnect
    - [ ] Virtual ports
        - [ ] Add/Remove
    - [ ] Save state
- [x] Timing
    - [x] Hardware
        - retrieved using a modified mido RtMidi backend
    - [x] System
        - computed using the local clock
- [ ] History view (Table decode)
    - [x] Input
    - [x] Output
    - [x] Selection decodes to monitor
    - [ ] Selection prepares generator
- [ ] **(WIP)** Modules (Plugins?)
    - [ ] Instances management (Add/Remove)
    - [x] Virtual Debug Probe
        - [x] Activity monitor
            - [x] Settings
                - [x] Colors
                    - [x] Live
                    - [x] Selected
                - [x] Persistence
                - [x] Note-On with velocity set to 0 is Note-Off (Per specification)
                - [x] Display EOX as either a System Common or a System Exclusive message
                - [x] Notation
                    - [x] English Alphabetical
                    - [x] Syllabic
                    - [x] German Alphabetical
            - [ ] Stateless
                - [x] Message type
                    - [x] Channel
                    - [x] System
                - [x] Channel
                - [x] Controllers
                    - [ ] Data Increment / Decrement  
                      [RP-018 (MMA)](https://www.midi.org/specifications/midi1-specifications/midi-1-addenda/response-to-data-increment-decrement-controllers)
                      Response to Data Inc/Dec Controllers  
                      [RP-018 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp18.pdf)
                      Response to Data Increment/Decrement Controller
                    - [ ] Sound Controller Defaults  
                      [RP-021 (MMA)](https://www.midi.org/specifications/midi1-specifications/midi-1-addenda/sound-controller-defaults-revised)
                      Sound Controller Defaults (Revised)  
                      [RP-021 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp21.pdf)
                      Defaults for Sound Controllers
                    - [x] Redefinition of CC91 and CC93   
                      [RP-023 (MMA)](https://www.midi.org/specifications/midi1-specifications/midi-1-addenda/renaming-of-cc91-and-cc93)
                      Renaming of CC91 and CC93  
                      [RP-023 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp23.pdf)
                      Redefinition of CC91 and CC93
                    - [ ] Registered Parameter Numbers (RPN)
                        - [x] 00 Pitch Bend Sensitivity
                        - [x] 01 Fine Tuning
                        - [x] 02 Coarse Tuning
                            - [x] Redefinition of RPN 01/02  
                              [RP-022 (MMA)](https://www.midi.org/specifications/midi1-specifications/midi-1-addenda/redefinition-of-rpn01-and-rpn02-channel-fine-coarse-tuning)
                              Redefinition of RPN 01/02  
                              [RP-022 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp22.pdf)
                              Channel Fine/Coarse Tuning
                        - [x] 03 Tuning Program Select
                        - [x] 04 Tuning Bank Select
                        - [x] 05 GM2 Modulation Depth Range  
                          [CA-026 (MMA)](https://www.midi.org/specifications/midi1-specifications/general-midi-specifications/general-midi-2/modulation-depth-range-rpn)
                          Modulation Depth Range RPN  
                          [CA-026 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/ca26.pdf)
                          Modulation Depth Range RPN
                        - [ ] 06 MIDI Polyphonic Expression v1.1 (MPE)  
                          [RP-053/CA-034/M1-100-UM](https://www.midi.org/specifications/midi1-specifications/mpe-midi-polyphonic-expression)
                          MIDI Polyphonic Expression v1.1  
                          [CA-034 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/ca034.pdf)
                          MPE Configuration RPN
                        - [ ] …
                        - [ ] 61 (0x3D) Three Dimensional Sound Controller  
                          [RP-049 (MMA)](https://www.midi.org/specifications/midi1-specifications/midi-1-addenda/three-dimensional-sound-controllers)
                          Three Dimensional Sound Controllers  
                          [RP-049 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp49.pdf)
                          Three Dimensional Sound Controllers
                    - [ ] Non Registered Parameter Numbers (NRPN)
                    - [x] High Resolution Velocity Prefix  
                      [CA-031 (MMA)](https://www.midi.org/specifications/midi1-specifications/midi-1-addenda/high-resolution-velocity-prefix)
                      CC #88 High Resolution Velocity Prefix  
                      [CA-031 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/ca-31.pdf)
                      CC#88 High Resolution Velocity Prefix
                - [ ] **(WIP)** Notes
                    - [x] Keyboard
                    - [ ] Staff
            - [ ] Stateful
                - [ ] Program Changes, Bank Select & Patches
                    - [ ] [General MIDI System (MMA)](https://www.midi.org/specifications/midi1-specifications/general-midi-specifications)
                      (GM)
                        - [ ] Level 1 (GM1/GM-1) (1991)  
                          [MMA0007/RP-003](https://www.midi.org/specifications/midi1-specifications/general-midi-specifications/general-midi-1)
                          General MIDI System Level 1  
                          [RP-015 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp15.pdf)
                          Response to Reset All Controllers
                        - [ ] Level 2 (GM2/GM-2) (1999)  
                          [RP-024/RP-036/RP-037/RP-045 (MMA)](https://www.midi.org/specifications/midi1-specifications/general-midi-specifications/general-midi-2/general-midi-level-2)
                          General MIDI 2 v1.2a  
                          [RP-024 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp24(e).pdf)
                          General MIDI Level 2 Recommended Practice  
                          RP-024 [General MIDI 2 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/GM2-v12a.pdf)
                          v1.2a  
                          [RP-036 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp36.pdf)
                          Default Pan Curve  
                          [RP-037 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp37.pdf)
                          GM2 MIDI Tuning Amendment
                        - [ ] Lite (GML) (2001)  
                          [RP-033 (MMA)](https://www.midi.org/specifications/midi1-specifications/general-midi-specifications/general-midi-lite/general-midi-lite-2)
                          General MIDI Lite v1.0  
                          [RP-033 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/gml-v1.pdf)
                          General MIDI Lite v1.0
                    - [ ] Proprietary
                        - [ ] Roland
                            - [ ] Linear Arithmetic (LA) (MT-32…) (1987)
                            - [ ] General Standard (GS) (Sound Canvas…) (1991)
                        - [ ] Yamaha
                            - [ ] E**X**tended **G**eneral MIDI (XG)
                                - [ ] Level 1 (1994)
                                - [ ] Level 2 (1997)
                                - [ ] Level 3 (1998)
                                - [ ] Lite (2002)
                - [ ] **(WIP)** System Exclusive (SysEx)
                    - [x] Basic decoding
                        - [x] (Manufacturer) ID
                        - [x] Device ID
                        - [x] Raw payload
                    - [ ] **(WIP)** Universal System Exclusive
                        - [x] Sub-IDs type decoding
                        - [ ] Payloads decoding
                            - [ ] MIDI Show Control (MSC)  
                              [RP-002/RP-014 (MMA)](https://www.midi.org/specifications/midi1-specifications/midi-show-control-2)
                              MIDI Show Control 1.1.1
                            - [ ] MIDI Time Code (MTC)  
                              [MMA0001/RP-004/RP-008 (MMA)](https://www.midi.org/specifications/midi1-specifications/midi-time-code)
                              MIDI Time Code v4.2.1
                            - [ ] Notation information  
                              [RP-005/RP-006]()
                            - [ ] File dump  
                              [RP-009]()
                            - [ ] MIDI tuning  
                              [RP-012]()
                            - [ ] MIDI Machine Control (MMC)  
                              [MMA-0016/RP-013 (MMA)](https://www.midi.org/specifications/midi1-specifications/rp-013-v1-0-midi-machine-control-specification-96-1-4)
                              MIDI Machine Control 1.0
                            - [ ] File Reference System Exclusive Message  
                              [CA-018 (MMA)](https://www.midi.org/specifications/midi1-specifications/midi-1-addenda/file-reference-sysex-message)
                              File Reference System Exclusive Message  
                              [CA-018 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/ca18.pdf)
                              File Reference System Exclusive Message
                            - [ ] Sample Dump Size, Rate and Name Extensions  
                              [CA-019 (MMA)](https://www.midi.org/specifications/midi1-specifications/midi-1-addenda/sample-dump-size-rate-name-extensions)
                              Sample Dump Size, Rate and Name Extensions  
                              [CA-019 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/ca19.pdf)
                              Sample Dump Size, Rate and Name Extensions
                            - [ ] GM2 Midi Tuning Messages  
                              [CA-020/CA-021/RP-020 (MMA)](https://www.midi.org/specifications/midi1-specifications/general-midi-specifications/general-midi-2/midi-tuning-updated)
                              MIDI Tuning Messages  
                              [CA-020 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/ca20.pdf)
                              MIDI Tuning Bank and Dump Extensions  
                              [CA-021 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/ca21.pdf)
                              Scale/Octave Tuning  
                              [CA-021/Amd1 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/ca21_amd1.pdf)
                              Amendment to Scale/Octave Tuning  
                              [RP-020 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp20.pdf)
                            - [ ] GM2 Controller Destination Setting  
                              [CA-022 (MMA)](https://www.midi.org/specifications/midi1-specifications/general-midi-specifications/general-midi-2/controller-destination-setting)
                              Controller Destination Setting  
                              [CA-022 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/ca22.pdf)
                              Controller Destination Setting
                            - [ ] GM2 Key-Based Instrument Controllers  
                              [CA-023 (MMA)](https://www.midi.org/specifications/midi1-specifications/general-midi-specifications/general-midi-2/key-based-instrument-controllers)
                              Key-Based Instrument Controllers  
                              [CA-023 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/ca23.pdf)
                              Key-Based Instrument Controllers
                            - [ ] GM2 Global Parameter Control  
                              [CA-024 (MMA)](https://www.midi.org/specifications/midi1-specifications/general-midi-specifications/general-midi-2/global-parameter-control)
                              Global Parameter Control  
                              [CA-024 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/ca24.pdf)
                              Global Parameter Control
                            - [ ] GM2 Master Fine & Coarse Tuning  
                              [CA-025 (MMA)](https://www.midi.org/specifications/midi1-specifications/general-midi-specifications/general-midi-2/master-fine-course-tuning)
                              Master Fine/Coarse Tuning  
                              [CA-025 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/ca25.pdf)
                              Master Fine/Coarse Tuning
                            - [ ] GM2 System Level 2 Message  
                              [CA-027 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/ca27.pdf)
                              General MIDI Level 2 Universal System Exclusive Message
                            - [ ] Extension 00-01 to File Reference SysEx Message  
                              [CA-028 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/ca28.pdf)
                              Extension 00-01 to File Reference Sysex Message
                            - [ ] GM-Lite Scalable Polyphony MIDI Specification (SP-MIDI)  
                              [RP-034/RP-035 (MMA)](https://www.midi.org/specifications/file-format-specifications/mobile-midi/scalable-polyphony-midi-sp-midi-2)
                              Scalable Polyphony MIDI Specification and Device Profiles v1.0b  
                              [RP-034/RP-035 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/sp-midi_all_v1a.pdf)
                              Scalable Polyphony MIDI Specification and Device Profiles v1.0a
                            - [ ] GM-Lite Maximum Instantaneous Polyphony (MIP)  
                              [CA-029 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/spmidi-ca29.pdf)
                              Maximum Instantaneous Polyphony (MIP)
                            - [ ] Mobile Phone Control Message  
                              [RP-046 (MMA)](https://www.midi.org/specifications/file-format-specifications/mobile-midi/mobile-phone-control-message)
                              Mobile Phone Control Message  
                              [CA-030 (MMA)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/ca-30.pdf)
                              Mobile Phone Control Universal Real Time System Exclusive Message
                            - [ ] MIDI Visual Control (MVC)  
                              [CA-032/RP-050 (MMA)](https://www.midi.org/specifications/midi1-specifications/midi-visual-control)
                              MIDI Visual Control Specification v1.0  
                              [CA-032 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/ca32.pdf)
                              MIDI Visual Control Universal Non Realtime System Exclusive Message  
                              [RP-050 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp50spec(mvc).pdf)
                              MIDI Visual Control Specification v1.0
                            - [ ] MIDI Capability Inquiry (MIDI-CI)  
                              [CA-035 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/ca035.pdf)
                              MIDI Capability Inquiry (MIDI-CI) Specification  
                              [CA-035 Spec (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/ca035-spec.pdf)
                              MIDI Capability Inquiry (MIDI-CI) v1.0
        - [x] Read raw input
        - [x] Thru support
        - [ ] Color code
            - [ ] Per source
            - [ ] Per channel
            - [ ] Per message type
  - [ ] Splitter
  - [ ] Merger
  - [ ] Generator
      - [ ] Generate raw output
      - [ ] Buffer/Clipboard any message (raw or decoded) to output
  - [ ] Translator/Filter
  - [ ] File formats
      - [ ] Standard MIDI File (SMF)  
        [RP-001 (MMA)](https://www.midi.org/specifications/file-format-specifications/standard-midi-files/rp-001-v1-0-standard-midi-files-specification-96-1-4-pdf)
        Standard MIDI Files 1.0
          - [ ] Analyzer
          - [ ] Player
          - [ ] Recorder
          - [ ] Extensions
              - [ ] Lyrics Events Definition  
                [RP-017 (MMA)](https://www.midi.org/specifications/file-format-specifications/standard-midi-files/smf-lyric-meta-event-definition)
                SMF Lyric Meta Event Definition  
                [RP-017 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp17.pdf)
                SMF Lyric Meta Event Definition  
                [RP-026 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp26.pdf)
                SMF Lyric Meta Event  
                RP-026 [SMF with Lyrics Application Guide (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/SMFlyricsApplCreation.pdf)  
                RP-026 [SMF with Lyrics Data Creation Guideline](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/SMFlyricsDataCreation.pdf)
              - [ ] Device & Program Name  
                [RP-019 (MMA)](https://www.midi.org/specifications/file-format-specifications/standard-midi-files/smf-device-name-and-program-name-meta-events)
                SMF Device Name and Program Name Meta Events  
                [RP-019 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp19a.pdf)
                SMF Device Name and Program Name Meta Event
              - [ ] International Standard MIDI Code (ISMC)  
                [RP-051 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp51.pdf)
                International Standard MIDI Code
      - [ ] Downloadable Sounds (DLS)
          - [ ] Level 1 (DLS1/DLS-1)  
            [RP-016/MMA-0017 (MMA)](https://www.midi.org/specifications/file-format-specifications/dls-downloadable-sounds/dls-level-1)
            Downloadable Sounds Level 1 v1.1b  
            [RP-016 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/dls1v11a.pdf)
            Downloadable Sounds Level 1 v1.1a  
            [MMA-0017 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/dls1v11b.pdf)  
            Downloadable Sounds Level 1 v1.1b
          - [ ] Level 2 (DLS2/DLS-2)  
            [RP-025/Amd2 (MMA)](https://www.midi.org/specifications/file-format-specifications/dls-downloadable-sounds/dls-level-2-2)
            Downloadable Sounds Level 2.2 v1.0  
            [RP-025 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/dls2v10a.pdf)
            Downloadable Sounds Level 2 v1.0  
            [RP-025/Amd1 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp25dls2amd1.pdf)
            Downloadable Sounds Level 2.1 v1.0  
            [RP-025/Amd2 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/dls2amd2(all)a(pub).pdf)
            Downloadable Sounds Level 2.2 v1.0
          - [ ] GM-Lite Mobile DLS Specification  
            [RP-041 (MMA)](https://www.midi.org/specifications/file-format-specifications/mobile-midi/mobile-dls)
            Mobile DLS (Downloadable Sounds Format for Mobile Applications) v1.0a  
            [RP-041 (AMEI/MSC) **Password**:
            `amei2005`](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp41a(spec)_amei.pdf)
            Mobile DLS (Downloadable Sounds Format for Mobile Applications) v1.0a
      - [ ] RMID  
        [RP-029 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp29spec(rmid)4.pdf)
        Bundling SMF and DLS data in an "RMID" File
      - [ ] eXtensible Music Format (XMF)  
        [RP-030/RP-031/RP-032/RP-039/RP-040/RP-042/RP-043/RP-045/RP-047 (MMA)](https://www.midi.org/specifications/file-format-specifications/xmf-extensible-music-format/extensible-music-format-xmf-2)
        XMF Specification Incorporating all Recommended Practices v1.2  
        [RP-030 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/xmf-v1a.pdf)
        Specification for XMF Meta File Format v1.00a  
        [RP-031 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp31a.pdf)
        Type 0 and Type 1 XMF Files (SMF + DLS)  
        [RP-032 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp32a.pdf)
        SMF Meta Event for XMF Patch Type Prefix  
        [RP-039 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp39spec(xmf).pdf)
        XMF Meta File Format Updates 1.01  
        [RP-040 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp40.pdf)
        XMF Compression Definition for ZLIB  
        [RP-042 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp42.pdf)
        Mobile XMF Content Format Specification  
        [RP-043 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp43.pdf)
        XMF Meta File Format 2.00  
        [RP-045 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp45.pdf)
        Audio Clips for Mobile XMF  
        [RP-047 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp47.pdf)
        ID3 Metadata for XMF Files
  - [ ] Protocol analyzers/decoders
      - [ ] HUI
      - [ ] LCU
      - [ ] MCU
      - Others?
  - [ ] Trigger/Response (Protocol emulator)
      - [ ] HUI
      - [ ] LCU
      - [ ] MCU
      - Others?
  - [ ] Performance analyzer
      - [ ] Round trip latency
      - [ ] Jitter
      - [ ] Bandwidth
      - [ ] Correctness
      - [ ] Stresser/Fuzzer
  - [ ] Hardware toolbox
- [ ] MIDI Implementation Chart
    - [x] reStrucuredText (reST) Templates
        - [x] v1.0 (MIDI 1.0)
        - [x] v2.0  
          [RP-028 (MMA)](https://www.midi.org/specifications/midi1-specifications/midi-1-addenda/midi-implementation-chart-version-2)
          MIDI IMPLEMENTATION CHART V2 INSTRUCTIONS  
          [RP-028 (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp28.pdf)
          Version 2 MIDI Implementation Chart  
          [RP-028 MIDI IMPLEMENTATION CHART V2 INSTRUCTIONS (AMEI/MSC)](https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/rp28(chart_v2).pdf)
    - [ ] Generator from logged traffic?
- [ ] **(WIP)** Logging
    - [x] GUI
    - [ ] To file
        - [ ] Overwrite
        - [ ] Append

Prior art
---------

- [MIDI-OX](http://www.midiox.com/) (Win)
- [Snoize MIDI Monitor](https://www.snoize.com/midimonitor/) (Mac)
- [Midi View](https://hautetechnique.com/midi/midiview/) (Win/Mac)
- [OBD Software Midi Monitor 2002](http://obds.free.fr/midimon/) (Win)
- [Morson PocketMIDI](https://www.morson.jp/pocketmidi-webpage/) (Win/Mac/iOS)
- [Drumstick MIDI Monitor aka KMidiMon](https://kmidimon.sourceforge.io) (Linux)

Legal notice
------------

### License

![GPLv3](https://raw.githubusercontent.com/EMATech/midiexplorer/main/data/assets/sources/gplv3-or-later.svg)

Author: ©2021-2022 Raphaël Doursenaud.

This software is released under the terms of the GNU General Public License, version 3.0 or later (GPL-3.0-or-later).

See [LICENSE](LICENSE).

Logo and icons released under the
[Creative Commons Attribution-Share Alike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/).

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

#### Fonts

- [Roboto](https://github.com/googlefonts/Roboto)  
  Copyright (c) 2015 The Roboto Project Authors  
  Used under the terms of the Apache License, Version 2.0.
- [Roboto Mono](https://github.com/googlefonts/RobotoMono)  
  Copyright (c) 2015 The Roboto Mono Project Authors  
  Used under the terms of the Apache License, Version 2.0.

#### Logo and icons

Composite work based upon:

- [MIDI connector](https://commons.wikimedia.org/wiki/File:MIDI_connector2.svg)  
  Copyright [Fred the Oyster](https://commons.wikimedia.org/wiki/User:Fred_the_Oyster)  
  Used under the terms of the
  [Creative Commons Attribution-Share Alike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) license.
- [Steering Wheel](https://commons.wikimedia.org/wiki/File:Steering_Wheel_Black.svg)  
  Copyright [Spider](https://commons.wikimedia.org/wiki/User:Spider)  
  Used under the terms of the
  [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) license.

### Trademarks

[MIDI](https://midi.org) is a trademark of the MIDI Manufacturers Association (MMA) in the United States of America.

This is not a registered trademark in the European Union and France where I reside.

#### Other

Other trademarks are property of their respective owners and used fairly for descriptive and nominative purposes only.
