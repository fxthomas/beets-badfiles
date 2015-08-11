#!/usr/bin/python
# coding=utf-8

# Base Python File (setup.py)
# Created: Tue 11 Aug 2015 11:56:11 PM CEST
# Version: 1.0
#
# This Python script was developped by François-Xavier Thomas.
# You are free to copy, adapt or modify it.
# If you do so, however, leave my name somewhere in the credits, I'd appreciate it ;)
#
# (ɔ) François-Xavier Thomas <fx.thomas@gmail.com>

from distutils.core import setup

setup(
    name="Badfiles",
    description="Badfiles - a beets plugin for finding corrupt and missing files",
    author="François-Xavier Thomas",
    author_email="",
    url="http://github.com/fxthomas/badfiles",
    packages=["beetsplug"],
)

