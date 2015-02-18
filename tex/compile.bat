@echo off
for /d %%a in (.\pythontex*) do rd %%a /q/s
pythontex %~f1
