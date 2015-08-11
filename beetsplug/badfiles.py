#!/usr/bin/python
# coding=utf-8

# Base Python File (badfiles.py)
# Created: Tue 11 Aug 2015 10:46:34 PM CEST
# Version: 1.0
#
# This Python script was developped by François-Xavier Thomas.
# You are free to copy, adapt or modify it.
# If you do so, however, leave my name somewhere in the credits, I'd appreciate it ;)
#
# (ɔ) François-Xavier Thomas <fx.thomas@gmail.com>

from beets.plugins import BeetsPlugin
from beets.ui import Subcommand
from beets.util import displayable_path
from beets import ui
from subprocess import check_output, CalledProcessError, list2cmdline, STDOUT
import shlex
import os

class BadFiles(BeetsPlugin):

    def check_bad(self, lib, opts, args):
        command_by_ext = self.config['commands'].get()
        for item in lib.items(args):

            # First check if the path exists. If not, should run 'beets update'
            # to cleanup your library.
            dpath = displayable_path(item.path)
            self._log.debug(u"checking path: %s" % dpath)
            if not os.path.exists(item.path):
                ui.print_(u"%s: file does not exist" % dpath)

            # Find a command in the 'commands' dictionary in the plugin
            # configuration. If that command is not defined, go to the next
            # file.
            ext = os.path.splitext(item.path)[1][1:]
            cmd = command_by_ext.get(ext)
            self._log.debug(u"command for extension %s: %s" % (ext, cmd))
            if not cmd:
                continue

            # Add the path to the music file at the end of the check command,
            # run it, then display the results.
            cmd = shlex.split(cmd)
            cmd.append(item.path)
            self._log.debug(u"final command: %s" % displayable_path(list2cmdline(cmd)))
            try:
                check_output(cmd, stderr=STDOUT)
            except CalledProcessError as e:
                ui.print_(u"%s: command exited with status %s" % (dpath, e.returncode))
                for line in e.output.split("\n"):
                    if not line:
                        continue
                    ui.print_(u"  %s" % line)
            else:
                ui.print_(u"%s: ok" % dpath)

    def commands(self):
        bad_command = Subcommand('bad', help='check for corrupt or missing files')
        bad_command.func = self.check_bad
        return [bad_command]
