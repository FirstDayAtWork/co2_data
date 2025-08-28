:: cd countries && dir /b /A:-D > ../countries.txt
cd countries/ && for /F "delims= eol=" %%A IN ('dir /A-D /B') do echo %%~nA >> ../countries.txt