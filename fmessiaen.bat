@echo off
REM Wrapper Windows : permet d'appeler "fmessiaen ..." depuis cmd / PowerShell
REM sans prefixer par "python". %~dp0 = dossier de ce .bat avec trailing \.
python "%~dp0fmessiaen" %*
