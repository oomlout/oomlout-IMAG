@echo off
set IMAGdirectory=C:\GH\oomlout-IMAG\


set PRODDirectory=C:\DB\Dropbox\erpe\data\PROD-data\




REM
REM Generate Image Resolution Single
REM

	REM      Generate Directory Of Images
python %IMAGdirectory%IMAGmain.py -di %PRODDirectory% -re 140,420,1500 -ed gen\