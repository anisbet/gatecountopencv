####################################################
# Makefile for project deleteme 
# Created: Sat Oct 28 08:47:24 MDT 2017
#
#<one line to give the program's name and a brief idea of what it does.>
#    Copyright (C) 2017  Andrew Nisbet, Edmonton Public Library
# The Edmonton Public Library respectfully acknowledges that we sit on
# Treaty 6 territory, traditional lands of First Nations and Metis people.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
#
# Written by Andrew Nisbet at Edmonton Public Library
# Rev: 
#      0.0 - Dev. 
####################################################
# Change comment below for appropriate server.
PRODUCTION_SERVER=eplapp.library.ualberta.ca
TEST_SERVER=edpl-t.library.ualberta.ca
USER=sirsi
REMOTE=~/Unicorn/Bincustom/
LOCAL=~/projects/gatecountopencv/
APP=gatecountopencv.pl
ARGS=-x
.PHONY: put test production
put: test
	scp ${LOCAL}${APP} ${USER}@${TEST_SERVER}:${REMOTE}
	ssh ${USER}@${TEST_SERVER} '${REMOTE}${APP} ${ARGS}'
test:
	perl -c ${APP}
production: test
	scp ${LOCAL}${APP} ${USER}@${PRODUCTION_SERVER}:${REMOTE}
