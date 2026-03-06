@echo off
chcp 65001 > NUL
echo 正在啟動本機伺服器...
start /b python -m http.server 8000

echo 等待伺服器啟動...
timeout /t 1 /nobreak > NUL

echo 正在開啟瀏覽器...
start http://localhost:8000/gallery.html

echo.
echo 伺服器已在背景執行。
echo 若要結束伺服器，請關閉此命令提示字元視窗。
pause
