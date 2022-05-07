@echo off
set n=0
set end=114
copy %n%.ts out.ts
set num=%n%-%end%
:home
set /a n+=1
echo Y | copy /b out.ts+%n%.ts temp.ts && move /y temp.ts out.ts
if not %n%==%end% goto home
move /y out.ts out_%num%.mp4
del *.ts