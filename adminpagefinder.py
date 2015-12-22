# adminpagefinder.py
#
# Copyright (C) 2010 -  Wei-Ning Huang (AZ) <aitjcize@gmail.com>
# All Rights reserved.
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
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#


from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import sys

def AdminPage():
	try: f = open("pages.txt","r")
	except IOError:
		print('File Not Found!')
	except OSError as err:
		print("OS error: {0}".format(err))
	else:
		link = input("Enter Website Address For eg. : example.com or www.example.com \n\n  URL : ")
		while link == "":
			print ("\n"*100)
			print ("Please Enter a Valid Website Address\n")
			link = input("Enter Website Address For eg. : example.com or www.example.com \n\n  URL : ")
			
		
		print ("\n\nAvilable Admin Pages : \n")
		slno = 1
		while True:
			end_link = f.readline()
			if not end_link:
				break
			req_link = "http://"+link+"/"+end_link
			req = Request(req_link)
			try:
				response = urlopen(req)
			except HTTPError as e:
				continue
			except URLError as e:
				continue
			else:
				print (" ", slno, " => ",req_link)
				slno = slno+1
			
			
AdminPage()
