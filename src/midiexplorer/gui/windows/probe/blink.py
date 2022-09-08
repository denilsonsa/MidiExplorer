# This Python file uses the following encoding: utf-8
#
# SPDX-FileCopyrightText: 2021-2022 Raphaël Doursenaud <rdoursenaud@free.fr>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Probe monitoring blinking buttons.
"""
import functools
import time

from dearpygui import dearpygui as dpg

from midiexplorer.gui.config import START_TIME, DEBUG


@functools.lru_cache()
def get_supported_indicators() -> list:
    """Cached list of supported indicators.

    :return: list of indicators.
    """
    mon_indicators = [
        'mon_c',
        'mon_s',
        'mon_note_off',
        'mon_note_on',
        'mon_polytouch',
        'mon_control_change',
        'mon_program_change',
        'mon_aftertouch',
        'mon_pitchwheel',
        'mon_sysex',
        'mon_quarter_frame',
        'mon_songpos',
        'mon_song_select',
        'mon_tune_request',
        'mon_end_of_exclusive',
        'mon_clock',
        'mon_start',
        'mon_continue',
        'mon_stop',
        'mon_active_sensing',
        'mon_reset'
    ]
    for channel in range(16):
        mon_indicators.append(f'mon_{channel}')
    for controller in range(128):
        mon_indicators.append(f'mon_cc_{controller}')
    if DEBUG:  # Experimental
        mon_indicators.append([
            'mon_undef1',
            'mon_undef2',
            'mon_undef3',
            'mon_undef4',
            'mon_all_sound_off',
            'mon_reset_all_controllers',
            'mon_local_control',
            'mon_all_notes_off',
            'mon_omni_off',
            'mon_omni_on',
            'mon_mono_on',
            'mon_poly_on'
        ])

    return mon_indicators


def _mon(indicator: int | str) -> None:
    """Illuminates an indicator in the monitor panel and prepare metadata for its lifetime management.

    :param indicator: Name of the indicator to blink

    """
    # logger = midiexplorer.gui.logger.Logger()
    # logger.log_debug(f"blink {indicator}")

    now = time.time() - START_TIME
    delay = dpg.get_value('mon_blink_duration')
    target = f'mon_{indicator}_active_until'
    until = now + delay
    dpg.set_value(target, until)
    theme = '__act'
    # EOX special case since we have two alternate representations.
    if indicator != 'end_of_exclusive':
        dpg.bind_item_theme(f'mon_{indicator}', theme)
    else:
        dpg.bind_item_theme(f'mon_{indicator}_common', theme)
        dpg.bind_item_theme(f'mon_{indicator}_syx', theme)
    # logger.log_debug(f"Current time:{time.time() - START_TIME}")
    # logger.log_debug(f"Blink {delay} until: {dpg.get_value(target)}")


def _note_on(number: int | str) -> None:
    """Illuminates the note.

    :param number: MIDI note number.

    """
    dpg.bind_item_theme(f'note_{number}', '__act')


def _note_off(number: int | str) -> None:
    """Darken the note.

    :param number: MIDI note number.

    """
    dpg.bind_item_theme(f'note_{number}', None)


def update_mon_status() -> None:
    """Handles monitor indicators blinking status update each frame.

    Checks for the time it should stay illuminated and darkens it if expired.

    """
    now = time.time() - START_TIME
    for indicator in get_supported_indicators():
        if dpg.get_value(f'{indicator}_active_until') < now:
            # EOX is a special case since we have two alternate representations.
            if indicator != 'mon_end_of_exclusive':
                dpg.bind_item_theme(f'{indicator}', None)
            else:
                dpg.bind_item_theme(f'{indicator}_common', None)
                dpg.bind_item_theme(f'{indicator}_syx', None)