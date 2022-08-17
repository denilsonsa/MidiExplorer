# This Python file uses the following encoding: utf-8
#
# SPDX-FileCopyrightText: 2022 Raphaël Doursenaud <rdoursenaud@free.fr>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
About window layout and content.
"""
import platform
import sys
from typing import Any, Optional

import mido
from dearpygui import dearpygui as dpg

from gui.logger import Logger


def create() -> None:
    """
    Creates the about window.
    """
    with dpg.window(
            tag='about_win',
            label="About",
            modal=True,
            no_collapse=True,
            no_background=False,
            no_move=True,
            pos=(640, 0),
            autosize=True,
            show=False,
    ):
        midiexplorer_version = "DEV"  # TODO: Generate from setup
        logo_size = 128
        title_color = (0, 255, 255)  # Cyan
        text_indent = 50

        # ----
        # Logo
        # ----
        width, height, channels, data = dpg.load_image(f'icons/midiexplorer_{logo_size}.png')
        with dpg.texture_registry():
            dpg.add_static_texture(width, height, data, tag='logo')
        with dpg.drawlist(width=width, height=height):
            dpg.draw_image('logo', pmin=(0, 0), pmax=(width, height))

        # -----
        # Title
        # -----
        dpg.add_text("MIDI Explorer", color=title_color)
        dpg.add_text(f"Version {midiexplorer_version}.")
        dpg.add_text("Yet another MIDI monitor, analyzer, debugger and manipulation tool.")

        # ------
        # Author
        # ------
        dpg.add_text("Author", color=title_color)
        dpg.add_text(f"Raphaël Doursenaud")

        # -------
        # License
        # -------
        dpg.add_text("License", color=title_color)
        width, height, channels, data = dpg.load_image('icons/gplv3-or-later-sm.png')
        with dpg.texture_registry():
            dpg.add_static_texture(width, height, data, tag='gpl_logo')
        with dpg.drawlist(width=width, height=height):
            dpg.draw_image('gpl_logo', pmin=(0, 0), pmax=(width, height))
        dpg.add_text("Copyright ©2021-2022 Raphaël Doursenaud")
        dpg.add_text("""This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.""")
        dpg.add_separator()

        # -------
        # Credits
        # -------
        dpg.add_text("Credits", color=title_color)

        dpg.add_text(f"""Python {platform.python_version()}
Used under the terms of the PSF License Agreement.""",
                     bullet=True)

        dpg.add_text(f"""mido {mido.__version__}
Copyright (c) 2013-infinity Ole Martin Bjørndalen
Used under the terms of the MIT License.""",
                     bullet=True)
        dpg.add_text("""python-rtmidi
Copyright (c) 2012 - 2021 Christopher Arndt
Used under the terms of the MIT License.""",
                     indent=text_indent)
        dpg.add_text("""RtMidi
Copyright (c) 2003-2021 Gary P. Scavone
Used under the terms of the MIT License.""",
                     indent=text_indent)

        dpg.add_text(f"""Dear PyGui {dpg.get_dearpygui_version()}.
Copyright (c) 2021 Dear PyGui, LLC
Used under the terms of the MIT License.""",
                     bullet=True)
        dpg.add_text("""Dear ImGui
Copyright (c) 2014-2022 Omar Cornut
Used under the terms of the MIT License.""",
                     indent=text_indent)

        # -----
        # Fonts
        # -----
        dpg.add_text("Fonts", color=title_color)
        dpg.add_text("""Roboto and Roboto Mono
Copyright (c) 2015 The Roboto Project Authors
Used under the terms of the Apache License, Version 2.0.""",
                     bullet=True)

        # ------------
        # Logo & icons
        # ------------
        dpg.add_text("Logo and icons", color=title_color)
        dpg.add_text("Composite work based upon:")
        dpg.add_text("""MIDI Connector
Copyright Fred the Oyster
Used under the terms of the Creative Commons Attribution-Share Alike 4.0 International license.""",
                     bullet=True)
        dpg.add_text("""Steering wheel
Copyright Spider
Used under the terms of the Creative Commons Attribution 4.0 International license.""",
                     bullet=True)

        # ----------
        # Trademarks
        # ----------
        dpg.add_text("Trademarks", color=title_color)
        dpg.add_text("""MIDI is a trademark of the MIDI Manufacturers Association (MMA) in the United States of America.
This is not a registered trademark in the European Union and France where I reside.
Other trademarks are property of their respective owners and used fairly for descriptive and nominative purposes only.""")


def toggle(sender: int | str, app_data: Any, user_data: Optional[Any]) -> None:
    """
    Callback to toggle the about window visibility.

    :param sender: argument is used by DPG to inform the callback
                   which item triggered the callback by sending the tag
                   or 0 if trigger by the application.
    :param app_data: argument is used DPG to send information to the callback
                     i.e. the current value of most basic widgets.
    :param user_data: argument is Optionally used to pass your own python data into the function.
    """
    logger = Logger()

    # Debug
    logger.log_debug(f"Entering {sys._getframe().f_code.co_name}:")
    logger.log_debug(f"\tSender: {sender!r}")
    logger.log_debug(f"\tApp data: {app_data!r}")
    logger.log_debug(f"\tUser data: {user_data!r}")

    dpg.configure_item('about_win', show=not dpg.is_item_visible('about_win'))
