# DaD packet sniffer

This scripts reads all the packets transmitted between the client and server, as well as decoded using proto templates datamined from the game

**THIS SCRIPT IS NOT MADE FOR CHEATS, EDUCATIONAL PURPOSES ONLY**

## How to launch

Just run ```py run.py``` in CMD and two windows will open with each having either server or client sided packets only

## Updating the protos

Although there is already both compiled and raw proto templates in the repository folder, if you want to update them:
* Delete the old pb2 and protos folders
* [Install protoc](https://stackoverflow.com/questions/13616033/install-protocol-buffers-on-windows)
* Add ```C:\Program Files\protoc\bin``` and ```C:\Program Files\protoc\include``` to the PATH (instance paths may vary depending on where you installed it)
* Drop a folder with .proto templates inside script folder(not the templates from protoc folder), and execute ```compile.bat```
* You should see pb2 folder containing files *_pb2.py

or like just wait for me to update it idk

## Respects to be paid
Spells and Guns DaD wiki discord: [https://discord.gg/CmNttKDSGD](https://discord.gg/CmNttKDSGD)

@ian.3 for creating the first version of the script

@bry.n, @kokkor, @z7272 for useful info regarding tcp / protobuf / game files
