@echo off
rem datos de entrada
echo Se va realizar un informe del hardware del equipo.
rem echo '%1'
if [%1] == [USB] (
	set fileReport=info_%USERNAME%_%COMPUTERNAME%.txt
	echo Modo USB  
) else (
	set fileReport=%USERPROFILE%\Desktop\info_%USERNAME%_%COMPUTERNAME%.txt
	echo Modo Escritorio
)
echo.
echo.
echo Recopilando datos generales del sistema  
echo #COMPUTERSYSTEM# > %fileReport%
wmic COMPUTERSYSTEM GET Caption, Description, Manufacturer, Model, Name, NumberOfProcessors, PrimaryOwnerName, SystemType, UserName >> %fileReport%
echo Recopilando datos de la placa base
echo #BASEBOARD# >> %fileReport%
wmic BASEBOARD get Description, Manufacturer, Name, Product,SerialNumber,Version >> %fileReport%
echo Recopilando datos de la cpu
echo #CPU# >> %fileReport%
wmic CPU GET Caption, CurrentClockSpeed, Description, Manufacturer, MaxClockSpeed, Name, ProcessorId, SystemName, NumberOfCores, NumberOfEnabledCore, NumberOfLogicalProcessors >> %fileReport%
echo Recopilando datos de la memoria
echo #MEMPHYSICAL# >> %fileReport%
wmic MEMPHYSICAL GET MaxCapacity, MemoryDevices >> %fileReport%
echo #MEMORYCHIP# >> %fileReport%
wmic MEMORYCHIP GET Capacity,Description,DeviceLocator,Manufacturer,Name,PartNumber,PositionInRow,SerialNumber,Speed,Tag,TypeDetail >> %fileReport%
echo Recopilando datos del disco duro
echo #DISKDRIVE# >> %fileReport%
wmic DISKDRIVE GET Description,DeviceID,InterfaceType,Manufacturer,MediaType,Model,Name,SectorsPerTrack,Size,TotalCylinders,TotalHeads,TotalSectors,TotalTracks,TracksPerCylinder >> %fileReport%
echo #VOLUME# >> %fileReport%
wmic VOLUME Get DriveLetter,FileSystem,Label,Name,Capacity,FreeSpace,DriveType >> %fileReport%
echo.
echo.
echo.
echo Se ha finalizado de generar el informe %fileReport%
