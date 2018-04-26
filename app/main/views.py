#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 26/04/2018 7:27 PM
from . import main


@main.route("/")
def index():
    return "Hello World from docker"
