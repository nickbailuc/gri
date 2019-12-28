#!/bin/bash

##  Author = "Nick Bailuc"
##  Copyright = "Copyright (C) 2019 Nick Bailuc, <nick.bailuc@gmail.com>"
##  License = "GNU General Public License, version 3 or later"
##  version = "1.00-bash"
##
##
##  "Generator of Recurring Integers" (or "GRI")
##  is free software; you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation; either version 3 of the License, or
##  (at your option) any later version.
##
##  GRI is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.


echo Periodic integer
read x
echo Initiating place-value
read a
echo Terminating place-value
read b

k=$(printf $x | wc -m)

y=$a
z=$b

if [ $y == 0 ]
then
	printf "0"
else
	for ((i = 0; i < y; i++))
	do
		printf "$x"
	done
fi

printf "."

if [ $z == 0 ]
then
	printf "0"
else
	for ((i = 0; i < z; i++))
	do
		printf "$x"
	done
fi

echo
exit
