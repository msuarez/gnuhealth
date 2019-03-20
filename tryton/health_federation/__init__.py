# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2019 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2019 GNU Solidario <health@gnusolidario.org>
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
"""
health_federation package: HMIS Federation manager

This package is responsible to communicate the GNU Health HMIS 
with Thalamus, the Federation message server.

The main functionalities of the package are :
    * HMIS configuration to connect to Thalamus message server
    * Define the models that will participate on the Federation
    * Define which fields of each model will be shared on the Federation
    * Queue manager: Manages the local node queue to be sent to the Federation.
    * Defines the classes for each model and specific methods to interact
      with Thalamus
"""

from trytond.pool import Pool
from .health_federation import *


def register():
    Pool.register(
        FederationNodeConfig,
        FederationQueue,
        FederationObject,
        PartyFed,
        PoLFed,
        module='health_federation', type_='model')
