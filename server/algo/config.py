"""
Copyright 2017, MachineHeads
Author: Maria Sandrikova
Description: Config for trips generation
"""
import os

WORKING_DIR = os.path.dirname(__file__)

DATA_DIR = os.path.join(WORKING_DIR, 'data')

MIN_DAYS_BEFORE_TRIP = 20
MAX_DAYS_BEFORE_TRIP = 180

GAP_BEFORE_EVENT = 1
GAP_AFTER_EVENT = 4
