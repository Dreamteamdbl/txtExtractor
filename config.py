#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "28563361"))
    API_HASH = os.environ.get("API_HASH", "3255ae227ce20535c9230f8fd8b9e092")
    AUTH_USERS = os.environ.get("AUTH_USERS", "")
