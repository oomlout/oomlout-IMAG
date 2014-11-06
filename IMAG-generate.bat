@echo off
set IMAGdirectory=C:\GH\oomlout-IMAG\


set PRODDirectory=C:\DB\Dropbox\erpe\data\PROD-data\

set IMAGEName=LCDD-01_03
set id=ABUT-01-04


REM
REM Generate Image Resolution Single
REM

	REM      Generate Single Image
REM python %IMAGdirectory%IMAGmain.py -im %PRODDirectory%%IMAGEName% -re 140,420,1500

	REM      Generate Directory Of Images
python %IMAGdirectory%IMAGmain.py -di %PRODDirectory% -re 140,420,1500