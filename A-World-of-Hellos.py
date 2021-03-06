#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  A-World-of-Hellos.py
#  
#  Copyright 2013 Jonathan Casteel <iczesmv@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  version= 0.1.0
#  

source = "http://www.roesler-ac.de/wolfram/hello.htm"

hellos = {"ENGLISH":"Hello, World!", "SPANISH":"\u00a1Hola mundo!", 
"FRENCH":"Salut le Monde", "PORTUGUESE":"Ol\u00e1, mundo", "GERMAN":"Hallo Welt",
"ITALIAN":"Ciao Mondo"}

def main():
	while True:
		lang = input('In what language do you want your Hello World?:')
		lang = lang.upper() #makes input non-casesensitive
			
		if lang in hellos:
			hello = hellos[lang]
			print(hello)
		
		elif lang == "QUIT":
			break
		
		elif lang == "WHERE FROM?":
			print(source)
		
		else:
			print("Insert a different language.")
	
	return 0

if __name__ == '__main__': 
	main()
