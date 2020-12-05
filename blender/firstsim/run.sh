#!/bin/bash

blender --background test.blend --python scripts/modules/dodrop.py -- $1
