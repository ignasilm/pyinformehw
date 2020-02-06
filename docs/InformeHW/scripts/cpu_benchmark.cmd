@echo off
echo.
echo.
echo Ejecutando benchmark de CPU, enseguida termina.
.\scripts\cpuz_x64 -bench
echo.
echo El benchmark ha terminado.
echo.
rem echo '%1'
if [%1] == [USB] (
	move .\scripts\%COMPUTERNAME%.txt .\benchmark_%COMPUTERNAME%_%date:~-4%-%date:~3,2%-%date:~-0,2%.txt
	echo Modo USB  
) else (
	move .\scripts\%COMPUTERNAME%.txt %UserProfile%\Desktop\benchmark_%COMPUTERNAME%_%date:~-4%-%date:~3,2%-%date:~-0,2%.txt
	echo Modo Escritorio
)
