#!/bin/python

import sys
import bpy
import mydrop

mydrop.physics()
mydrop.sim()
mydrop.render(sys.argv[-1], end=True, samples=10)
