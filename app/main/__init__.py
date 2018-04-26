#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 26/04/2018 7:26 PM
from flask import Blueprint

main = Blueprint("main", __name__)

from . import views