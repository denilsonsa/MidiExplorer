# This Python file uses the following encoding: utf-8
#
# SPDX-FileCopyrightText: 2021-2022 Raphaël Doursenaud <rdoursenaud@free.fr>
#
# SPDX-License-Identifier: Unlicense

"""
MIDI related constants.

Derived from official MIDI specifications available at:
- MIDI Association, ex MIDI Manufacturers Association (MMA) [US]: https://midi.org
- Association of Musical Electronics Industry (AMEI) [JP]: (https://www.amei.or.jp/)
- MIDI Standard Committee (MSC) [JP]: http://amei.or.jp/midistandardcommittee
"""
import datetime

MIDI_VERSION = {
    1: "1.0",
    2: "2.0"  # TODO
}

###
# MIDI 1.0 STANDARD CONSTANTS
#
# Reference: MIDI 1.0 Detailed Specification v4.2.1
#            February 1996
###

# TODO: contribute to mido?

# Page 7
MODE = {
    1: {
        'omni': True,
        'poly': True,
    },
    2: {
        'omni': True,
        'poly': False,
    },
    3: {
        'omni': False,
        'poly': True,
    },
    4: {
        'omni': False,
        'poly': False,
    },
}
RX_MODE = {
    1: "Voice messages are received from all Voice channels "
       "and assigned to voices polyphonically",
    2: "Voice messages are received from all Voice Channels, "
       "and control only one voice, monophonically",
    3: "Voice messages are received in Voice Channel N only, "
       "and are assigned to voices polyphonically",
    4: "Voice messages are received in Voice channels N though N+M-1, "
       "and assigned monophonically to voices 1 though M, respectively. "
       "The number of voices \"M\" is specified by the third byte of the Mono Mode Message.",
}
TX_MODE = {
    1: "All voice messages are transmitted in Channel N.",
    2: "Voice messages for one voice are sent in Channel N.",
    3: "Voice messages for all voices are sent in Channel N.",
    4: "Voice messages for voices 1 through M are transmitted in Voice Channels N through N+M-1, respectively. "
       "(Single voice per channel).",
}
DEFAULT_BASIC_CHANNEL = 0  # Equivalent to 1 in MIDI parlance
DEFAULT_MODE = 1

# Page 8
POWER_UP_DEFAULT = {
    "basic_channel": DEFAULT_BASIC_CHANNEL,
    "mode": DEFAULT_MODE,  # Omni On/Poly
}

# Page 10
MIDDLE_C_NOTE = 60
DEFAULT_VELOCITY = 64
NOTE_OFF_VELOCITY = 0

# Page T-2
CHANNEL_VOICE_MESSAGES = {
    0x8: "Note Off",
    0x9: "Note On",
    0xA: "Polyphonic Key Pressure (Aftertouch)",
    0xB: "Control Change",
    0xC: "Program Change",
    0xD: "Channel Pressure (Aftertouch)",
    0xE: "Pitch Bend Change",
}

# Page T-3
CONTROLLER_NUMBERS = {
    0: "Bank Select",
    1: "Modulation Depth",  # Amended by RP-024. Was "Modulation" under RP-003. Was "Modulation wheel or lever".
    2: "Breath controller",
    3: "Undefined",
    4: "Foot controller",
    5: "Portamento Time",
    6: "Data entry MSB",
    7: "Channel Volume",  # Amended by RP-024. Was "Volume" under RP-003. Formerly "Main Volume".
    8: "Balance",
    9: "Undefined",
    10: "Pan",
    11: "Expression",  # Amended by RP-003. Was "Expression Controller".
    12: "Effect Control 1",
    13: "Effect Control 2",
    14: "Undefined",
    15: "Undefined",
    16: "General Purpose Controller 1",
    17: "General Purpose Controller 2",
    18: "General Purpose Controller 3",
    19: "General Purpose Controller 4",
    20: "Undefined",
    21: "Undefined",
    22: "Undefined",
    23: "Undefined",
    24: "Undefined",
    25: "Undefined",
    26: "Undefined",
    27: "Undefined",
    28: "Undefined",
    29: "Undefined",
    30: "Undefined",
    31: "Undefined",
    # LSB for values 0-31
    32: "Bank Select LSB",
    33: "Modulation wheel or lever LSB",
    34: "Breath controller LSB",
    35: "Undefined LSB (3)",
    36: "Foot controller LSB",
    37: "Portamento time LSB",
    38: "Data entry LSB",
    39: "Channel Volume LSB",  # formerly Main Volume
    40: "Balance LSB",
    41: "Undefined LSB (9)",
    42: "Pan LSB",
    43: "Expression Controller LSB",
    44: "Effect Control 1 LSB",
    45: "Effect Control 2 LSB",
    46: "Undefined LSB (14)",
    47: "Undefined LSB (15)",
    48: "General Purpose Controller 1 LSB",
    49: "General Purpose Controller 2 LSB",
    50: "General Purpose Controller 3 LSB",
    51: "General Purpose Controller 4 LSB",
    52: "Undefined LSB (20)",
    53: "Undefined LSB (21)",
    54: "Undefined LSB (22)",
    55: "Undefined LSB (23)",
    56: "Undefined LSB (24)",
    57: "Undefined LSB (25)",
    58: "Undefined LSB (26)",
    59: "Undefined LSB (27)",
    60: "Undefined LSB (28)",
    61: "Undefined LSB (29)",
    62: "Undefined LSB (30)",
    63: "Undefined LSB (31)",
    64: "Hold 1 (Damper)",  # Amended by RP-024. Was "Sustain" under RP-003. Was "Damper pedal (sustain)".
    65: "Portamento ON/OFF",
    66: "Sostenuto",
    67: "Soft",  # Amended by RP-024. Was "Soft pedal".
    68: "Legato Footswitch",  # vv = 00-3F:Normal, 40-7F: Legatto
    69: "Hold 2",
    # FIXME: Add default names structure?
    70: "Sound Controller 1 (Sound Variation)",  # default name: Sound Variation
    71: "Sound Controller 2 (Timbre/Harmonic Intensity)",  # default name: Timbre/Harmonic Intensity
    72: "Sound Controller 3 (Release Time)",  # default name: Release Time
    73: "Sound Controller 4 (Attack Time)",  # default name : Attack Time
    74: "Sound Controller 5 (Brightness)",  # default name: Brightness
    75: "Sound Controller 6 (Decay Time)",  # default name per RP-021: Decay Time
    76: "Sound Controller 7 (Vibrato Rate)",  # default name per RP-021: Vibrato Rate
    77: "Sound Controller 8 (Vibrato Depth)",  # default name per RP-021: Vibrato Depth
    78: "Sound Controller 9 (Vibrato Delay)",  # default name per RP-021: Vibrato Delay
    79: "Sound Controller 10 (undefined)",  # default name per RP-021: undefined
    80: "General Purpose Controller 5",
    81: "General Purpose Controller 6",
    82: "General Purpose Controller 7",
    83: "General Purpose Controller 8",
    84: "Portamento Control",
    85: "Undefined",
    86: "Undefined",
    87: "Undefined",
    88: "High Resolution Velocity Prefix",  # Amended by CA-031. Was "Undefined"
    89: "Undefined",
    90: "Undefined",
    91: "Reverb Send Level",
    # Amended by RP-023. Was "Effects 1 Depth". Formerly and recommended default: External Effects Depth.
    92: "Effects 2 Depth",  # formerly and recommended default: Tremolo Depth
    93: "Chorus Send Level",  # Amended by RP-024. Was "Effects 3 Depth". Formerly and recommended default: Chorus Depth
    94: "Effects 4 Depth",  # formerly and recommended default: Celeste (Detune) Depth
    95: "Effects 5 Depth",  # formerly and recommended default: Phaser Depth
    96: "Data increment",
    97: "Data decrement",
    98: "Non-Registered Parameter Number LSB",
    99: "Non-Registered Parameter Number MSB",
    100: "Resistered Parameter Number LSB",
    101: "Resistered Parameter Number MSB",
    102: "Undefined",
    103: "Undefined",
    104: "Undefined",
    105: "Undefined",
    106: "Undefined",
    107: "Undefined",
    108: "Undefined",
    109: "Undefined",
    110: "Undefined",
    111: "Undefined",
    112: "Undefined",
    113: "Undefined",
    114: "Undefined",
    115: "Undefined",
    116: "Undefined",
    117: "Undefined",
    118: "Undefined",
    119: "Undefined",
    # Reserved for Channel Mode Messages
    120: "Reserved for Channel Mode Messages",
    121: "Reserved for Channel Mode Messages",
    122: "Reserved for Channel Mode Messages",
    123: "Reserved for Channel Mode Messages",
    124: "Reserved for Channel Mode Messages",
    125: "Reserved for Channel Mode Messages",
    126: "Reserved for Channel Mode Messages",
    127: "Reserved for Channel Mode Messages",
}

# Page T-4
REGISTERED_PARAMETER_NUMBERS = {
    # LSB only since MSB is always 0x00. # FIXME: RP-024 defines an LSB of 0x7F!
    0x00: "Pitch Bend Sensitivity",
    0x01: "Channel Fine Tuning",  # Amended by RP-022, was "Fine Tuning" under RP-003.
    0x02: "Channel Coarse Tuning",  # Amended by RP-022 was "Coarse Tuning" under RP-003.
    0x03: "Tuning Program Select",
    0x04: "Tuning Bank Select",
    0x05: "Modulation Depth Range",  # Introduced by CA-026.
}

# Page T-5
# Only valid for the device’s Basic Channel Number
CHANNEL_MODE_MESSAGES = {
    120: "All Sound Off",  # 0
    121: "Reset All Controllers",  # 0
    122: "Local Control",  # 0, Local Control Off. 127, Local Control On.
    123: "All Notes Off",  # 0
    124: "Omni Mode Off (All Notes Off)",  # 0
    125: "Omni Mode On (All Notes Off)",  # 0
    126: "Mono Mode On (Poly Mode Off) (All Notes Off)",
    # M, where M is the number of channels. 0, the number of channels equals the number of voices in the receiver.
    127: "Poly Mode On (Mono Mode Off) (All Notes Off)",
}

# Page T-6
SYSTEM_COMMON_MESSAGES = {
    0xF1: "MIDI Time Code Quarter Frame",
    0xF2: "Song Position Pointer",
    0xF3: "Song Select",
    0xF4: "Undefined",
    0xF5: "Undefined",
    0xF6: "Tune Request",
    0xF7: "EOX: \"End of System Exclusive\" flag",
}

# Page T-7
SYSTEM_REAL_TIME_MESSAGES = {
    0xF8: "Timing Clock",
    0xF9: "Undefined",
    0xFA: "Start",
    0xFB: "Continue",
    0xFC: "Stop",
    0xFD: "Undefined",
    0xFE: "Active Sensing",
    0xFF: "System Reset",
}

# Page T-8
SYSTEM_EXCLUSIVE_MESSAGES = {
    0xF0: "Start of System Exclusive",
    0xF7: "End of System Exclusive",
}
# See SYSTEM_EXCLUSIVE_MANUFACTURER_ID

# All status bytes
STATUS_BYTES = {}
CHANNEL_VOICE_BYTES = {}
for status_nibble, name in CHANNEL_VOICE_MESSAGES.items():
    for channel in range(16):
        status_byte = (status_nibble << 4) + channel
        CHANNEL_VOICE_BYTES.update({status_byte: name})
STATUS_BYTES.update(CHANNEL_VOICE_BYTES)
STATUS_BYTES.update(SYSTEM_COMMON_MESSAGES)
STATUS_BYTES.update(SYSTEM_REAL_TIME_MESSAGES)
STATUS_BYTES.update(SYSTEM_EXCLUSIVE_MESSAGES)

# Page T-9
DEFINED_UNIVERSAL_SYSTEM_EXCLUSIVE_MESSAGES_NON_REAL_TIME_SUB_ID_1 = {  # 0x7E
    0x00: "Unused",
    0x01: "Sample Dump Header",
    0x02: "Sample Data Packet",
    0x03: "Sample Dump Request",
    0x04: "MIDI Time Code",  # SUB-ID #2
    0x05: "Sample Dump Extensions",  # SUB-ID #2
    0x06: "General Information",  # SUB-ID #2
    0x07: "File Dump",  # SUB-ID #2
    0x08: "MIDI Tuning Standard",  # SUB-ID #2
    0x09: "General MIDI Message",  # SUB-ID #2
    0x0B: "File Reference Message Command",  # Introduced by CA-018.
    0x7B: "End of File",
    0x7C: "Wait",
    0x7D: "Cancel",
    0x7E: "NAK",
    0x7F: "ACK",
}
NON_REAL_TIME_MIDI_TIME_CODE_SUB_ID_2 = {  # 0x04
    0x00: "Special",
    0x01: "Punch In Points",
    0x02: "Punch Out Points",
    0x03: "Delete Punch In Points",
    0x04: "Delete Punch Out Points",
    0x05: "Event Start Point",
    0x06: "Event Stop Point",
    0x07: "Event Start Points with additional info.",
    0x08: "Event Stop Points with additional info.",
    0x09: "Delete Event Start Point",
    0x0A: "Delete Event Stop Point",
    0x0B: "Cue Points",
    0x0C: "Cue Points with additional info.",
    0x0D: "Delete Cue Point",
    0x0E: "Event Name in additional info.",
}
NON_REAL_TIME_SAMPLE_DUMP_EXTENSIONS_SUB_ID_2 = {  # 0x05
    0x01: "Multiple Loop Points",
    0x02: "Loop Points Request",
    0x03: "Sample Name Transmission",  # Introduced by CA-019.
    0x04: "Sample Name Request",  # Introduced by CA-019.
    0x05: "Extended Dump Header",  # Introduced by CA-019.
    0x06: "Sample Extended Loop Point Transmission",  # Introduced by CA-019.
    0x07: "Sample Extended Loop Point Request",
    # Introduced by CA-019. FIXME: report typo in CA-019, "Transmission" instead of "Request" in the sample.
}
NON_REAL_TIME_GENERAL_INFORMATION_SUB_ID_2 = {  # 0x06
    0x01: "Identity Request",
    0x02: "Identity Reply",
}
NON_REAL_TIME_FILE_DUMP_SUB_ID_2 = {  # 0x07
    0x01: "Header",
    0x02: "Data Packet",
    0x03: "Request",
}
NON_REAL_TIME_MIDI_TUNING_STANDARD_SUB_ID_2 = {  # 0x08
    0x00: "Bulk Dump Request",
    0x01: "Bulk Dump Reply",
    0x03: "Bulk Tuning Dump Request (Bank)",  # Introduced by CA-020.
    0x04: "Key-Based Tuning Dump",  # Introduced by CA-020.
    0x05: "Scale/Octave Tuning Dump, 1 byte format",  # Introduced by CA-020.
    0x06: "Scale/Octave Tuning Dump, 2 byte format",  # Introduced by CA-020.
    0x07: "Single Note Tuning Change (Bank)",  # Introduced by CA-020.
    0x08: "Scale/Octave Tuning 1-Byte Form",  # Introduced by CA-021.
    0x09: "Scale/Octave Tuning 2-Byte Form",  # Introduced by CA-021.
}
NON_REAL_TIME_GENERAL_MIDI_SUB_ID_2 = {  # 0x09
    0x01: "General MIDI 1 On",  # Amended by CA-027. Was "General MIDI System On".
    0x02: "General MIDI Off",  # Amended by RP-003. Was "General MIDI System Off"
    0x03: "General MIDI 2 On",  # Introduced by CA-027.
}
NON_REAL_TIME_FILE_REFERENCE_MESSAGE_COMMAND_SUB_ID_2 = {  # 0x0B
    # Introduced by CA-018.
    0x00: "reserved",
    0x01: "Open File",
    0x02: "Select or Reselect Contents",
    0x03: "Open File and Select Contents",
    0x04: "Close File",
    0x05: "reserved",
    # FIXME: Fill with reserved.
    0x7F: "reserved",
}
NON_REAL_TIME_SUB_ID_2_FROM_1 = {
    0x04: NON_REAL_TIME_MIDI_TIME_CODE_SUB_ID_2,
    0x05: NON_REAL_TIME_SAMPLE_DUMP_EXTENSIONS_SUB_ID_2,
    0x06: NON_REAL_TIME_GENERAL_INFORMATION_SUB_ID_2,
    0x07: NON_REAL_TIME_FILE_DUMP_SUB_ID_2,
    0X08: NON_REAL_TIME_MIDI_TUNING_STANDARD_SUB_ID_2,
    0X09: NON_REAL_TIME_GENERAL_MIDI_SUB_ID_2,
    0x0B: NON_REAL_TIME_FILE_REFERENCE_MESSAGE_COMMAND_SUB_ID_2,  # Introduced by CA-018.
}

# Page T-10
DEFINED_UNIVERSAL_SYSTEM_EXCLUSIVE_MESSAGES_REAL_TIME_SUB_ID_1 = {  # 0x7F
    0x00: "Unused",
    0x01: "MIDI Time Code",  # Has a SUB-ID #2.
    0x02: "MIDI Show Control",  # Has a SUB-ID #2.
    0x03: "Notation Information",  # Has a SUB-ID #2.
    0x04: "Device Control",  # Has a SUB-ID #2.
    0x05: "Real Time MTC Cueing",  # Has a SUB-ID #2.
    0x06: "MIDI Machine Control Commands",  # Has a SUB-ID #2.
    0x07: "MIDI Machine Control Responses",  # Has a SUB-ID #2.
    0x08: "MIDI Tuning Standard",  # Has a SUB-ID #2.
    0x09: "Controller Destination Setting",  # Introduced by CA-022. Has SUB-ID#2.
    0x0A: "Key-Based Instrument Control",  # Introduced by CA-023. Has SUB-ID #2.
    0x0B: "Scalable Polyphony MIDI",  # Introduced by CA-029. Has a SUB-ID#2.
    0x0C: "Mobile Phone Control Message",  # Introduced by CA-030. Has a SUB-ID#2.
}
REAL_TIME_MIDI_TIME_CODE_SUB_ID_2 = {  # 0x01
    0x01: "Full Message",
    0x02: "User Bits",
}
REAL_TIME_SHOW_CONTROL_SUB_ID_2 = {  # 0x02
    # Extracted from MSC specification
    0x00: "(Reserved)",

    0x01: "Lighting (General Category)",
    0x02: "Moving Lights",
    0x03: "Color Changers",
    0x04: "Strobes",
    0x05: "Lasers",
    0x06: "Chasers",

    0x10: "Sound (General Category)",
    0x11: "Music",
    0x12: "CD Players",
    0x13: "EPROM Playback",
    0x14: "Audio Tape Machines",
    0x15: "Intecoms",
    0x16: "Amplifiers",
    0x17: "Audio Effects Devices",
    0x18: "Equalizers",

    0x20: "Machinery (General Category)",
    0x21: "Rigging",
    0x22: "Flys",
    0x23: "Lifts",
    0x24: "Turntables",
    0x25: "Trusses",
    0x26: "Robots",
    0x27: "Animation",
    0x28: "Floats",
    0x29: "Breakaways",
    0x2A: "Barges",

    0x30: "Video (General Category)",
    0x31: "Video Tape Machines",
    0x32: "Video Cassette Machines",
    0x33: "Video Disc Players",
    0x34: "Video Switchers",
    0x35: "Video Effects",
    0x36: "Video Character Generators",
    0x37: "Video Still Stores",
    0x38: "Video Monitors",

    0x40: "Projection (General Category)",
    0x41: "Film Projectors",
    0x42: "Slide Projectors",
    0x43: "Video Projectors",
    0x44: "Dissolvers",
    0x45: "Shutter Controls",

    0x50: "Process Control (General Category)",
    0x51: "Hydraulic Oil",
    0x52: "H2O",
    0x53: "CO2",
    0x54: "Compressed Air",
    0x55: "Natural Gas",
    0x56: "Fog",
    0x57: "Smoke",
    0x58: "Cracked Haze",

    0x60: "Pyro (General Category)",
    0x61: "Fireworks",
    0x62: "Explosions",
    0x63: "Flame",
    0x64: "Smoke pots",

    0x7F: "All-types",
}
REAL_TIME_NOTATION_INFORMATION_SUB_ID_2 = {  # 0x03
    0x01: "Bar Number",
    0x02: "Time Signature (Immediate)",
    0x03: "Time Signature (Delayed)",
}
REAL_TIME_DEVICE_CONTROL_SUB_ID_2 = {  # 0x04
    0x01: "Master Volume",
    0x02: "Master Balance",
    0x03: "Master Fine Tuning",  # Introduced by CA-025.
    0x04: "Master Coarse Tuning",  # Introduced by CA-025.
    0x05: "Global Parameter Control",  # Introduced by CA-024.
}
REAL_TIME_MTC_CUEING_SUB_ID_2 = {  # 0x05
    0x00: "Special",
    0x01: "Punch In Points",
    0x02: "Punch Out Points",
    0x03: "(Reserved)",
    0x04: "(Reserved)",
    0x05: "Event Start Point",
    0x06: "Event Stop Point",
    0x07: "Event Start Points with additional info.",
    0x08: "Event Stop Points with additional info.",
    0x09: "(Reserved)",
    0x0A: "(Reserved)",
    0x0B: "Cue Points",
    0x0C: "Cue Points with additional info.",
    0x0D: "(Reserved)",
    0x0E: "Event Name in additional info.",
}
REAL_TIME_MIDI_MACHINE_CONTROL_COMMANDS_SUB_ID_2 = {  # 0x06
    # Extracted from the MMC specification
    0x00: "(Reserved)",
    0x01: "STOP",
    0x02: "PLAY",
    0x03: "DEFERRED PLAY",
    0x04: "FAST FORWARD",
    0x05: "REWIND",
    0x06: "RECORD STROBE",
    0x07: "RECORD EXIT",
    0x08: "RECORD PAUSE",
    0x09: "PAUSE",
    0x0A: "EJECT",
    0x0B: "CHASE",
    0x0C: "COMMAND ERROR RESET",
    0x0D: "MMC RESET",

    0x40: "WRITE",
    0x41: "MASKED WRITE",
    0x42: "READ",
    0x43: "UPDATE",
    0x44: "LOCATE",
    0x45: "VARIABLE PLAY",
    0x46: "SEARCH",
    0x47: "SHUTTLE",
    0x48: "STEP",
    0x49: "ASSIGN SYSTEM MASTER",
    0x4A: "GENERATOR COMMAND",
    0x4B: "MIDI TIME CODE COMMAND",
    0x4C: "MOVE",
    0x4D: "ADD",
    0x4E: "SUBTRACT",
    0x4F: "DROP FRAME ADJUST",
    0x50: "PROCEDURE",
    0x51: "EVENT",
    0x52: "GROUP",
    0x53: "COMMAND SEGMENT",
    0x54: "DEFERRED VARIABLE PLAY",
    0x55: "RECORD STROBE VARIABLE",

    0x7C: "WAIT",

    0x7F: "RESUME",
}
REAL_TIME_MIDI_MACHINE_CONTROL_RESPONSES_SUB_ID_2 = {  # 0x07
    # Extracted from the MMC specification
    0x00: "(Reserved)",
    0x01: "SELECTED TIME CODE",
    0x02: "SELECTED MASTER CODE",
    0x03: "REQUESTED OFFSET",
    0x04: "ACTUAL OFFSET",
    0x05: "LOCK DEVIATION",
    0x06: "GENERATOR TIME CODE",
    0x07: "MIDI TIME CODE INPUT",
    0x08: "GP0 / LOCATE POINT",
    0x09: "GP1",
    0x0A: "GP2",
    0x0B: "GP3",
    0x0C: "GP4",
    0x0D: "GP5",
    0x0E: "GP6",
    0x0F: "GP7",

    0x20: "(Reserved)",
    0x21: "Short SELECTED TIME CODE",
    0x22: "Short SELECTED MASTER CODE",
    0x23: "Short REQUESTED OFFSET",
    0x24: "Short ACTUAL OFFSET",
    0x25: "Short LOCK DEVIATION",
    0x26: "Short GENERATOR TIME CODE",
    0x27: "Short MIDI TIME CODE INPUT",
    0x28: "Short GP0 / LOCATE POINT",
    0x29: "Short GP1",
    0x2A: "Short GP2",
    0x2B: "Short GP3",
    0x2C: "Short GP4",
    0x2D: "Short GP5",
    0x2E: "Short GP6",
    0x2F: "Short GP7",

    0x40: "SIGNATURE",
    0x41: "UPDATE RATE",
    0x42: "RESPONSE ERROR",
    0x43: "COMMAND ERROR",
    0x44: "COMMAND ERROR LEVEL",
    0x45: "TIME STANDARD",
    0x46: "SELECTED TIME CODE SOURCE",
    0x47: "SELECTED TIME CODE USERBITS",
    0x48: "MOTION CONTROL TALLY",
    0x49: "VELOCITY TALLY",
    0x4A: "STOP MODE",
    0x4B: "FAST MODE",
    0x4C: "RECORD MODE",
    0x4D: "RECORD STATUS",
    0x4E: "TRACK RECORD STATUS",
    0x4F: "TRACK RECORD READY",
    0x50: "GLOBAL MONITOR",
    0x51: "RECORD MONITOR",
    0x52: "TRACK SYNC MONITOR",
    0x53: "TRACK INPUT MONITOR",
    0x54: "STEP LENGTH",
    0x55: "PLAY SPEED REFERENCE",
    0x56: "FIXED SPEED",
    0x57: "LIFTER DEFEAT",
    0x58: "CONTROL DISABLE",
    0x59: "RESOLVED PLAY MODE",
    0x5A: "CHASE MODE",
    0x5B: "GENERATOR COMMAND TALLY",
    0x5C: "GENERATOR SET UP",
    0x5D: "GENERATOR USERBITS",
    0x5E: "MIDI TIME CODE COMMAND TALLY",
    0x5F: "MID TIME CODE SET UP",

    0x60: "PROCEDURE RESPONSE",
    0x61: "EVENT RESPONSE",
    0x62: "TRACK MUTE",
    0x63: "VITC INSERT ENABLE",
    0x64: "RESPONSE SEGMENT",
    0x65: "FAILURE",

    0x7C: "WAIT",

    0x7F: "RESUME",
}
REAL_TIME_MIDI_TUNING_STANDARD_SUB_ID_2 = {  # 0x08
    0x02: "Note Change",
    0x07: "Single Note Tuning Change (Bank)",  # Introduced by CA-020.
    0x08: "Scale/Octave Tuning 1-Byte Form",  # Introduced in CA-021.
    0x09: "Scale/Octave Tuning 2-Byte Form",  # Introduced in CA-021.
}
REAL_TIME_CONTROLLER_DESTINATION_SETTING_SUB_ID_2 = {  # 0x09
    # Introduced by CA-022.
    0x01: "Channel Pressure (Aftertouch)",
    0x02: "Polyphonic Key Pressure (Aftertouch)",
    0x03: "Control Change",
}
REAL_TIME_KEY_BASED_INSTRUMENT_CONTROL_SUB_ID_2 = {  # 0x0A
    # Introduced by CA-023.
    0x01: "Basic Message",
}
REAL_TIME_SCALABLE_POLYPHONY_MIDI_SUB_ID_2 = {  # 0x0B
    # Introduced by CA-029.
    0x01: "MIP Message",
}
REAL_TIME_MOBILE_PHONE_CONTROL_MESSAGE_SUB_ID_2 = {  # 0x0C
    # Introduced by CA-030.
    0x00: "",  # Always 00
}
REAL_TIME_SUB_ID_2_FROM_1 = {
    0x01: REAL_TIME_MIDI_TIME_CODE_SUB_ID_2,
    0x02: REAL_TIME_SHOW_CONTROL_SUB_ID_2,
    0x03: REAL_TIME_NOTATION_INFORMATION_SUB_ID_2,
    0x04: REAL_TIME_DEVICE_CONTROL_SUB_ID_2,
    0x05: REAL_TIME_MTC_CUEING_SUB_ID_2,
    0x06: REAL_TIME_MIDI_MACHINE_CONTROL_COMMANDS_SUB_ID_2,
    0x07: REAL_TIME_MIDI_MACHINE_CONTROL_RESPONSES_SUB_ID_2,
    0x08: REAL_TIME_MIDI_TUNING_STANDARD_SUB_ID_2,
    0x09: REAL_TIME_CONTROLLER_DESTINATION_SETTING_SUB_ID_2,  # Introduced by CA-022.
    0x0A: REAL_TIME_KEY_BASED_INSTRUMENT_CONTROL_SUB_ID_2,  # Introduced by CA-024.
    0x0B: REAL_TIME_SCALABLE_POLYPHONY_MIDI_SUB_ID_2,  # Introduced by CA-029.
    0x0C: REAL_TIME_MOBILE_PHONE_CONTROL_MESSAGE_SUB_ID_2,  # Introduced by CA-030.
}

# Page T-11
# Up to date sources:  TODO: update, write a scrapper?
# - https://www.midi.org/specifications-old/item/manufacturer-id-numbers
# - http://www.amei.or.jp/report/report6.html (JAPANESE)
# - http://www.amei.or.jp/report/System_ID_e.html (ENGLISH)
SYSTEM_EXCLUSIVE_ID = {
    0x00: {  # 3-byte IDs
        # American Group (00-1F)
        0x00: {
            0x00: "Not to be used!",

            0x01: "Time Warner Interactive",

            0x07: "Digital Music Corp.",
            0x08: "IOTA Systems",
            0x09: "New England Digital",
            0x0A: "Artisyn",
            0x0B: "IVL Technologies",
            0x0C: "Southern Music Systems",
            0x0D: "Lake Butler Sound Company",
            0x0E: "Alesis",

            0x10: "DOD Electronics",
            0x11: "Studer-Editech",

            0x14: "Perfect Fretworks",
            0x15: "KAT",
            0x16: "Opcode",
            0x17: "Rane Corp.",
            0x18: "Anadi Inc.",
            0x19: "KMX",
            0x1A: "Allen & Heath Brenell",
            0x1B: "Peavey Electronics",
            0x1C: "360 Systems",
            0x1D: "Spectrum Design and Development",
            0x1E: "Marquis Music",
            0x1F: "Zeta Systems",
            0x20: "Axxes",
            0x21: "Orban",

            0x24: "KTI",
            0x25: "Breakaway Technologies",
            0x26: "CAE",

            0x29: "Rocktron Corp.",
            0x2A: "PianoDisc",
            0x2B: "Cannon Research Group",

            0x2D: "Regors Instrument Corp.",
            0x2E: "Blue Sky Logic",
            0x2F: "Encore Electronics",
            0x30: "Uptown",
            0x31: "Voce",
            0x32: "CTI Audio, Inc. (Music. Intel Dev.)",
            0x33: "S&S Research",
            0x34: "Broderbund Software, Inc.",
            0x35: "Allen Organ Co.",

            0x37: "Music Quest",
            0x38: "APHEX",
            0x39: "Gallien Krueger",
            0x3A: "IBM",

            0x3C: "Hotz Instruments Technologies",
            0x3D: "ETA Lighting",
            0x3E: "NSI Corporation",
            0x3F: "Ad Lib, Inc.",
            0x40: "Richmond Sound Design",
            0x41: "Microsoft",
            0x42: "The Software Toolworks",
            0x43: "Niche/RJMG",
            0x44: "Intone",

            0x47: "GT Electronics/Groove Tubes",
            # TODO: Report to MMA that 0x4F is duplicated here as "InterMIDI, Inc." instead of just "InterMIDI"?
            0x49: "Timeline Vista",
            0x4A: "Mesa Boogie",

            0x4C: "Sequoia Development",
            0x4D: "Studio Electrionics",
            0x4E: "Euphonix",
            0x4F: "InterMIDI",
            0x50: "MIDI Solutions",
            0x51: "3DO Company",
            0x52: "Lightwave Research",
            0x53: "Micro-W",
            0x54: "Spectral Synthesis",
            0x55: "Lone Wolf",
            0x56: "Studio Technologies",
            0x57: "Peterson EMP",
            0x58: "Atari",
            0x59: "Marion Systems",
            0x5A: "Design Event",
            0x5B: "Winjammer Software",
            0x5C: "AT&T Bell Labs",
            0x5E: "Symetrix",
            0x5F: "MIDI the world",
            0x60: "Desper Products",
            0x61: "Micros ’N MIDI",
            0x62: "Accordians Intl",
            0x63: "EuPhonics",
            0x64: "Musonix",
            0x65: "Turtle Beach Systems",
            0x66: "Mackie Designs",
            0x67: "Compuserve",
            0x68: "BES Technologies",
            0x69: "QRS Music Rolls",
            0x6A: "P G Music",
            0x6B: "Sierra Semiconductor",
            0x6C: "EpiGraf Audio Visual",
            0x6D: "Electronics Deiversified",
            0x6E: "Tune 1000",
            0x6F: "Advanced Micro Devices",
            0x70: "Mediamation",
            0x71: "Sabine Music",
            0x72: "Woog Labs",
            0x73: "Micropolis",
            0x74: "Ta Horng Musical Inst.",
            0x75: "eTek (formerly Forte)",
            0x76: "Electrovoice",
            0x77: "Midisoft",
            0x78: "Q-Sound Labs",
            0x79: "Westrex",
            0x7A: "NVidia",
            0x7B: "ESS Technology",
            0x7C: "MediaTrix Peripherals",
            0x7D: "Brooktree",
            0x7E: "Otari",
            0x7F: "Key Electronics",
            0x80: "Crystalake Multimedia",
            0x81: "Crystal Semiconductor",
            0x82: "Rockwell Semiconductor",
        },
        # European Group (20-3F)
        0x20: {
            0x00: "Dream",
            0x01: "Strand Lighting",
            0x02: "Amek Systems",

            0x04: "Böhm Electronic",

            0x06: "Trident Audio",
            0x07: "Real World Studio",

            0x09: "Yes Technology",
            0x0A: "Automatica",
            0x0B: "Bontempi/Farfisa",
            0x0C: "F.B.T. Elettronica",
            0x0D: "MidiTemp",
            0x0E: "LA Audio (Larking Audio)",
            0x0F: "Zero 88 Lighting Limited",
            0x10: "Micon Audio Electronics GmbH",
            0x11: "Forefront Technology",

            0x13: "Kenton Electronics",

            0x15: "ADB",
            0x16: "Marshall Products",
            0x17: "DDA",
            0x18: "BSS",
            0x19: "MA Lighting Technology",
            0x1A: "Fatar",
            0x1B: "QSC Audio",
            0x1C: "Artisan Classic Organ",
            0x1D: "Orla Spa",
            0x1E: "Pinnacle Audio",
            0x1F: "TC Electronics",
            0x20: "Doepfer Musikelektronik",
            0x21: "Creative Technology Pte",
            0x22: "Minami/Seiyddo",
            0x23: "Goldstar",
            0x24: "Midisoft s.a.s. di M. Cima",
            0x25: "Samick",
            0x26: "Penny and Giles",
            0x27: "Acorn Computer",
            0x28: "LSC Electronics",
            0x29: "Novation EMS",
            0x2A: "Samkyung Mechatroncis",
            0x2B: "Medeli Electronics",
            0x2C: "Charlie Lab",
            0x2D: "Blue Chip Music Tech",
            0x2E: "BBE OH Corp",
        },
        # Japanese Group (40-5F)
        0x40: {
            0x00: "Crimson Technology Inc.",
            0x01: "Vodafone Co., Ltd.",

            0x03: "D & M Holdings Co., Ltd.",  # Denon & Marantz
            0x04: "XING Inc.",
            0x05: "AlphaTheta Corporation",
            0x06: "Pioneer Corporation",
            0x07: "Slick Co., Ltd.",
        },
        0x48: {
            0x00: "sigboost Co., Ltd.",
            0x01: "Lost Technology",
            0x02: "Uchiwa Fujin",
            0x03: "Tsukuba Science Co., Ltd.",
            0x04: "Sonicware Co., Ltd.",
            0x05: "Poppy only workshop",
            0x06: "BLACK CORPORATION GK",
            0x07: "G-TONE Giken Co., Ltd.",
        },
        0x60: {  # Others Group (60-7F)
        }
    },

    # 1-byte IDs

    # American Group (01-1F)
    0x01: "Sequencial",
    0x02: "IDP",
    0x03: "Voyetra/Octave-Plateau",
    0x04: "Moog",
    0x05: "Passport Designs",
    0x06: "Lexicon",
    0x07: "Kurzweil",
    0x08: "Fender",
    0x09: "Gulbransen",
    0x0A: "AKG Acoustics",
    0x0B: "Voyce Music",
    0x0C: "Waveframe Corp",
    0x0D: "ADA Signal Processors",
    0x0E: "Garfield Electronics",
    0x0F: "Ensoniq",
    0x10: "Oberheim",
    0x11: "Apple Computer",
    0x12: "Grey Matter Response",
    0x13: "Digidesign",
    0x14: "Palm Tree Instruments",
    0x15: "JLCooper Electronics",
    0x16: "Lowrey",
    0x17: "Adams-Smith",
    0x18: "Emu Systems",
    0x19: "Harmony Systems",
    0x1A: "ART",
    0x1B: "Baldwin",
    0x1C: "Eventide",
    0x1D: "Inventronics",

    0x1F: "Clarity",

    # European Group (20-3F)
    0x20: "Passac",
    0x21: "SIEL",
    0x22: "Synthaxe",

    0x24: "Hohner",
    0x25: "Twister",
    0x26: "Solton",
    0x27: "Jellinghaus MS",
    0x28: "Southworth Music Systems",
    0x29: "PPG",
    0x2A: "JEN",
    0x2B: "SSL Limited",
    0x2C: "Audio Veritrieb",

    0x2F: "Elka",
    0x30: "Dynacord",
    0x31: "Viscount",

    0x33: "Clavia Digital Instruments",
    0x34: "Audio Architecture",
    0x35: "General Music Corp.",

    0x39: "Soundcraft Electronics",

    0x3B: "Wersi",
    0x3C: "Avab Electronik Ab",
    0x3D: "Digigram",
    0x3E: "Waldorf Electronics",
    0x3F: "Quasimidi",

    # Japanese Group (40-5F)
    0x40: "Kawai",
    0x41: "Roland",
    0x42: "Korg",
    0x43: "Yamaha",
    0x44: "Casio",

    # Shigenori Kamiya.
    # Worked with Roland and made MIDI sequence software and tone editors such as Odyssey-K for the MSX Computer.
    0x46: "Kamiya Studio",
    0x47: "Akai",
    0x48: "Japan Victor",  # JVC
    0x49: "Mesosha",
    0x4A: "Hoshino Gakki",  # Ibanez & Tama
    0x4B: "Fujitsu Elect",
    0x4C: "Sony",
    0x4D: "Nisshin Onpa",  # Maxon
    0x4E: "TEAC",  # Tascam

    0x50: "Matsushita Electric",  # Panasonic
    0x51: "Fostex",
    0x52: "Zoom",
    0x53: "Midori Electronics",
    0x54: "Matsushita Communication Industrial",  # Panasonic
    0x55: "Suzuki Musical Inst. Mfg.",
    # Update from AMEI database (56-5F)
    0x56: "Fuji Onkyo Co., Ltd.",
    0x57: "Onkyo Research Institute Co., Ltd.",

    0x5A: "Internet Co., Ltd.",

    0x5C: "Seekers Co., Ltd.",

    0x5F: "SD Card Association",

    # Others Group (60-7C)

    # Page T-8
    # Special Group (7D-7F)
    0x7D: "Non Commercial",
    0x7E: "Non-Real Time",
    0x7F: "Realtime"
}

# ID Groups
SYSTEM_EXCLUSIVE_ID_GROUPS = {}
for syx_id in range(0x00, 0x7C + 1):
    SYSTEM_EXCLUSIVE_ID_GROUPS.update({syx_id: "Manufacturer"})
SYSTEM_EXCLUSIVE_ID_GROUPS.update({0x7D: "Reserved"})
for syx_id in range(0x7E, 0x7F + 1):
    SYSTEM_EXCLUSIVE_ID_GROUPS.update({syx_id: "Universal"})

# ID Regions
SYSTEM_EXCLUSIVE_ID_REGIONS = {}
for syx_id in range(0x00, 0x1F + 1):
    SYSTEM_EXCLUSIVE_ID_REGIONS.update({syx_id: "American"})
for syx_id in range(0x20, 0x3F + 1):
    SYSTEM_EXCLUSIVE_ID_REGIONS.update({syx_id: "European"})
for syx_id in range(0x40, 0x5F + 1):
    SYSTEM_EXCLUSIVE_ID_REGIONS.update({syx_id: "Japanese"})

# Page T-14
ADDITIONAL_SPECIFICATIONS = {
    "MIDI Time Code",
    "MIDI Show Control 1.1",
    "MIDI Machine Control",
    "Standard MIDI Files",
    "General MIDI System Level 1"
}

###
# Recommended Practices (RP)
#           &
# Confirmation of Approval (CA)
#
# Official history list:
# http://amei.or.jp/midistandardcommittee/RP&CAj.html
###

###
# CA-001
# CA-002
# CA-003
# CA-004
# CA-005
# CA-006
# CA-007
# CA-008
# CA-009
# CA-010
# CA-011
# CA-012
# CA-013
# CA-014
# CA-015
# CA-016
# CA-017
###

# FIXME: original specifications lost to time. Probably integrated into the MIDI 1.0 specification.

###
# STANDARD MIDI FILES (SMF)
# v1.0
#
# Reference: RP-001
###

# Page 2 (PDF: 4)
SMF_MAC_FILE_TYPE = 'Midi'
SMF_MAC_CLIPBOARD_DATA_TYPE = 'Midi'

# Page 3 (PDF: 5)
SMF_CHUNK_TYPES = {
    'MThd': "Header",
    'MTrk': "Track",
}

# Page 4 (PDF: 6)
SMF_HEADER_FORMATS = {
    0: "Single multi-channel track",
    1: "One or more simultaneous tracks (or MIDI outputs) of a sequence",
    2: "One or more sequentially independent single-track patterns",
}

SMF_HEADER_DIVISION_FORMAT = {
    0: "Ticks per quarter-note",
    1: "Negative SMPTE FPS & Ticks per frame",
}

SMF_HEADER_DIVISION_SMPTE = {
    -24: "24 FPS",  # Film
    -25: "25 FPS",  # PAL
    -29: "30 FPS DF",  # drop-frame (29.97 FPS NTSC)
    -30: "30 FPS",  # non-drop
}

# Page 6-7 (PDF: 8-9)
SMF_TRACK_EVENT_TYPES = {
    0xF0: "Sysex",
    0xF7: "Escape (Sysex)",
    0xFF: "Meta",
}

# Page 8-11 (PDF: 10-13)
SMF_TRACK_EVENT_META_EVENT_TYPES = {
    0x00: "Sequence Number",
    # 0x01 to 0XF reserved for various types of text events.
    0x01: "Text Event",
    0x02: "Copyright Notice",
    0x03: "Sequence/Track Name",
    0x04: "Instrument Name",
    0x05: "Lyric",  # Renamed to "Display/Lyric" by RP-026 (See below).
    0x06: "Marker",
    0x07: "Cue Point",
    # 0x08: "Program Name",  # Added by RP-019 (See below).
    # 0x09: "Device Name",  # Added by RP-019 (See below).

    0x20: "MIDI Channel Prefix",

    0x2F: "End of Track",

    0x51: "Set Tempo",

    0x54: "SMPTE Offset",

    0x58: "Time Signature",
    0x59: "Key Signature",
    # 0x60: "XMF Patch Type Prefix",  # Added by RP-032 (See below).

    0x7F: "Sequencer-Specific Meta-Event",
}
_VLQ = -1  # Variable-Length Quantity
SMF_TRACK_EVENT_META_EVENT_PARAMETERS = {
    0x00: {  # Sequence number
        'length': 2,  # bytes
        'bytes': {
            0: "Number MSB",
            1: "Number LSB",
        },
    },
    0x01: {  # Text
        'length': _VLQ,
        'bytes': {
            _VLQ: "Any amount of text describing anything",
        },
    },
    0x02: {  # Copyright Notice
        'length': _VLQ,
        'bytes': {
            _VLQ: "Copyright notice",
        },
    },
    0x03: {  # Sequence/Track Name
        'length': _VLQ,
        'bytes': {
            _VLQ: "Name of the sequence or track",
        },
    },
    0x04: {  # Instrument Name
        'length': _VLQ,
        'bytes': {
            _VLQ: "Description of the type of instrumentation to be used in that track",
        },
    },
    0x05: {  # Lyric
        'length': _VLQ,
        'bytes': {
            _VLQ: "Lyric to be sung",
        },
    },
    0x06: {  # Marker
        'length': _VLQ,
        'bytes': {
            _VLQ: "Name of that point in the sequence",
        },
    },
    0x07: {  # Cue Point
        'length': _VLQ,
        'bytes': {
            _VLQ: "Description of something happening at that point in the musical score",
        },
    },
    0x20: {  # MIDI Channel Prefix
        'length': 1,
        'bytes': {
            0: "MIDI Channel",
        }
    },
    0x2F: {  # End of Track
        'length': 0,
    },
    0x51: {  # Set Tempo
        'length': 3,
        'bytes': {
            0: 'Tempo (MSB)',
            1: 'Tempo (Middle Byte)',
            2: 'Tempo (LSB)',
        },
    },
    0x54: {  # SMPTE Offset
        'length': 5,
        'bytes': {
            0: "Hours (Including Time Code Type)",  # See section: MIDI Time Code
            1: "Minutes",
            2: "Seconds",
            3: "Frames",
            4: "Fractional frames (100ths of a frame)"
        },
    },
    0x58: {  # Time Signature
        'length': 4,
        'bytes': {
            0: "Numerator",
            1: "Denominator",
            2: "MIDI clocks in a metronome click",
            3: "Number of 32nd-notes in MIDI quarter-note (24 MIDI Clocks)",
        },
    },
    0x59: {  # Key Signature
        'length': 2,
        'bytes': {
            0: "Flats",
            1: "Key",
        }
    },
    0x7F: {  # Sequencer-Specific Meta-Event
        'length': _VLQ,
        'bytes': {
            _VLQ: "Sequencer-Specific Meta-Event data",
            # See SYSTEM_EXCLUSIVE_MANUFACTURER_ID
            0: "Manufacturer ID (Single of first byte)",
            1: "Manufacturer ID (Second byte)",  # Only if byte 0 is 0x00!
            2: "Manufacturer ID (Third byte)",  # Only if byte 0 is 0x00!
            # Followed by Sequencer-Specific data
        }
    },
}

# Page 14 (PDF: 16)
_S_PER_MIN = 60
_S2MS = _MS2US = 1_000
_SMF_DEFAULT_TEMPO_BPM = 120
SMF_DEFAULT_TEMPO = _S_PER_MIN * _S2MS * _MS2US / _SMF_DEFAULT_TEMPO_BPM  # = 500_000 µs/qn


def compute_delta_time(delta_time: int, division: int, tempo: int = SMF_DEFAULT_TEMPO) -> datetime.timedelta:
    """Computes natural delta-time in milliseconds from MIDI delta-time expressed in ticks.
    
    :param delta_time: SMF Track Event delta-time (in ticks)
    :param division: SMF Header Chunk division (in delta ticks per quarter-note)
    :param tempo: SMF Track non-MIDI data Meta Event Tempo (in microseconds per quarter-note).
    Assumed to be 120 if not provided.
    :return: A time delta object.
    """
    return datetime.timedelta(milliseconds=delta_time * (tempo / division) / _MS2US)


# Inferred
SMF_DEFAULT_ENCODING = 'ASCII'

###
# MIDI SHOW CONTROL (MSC)
# v1.1.1
#
# Reference: RP-002/RP-014
###

# TODO!

###
# GENERAL MIDI SYSTEM LEVEL 1 (GM/GM1)
#
# Reference: MMA-00007/RP-003
###

GM1_MINIMUM_VOICES = 24
GM1_MINIMUM_MELODY_VOICES = 16
GM1_MINIMUM_PERCUSSION_VOICES = 8

GM1_PERCUSSION_CHANNEL = 10

GM1_MINIMUM_INSTRUMENTS = 128  # See: GM Sound Set
GM1_MINIMUM_PERCUSSION_SOUNDS = 47  # See: GM Percussion Map

GM1_REQUIRED_CONTROLLER_CHANGES = (
    1,  # Modulation
    7,  # Volume
    10,  # Pan
    11,  # Expression
    64,  # Sustain
    121,  # Reset All Controllers
    123  # All Notes Off
)

GM1_REQUIRED_REGISTERED_PARAMETER_NUMBERS = (
    0,  # Pitch Bend Sensitivity
    1,  # Fine Tuning
    2  # Coarse Tuning
)

GM1_REQUIRED_CHANNEL_MESSAGES = (
    0xD,  # Channel Pressure (Aftertouch)
    0xE  # Pitch Bend (default range = ±2 semitones)
)

GM1_DEFAULT_SETTINGS = {
    'bend': 0,
    'volume': 100,  # (0-127)
    'controllers': 'normal'
}

GENERAL_MIDI_SOUND_SET_GROUPINGS = {}
for group in (
        ((0, 8), "Piano"),
        ((8, 16), "Chromatic Percussion"),
        ((16, 24), "Organ"),
        ((24, 32), "Guitar"),
        ((33, 40), "Bass"),
        ((40, 48), "Strings"),
        ((48, 56), "Ensemble"),
        ((56, 64), "Brass"),
        ((64, 72), "Reed"),
        ((72, 80), "Pipe"),
        ((80, 88), "Synth Lead"),
        ((88, 96), "Synth Pad"),
        ((96, 104), "Synth Effects"),
        ((104, 112), "Ethnic"),
        ((112, 120), "Percussive"),
        ((120, 128), "Sound Effects"),
):
    for prog_num in range(*group[0]):
        GENERAL_MIDI_SOUND_SET_GROUPINGS[prog_num] = group[1]

GENERAL_MIDI_SOUND_SET = (
    "Acoustic Grand Piano",
    "Bright Acoustic Piano",
    "Electric Grand Piano",
    "Honky-tonk Piano",
    "Electric Piano 1",
    "Electric Piano 2",
    "Harpsichord",
    "Clavi",
    "Celesta",
    "Glockenspiel",
    "Music Box",
    "Vibraphone",
    "Marimba",
    "Xylophone",
    "Tubular Bells",
    "Dulcimer",
    "Drawbar Organ",
    "Percussive Organ",
    "Rock Organ",
    "Church Organ",
    "Reed Organ",
    "Accordion",
    "Harmonica",
    "Tango Accordion",
    "Acoustic Guitar (nylon",
    "Acoustic Guitar (steel)",
    "Electric Guitar (jazz)",
    "Electric Guitar (clean)",
    "Electric Guitar (muted",
    "Overdriven Guitar",
    "Distortion Guitar",
    "Guitar harmonics",
    "Acoustic Bass",
    "Electric Bass (finger)",
    "Electric Bass (pick)",
    "Fretless Bass",
    "Slap Bass 1",
    "Slap Bass 2",
    "Synth Bass 1",
    "Synth Bass 2",
    "Violin",
    "Viola",
    "Cello",
    "Contrabass",
    "Tremolo Strings",
    "Pizzicato Strings",
    "Orchestral Harp",
    "Timpani",
    "String Ensemble 1",
    "String Ensemble 2",
    "SynthStrings 1",
    "SynthStrings 2",
    "Choir Aahs",
    "Voice Oohs",
    "Synth Voice",
    "Orchestra Hit",
    "Trumpet",
    "Trombone",
    "Tuba",
    "Muted Trumpet",
    "French Horn",
    "Brass Section",
    "SynthBrass 1",
    "SynthBrass 2",
    "Soprano Sax",
    "Alto Sax",
    "Tenor Sax",
    "Baritone Sax",
    "Oboe",
    "English Horn",
    "Bassoon",
    "Clarinet",
    "Piccolo",
    "Flute",
    "Recorder",
    "Pan Flute",
    "Blown Bottle",
    "Shakuhachi",
    "Whistle",
    "Ocarina",
    "Lead 1 (square)",
    "Lead 2 (sawtooth)",
    "Lead 3 (calliope)",
    "Lead 4 (chiff)",
    "Lead 5 (charang)",
    "Lead 6 (voice)",
    "Lead 7 (fifths)",
    "Lead 8 (bass + lead)",
    "Pad 1 (new age)",
    "Pad 2 (warm)",
    "Pad 3 (polysynth)",
    "Pad 4 (choir)",
    "Pad 5 (bowed)",
    "Pad 6 (metallic)",
    "Pad 7 (halo)",
    "Pad 8 (sweep)",
    "FX 1 (rain)",
    "FX 2 (soundtrack)",
    "FX 3 (crystal)",
    "FX 4 (atmosphere)",
    "FX 5 (brightness)",
    "FX 6 (goblins)",
    "FX 7 (echoes)",
    "FX 8 (sci-fi)",
    "Sitar",
    "Banjo",
    "Shamisen",
    "Koto",
    "Kalimba",
    "Bag pipe",
    "Fiddle",
    "Shanai",
    "Tinkle Bell",
    "Agogo",
    "Steel Drums",
    "Woodblock",
    "Taiko Drum",
    "Melodic Tom",
    "Synth Drum",
    "Reverse Cymbal",
    "Guitar Fret Noise",
    "Breath Noise",
    "Seashore",
    "Bird Tweet",
    "Telephone Ring",
    "Helicopter",
    "Applause",
    "Gunshot",
)

GENERAL_MIDI_PERCUSSION_MAP = {  # Channel 10
    35: "Acoustic Bass Drum",
    36: "Bass Drum 1",
    37: "Side Stick",
    38: "Acoustic Snare",
    39: "Hand Clap",
    40: "Electric Snare",
    41: "Low Floor Tom",
    42: "Closed Hi Hat",
    43: "High Floor Tom",
    44: "Pedal Hi-Hat",
    45: "Low Tom",
    46: "Open Hi-Hat",
    47: "Low-Mid Tom",
    48: "Hi Mid Tom",
    49: "Crash Cymbal 1",
    50: "High Tom",
    51: "Ride Cymbal 1",
    52: "Chinese Cymbal",
    53: "Ride Bell",
    54: "Tambourine",
    55: "Splash Cymbal",
    56: "Cowbell",
    57: "Crash Cymbal 2",
    58: "Vibraslap",
    59: "Ride Cymbal 2",
    60: "Hi Bongo",
    61: "Low Bongo",
    62: "Mute Hi Conga",
    63: "Open Hi Conga",
    64: "Low Conga",
    65: "High Timbale",
    66: "Low Timbale",
    67: "High Agogo",
    68: "Low Agogo",
    69: "Cabasa",
    70: "Maracas",
    71: "Short Whistle",
    72: "Long Whistle",
    73: "Short Guiro",
    74: "Long Guiro",
    75: "Claves",
    76: "Hi Wood Block",
    77: "Low Wood Block",
    78: "Mute Cuica",
    79: "Open Cuica",
    80: "Mute Triangle",
    81: "Open Triangle",
}

###
# MIDI TIME CODE (MTC)
#
# Reference: MMA0001/RP-004/RP-008
###

# TODO!

###
# NOTATION INFORMATION
#
# Reference: RP-005, RP-006
# Integrated into v1.0 specification
###

# FIXME: original specification lost

# TODO!

###
# MASTER VOLUME & BALANCE
#
# Reference: RP-007
# Integrated into v1.0 specification
###

# FIXME: original specification lost

# TODO!

###
# RP-008
#
# See section: MIDI TIME CODE (MTC)
###

###
# FILE DUMP
#
# Reference: RP-009
# Integrated into v1.0 specification
###

# FIXME: original specification lost
# TODO!

###
# SOUND CONTROLLER DEFAULT
#
# Reference: RP-010
# Integrated into v1.0 specification
###

# FIXME: original specification lost
# TODO!

###
# RP-011
#
# Integrated into v1.0 specification
###

# FIXME: original specification lost

###
# MIDI TUNING STANDARD
#
# Reference: RP-012
# Integrated into v1.0 specification
###

# FIXME: original specification lost

###
# MIDI MACHINE CONTROL (MMC)
# v1.0
#
# Reference: MMA-0016/RP-013
###

# TODO!

###
# RP-014
#
# See section: MIDI Show Control
###

###
# RESPONSE TO RESET ALL CONTROLLERS
#
# Reference: RP-015
###

# TODO!

###
# DOWNLOADABLE SOUNDS LEVEL 1 (DLS/DLS1)
# v1.1b
#
# Reference: RP-016, MMA-0017
###

# TODO!

###
# SMF LYRICS EVENTS DEFINITION
#
# Reference: RP-017
# See section: STANDARD MIDI FILES (SMF)
###

SMF_TRACK_EVENT_META_EVENT_LYRIC_RECOMMENDED_FIRST_EVENT_POSITION = 0
# FIXME: [Upstream MMA specification] Title says "Line Return" while text refers to "Carriage Return".
SMF_TRACK_EVENT_META_EVENT_LYRIC_MAXIMUM_RECOMMENDED_LENGTH_BEFORE_RETURN = 40
SMF_TRACK_EVENT_META_EVENT_LYRIC_RESERVED_CHARACTERS = {  # Further defined in RP-027 (See below).
    '\\', '[', ']', '{', '}',
}

###
# DATA INCREMENT / DECREMENT CONTROLLER RECEPTION OPERATION
#
# Reference: RP-018
###

# TODO!

###
# SMF DEVICE & PROGRAM NAME
#
# Reference: RP-019a
# See section: STANDARD MIDI FILES (SMF)
###

SMF_TRACK_EVENT_META_EVENT_TYPES[0x09] = "Device Name"
SMF_TRACK_EVENT_META_EVENT_PARAMETERS[0x09] = {
    'length': _VLQ,
    'bytes': {
        _VLQ: "Name of the device that this track is intended to address",
    },
}
SMF_TRACK_EVENT_META_EVENT_TYPES[0x08] = "Program Name"
SMF_TRACK_EVENT_META_EVENT_PARAMETERS[0x08] = {
    'length': _VLQ,
    'bytes': {
        _VLQ: "Name of the program called up by the immediately following sequence of bank select "
              "and program change messages",
    },
}

###
# FILE REFERENCE SYSTEM EXCLUSIVE MESSAGE
#
# Reference: CA-018
###

# TODO!

###
# SAMPLE DUMP SIZE, RATE AND NAME EXTENSIONS
#
# Reference: CA-019
###

# TODO!

###
# GM-2 MIDI TUNING MESSAGES
#
# Reference: CA-020, CA-021, RP-020 (GM2)
###

# TODO!

###
# SOUND CONTROLLER DEFAULTS (Revised)
#
# Reference: RP-021
###

# FIXME: missing or integrated into main spec?

###
# Controller Destination Setting
#
# Reference: RP-022 (GM2)
###

# FIXME: missing or integrated into main spec?

###
# Control number 91/93 function name change
#
# Reference: RP-023
###

# FIXME: missing or integrated into main spec?

###
# CONTROLLER DESTINATION SETTING
#
# Reference: CA-022 (GM2)
###

# TODO!

###
# KEY-BASED INSTRUMENT CONTROLLERS
#
# Reference: CA-023 (GM2)
###

# TODO!

###
# GLOBAL PARAMETER CONTROL
#
# Reference: CA-024 (GM2)
###

# TODO!

###
# MASTER FINE/COARSE TUNING
#
# Reference: CA-025 (GM2)
###

# TODO!

###
# MODULATION DEPTH RANGE RPN
#
# Reference: CA-026 (GM2)
###

# TODO!

###
# GENERAL MIDI 2 SPECIFICATION
# v1.2a
#
# Reference: RP-024, RP-036, RP-037, RP-045
###

# TODO!

###
# GM System Level 2 SysEx Message
#
# Reference: CA-027
###

# TODO!

###
# DOWNLOADABLE SOUNDS LEVEL 2.2 (DLS2)
# v1.0
#
# Reference: RP-025
###

# TODO!

###
# SMF LANGUAGE & DISPLAY EXTENSIONS
#
# Reference: RP-026
# See section: STANDARD MIDI FILES (SMF)
###

SMF_TRACK_EVENT_META_EVENT_TYPES[0x05] = 'Lyric/Display'
SMF_TRACK_EVENT_META_LYRIC_DISPLAY_RESERVED_CHARACTERS = {
    # ASCII codes
    0x5B: 'Beginning of Ruby Tag',  # "["
    0x5C: "Prefix for Command Codes",  # "\"
    0x5D: "End of Ruby Tag",  # "]"

    0x7B: "With @ = Beginning of Language Tag, with # = Beginning of Song Information Tag",  # "{"
    0x7D: "End of Language @ or # Song Information Tag",
}
SMF_TRACK_EVENT_META_LYRIC_DISPLAY_COMMANDS = {
    'r': 0x0D,
    'n': 0x0A,
    't': 0x09,
    '\\': '\\',
    '{': '{',
    '}': '}',
    '[': '[',
    ']': ']'
}
SMF_TRACK_EVENT_META_LYRIC_DISPLAY_CODE_SETS = {
    'LATIN',  # ANSI
    'Latin',  # Same as "LATIN"
    'latin',  # Same as "LATIN"
    'JP',  # MS-Kanji (Shift-JIS)
    'Jp',  # Same as "JP"
    'jp'  # Same as "JP"
    # Warning: The Byte Order Mark (BOM) sets the code set to UNICODE despite not being declared here!
}

###
# MIDI MEDIA ADAPTATION LAYER FOR IEEE-1394
# v1.0
#
# Reference: RP-027
###

# TODO: Hardware!

###
# MIDI IMPLEMENTATION CHART
# V2.0
#
# Reference: RP-028
###

# TODO: Generator?
# See existing templates

###
# SMF/DLS bundle to RMID file
#
# Reference: RP-029
###

# TODO!

###
# XMF SPECIFICATION
#
# Reference: RP-030, RP-031, RP-032, RP-039, RP-040, RP-042, RP-043, RP-045, RP-047
###

# TODO!

###
# XMF PATCH PREFIX META EVENT
#
# Reference: RP-032a (XMF)
# See section: STANDARD MIDI FILES (SMF) RP-001
###

SMF_TRACK_EVENT_META_EVENT_TYPES[0x60] = "XMF Patch Type Prefix"
SMF_TRACK_EVENT_META_EVENT_PARAMETERS[0x60] = {
    'length': 1,
    'bytes': {
        0: "How to interpret subsequent Program Change and Bank Select Messages"
    },
    'values': {
        0x01: "General MIDI 1",
        0x02: "General MIDI 2",
        0x03: "DLS",
    },
}

###
# EXTENSION 00-01 TO FILE REFERENCE SYSEX MESSAGE
#
# Reference: CA-028, CA-018
###

# TODO!

###
# GENERAL MIDI LITE (GML)
# v1.0
#
# RP-033
###

# TODO!

###
# SCALABLE POLYPHONY MIDI SPECIFICATION
# v1.0b
#
# Reference: RP-034, RP-035
###

# TODO!

###
# MAXIMUM INSTANTANEOUS POLYPHONY (MIP)
#
# Reference: CA-029
###

# FIXME: Unavailable at MMA. Found at AMEI MSC.
# TODO!

###
# DEFAULT PAN CURVE
#
# Reference: RP-036 (GM2)
###

###
# No RP-038!
###

# FIXME: Unavailable at MMA & AMEI MSC.

###
# MOBILE DLS SPECIFICATION
# v1.0a
#
# Reference: RP-041 (DLS)
###

# FIXME: AMEI MSC. version is password protected! MMA has a "public" version.
# TODO!

###
# MOBILE PHONE CONTROL MESSAGE
#
# Reference: RP-046, CA-030
###

# TODO!

###
# MOBILE MUSICAL INTERFACE SPECIFICATION
# v1.0.6
#
# Reference: RP-048
###

# TODO!

###
# CC#88 HIGH RESOLUTION VELOCITY PREFIX
#
# Reference: CA-031
###

# TODO!

###
# THREE DIMENSIONAL SOUND CONTROLLER
#
# Reference: RP-049
###

# FIXME: Unavailable at MMA. Found at AMEI MSC.
# TODO!

###
# MIDI VISUAL CONTROL (MVC)
# v1.0
#
# Reference: CA-032, RP-050
###

# TODO!

###
# International Standard MIDI Code (ISMC) (MIDI Watermark)
#
# Reference: RP-051
###

# FIXME: Unavailable at MMA. Found at AMEI MSC.
# TODO!

###
# MIDI 1.0 Electrical Specification Update
#
# Reference: CA-033
###

# TODO: Hardware!

###
# SPECIFICATION FOR MIDI OVER BLUETOOTH LOW ENERGY (BLE-MIDI)
# v1.0
#
# Reference: RP-052
###

# TODO: Hardware!

###
# MIDI POLYPHONIC EXPRESSION (MPE)
# v1.1
#
# Reference: RP-053, CA-034, M1-100-UM
###

# TODO!

###
# MIDI CAPABILITY INQUIRY (MIDI-CI)
#
# Reference: CA-035
###

# TODO!

###
# SPECIFICATION FOR USE OF TRS CONNECTORS WITH MIDI DEVICES
#
# Reference: RP-054
###

# TODO: Hardware!


############
# Template #
############

###
# TITLE
#
# Reference: Specification ID
# See section: Specification section modified
###

# TODO!


#########
# Tests #
#########

if __name__ == '__main__':
    import logging
    from pprint import pformat

    logging.basicConfig(level=logging.DEBUG)

    assert SMF_DEFAULT_TEMPO == 500_000  # us/qn <=> 120 BPM

    # Check monkey patching works
    logging.debug("SMF_TRACK_EVENT_META_EVENT_TYPES=%s", pformat(SMF_TRACK_EVENT_META_EVENT_TYPES))
    logging.debug("SMF_TRACK_EVENT_META_EVENT_PARAMETERS=%s", pformat(SMF_TRACK_EVENT_META_EVENT_PARAMETERS))
