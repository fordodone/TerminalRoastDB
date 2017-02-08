#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TerminalRoastDB, released under GPLv3
# Get_Roaster_State

import Pyro4

roast_control = Pyro4.Proxy("PYRONAME:roaster.sr700")
print (roast_control.output_current_state()[0:3])
