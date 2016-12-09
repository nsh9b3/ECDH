To run their must be two parties that can talk to each other,

The first thing to explain is the config files
otherIpAddress is the ip Address you want to connect to and otherPort is the port used
(for a tcp connection)
then you have your ip address and the port they can use to connect to you(for tcp again)
after that is info for the curve, generator x and y are in hex form and 
are the coordinates of the generator for the group. a Val and b Val are parameters 
for y^2=x^2+ax+b, with b in hex form, fieldMod is the prime number group is modded by, 
and generatorMult is your secret used to generator shared secret generatorMult*GeneratorPoint

For two party communication
Now assuming you have the config file properly configured on both machines
(firt party uses firtPartyConfig.cfg and second party uses secondPartyConfig.cfg)
The first party must run firstPartyMain.py with python3
Then after first party program says outputs recieving to signify its ready to recieve data
the second party must run secondPartMain.py with python3
Assuming both machines have permission to communicate The diffie helman ellipctic curve
algorithm will now execute and the final output will be the shared secret point. To check
the results both parties should confirm they have the same final output

To mock two party configuration on one machine
simply properly set up config files as before(the ip address and port information isn't used)
and run mockTwoPartyMain with python 3. The curve parameters from firstPartyConfig are used
and the ones in secondPartyConfig are ignored.