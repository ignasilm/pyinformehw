@echo off
cmd /u /c .\scripts\generarInformeHW.cmd USB
cmd /u /c .\scripts\cpu_benchmark.cmd USB

timeout /T 10