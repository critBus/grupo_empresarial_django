@echo
cd /D D:\TRABAJO\Aimara ISCA\entornos && pcharm\Scripts\activate.bat && cd /D D:\TRABAJO\Aimara ISCA\tesis && py manage.py migrate && py manage.py init_data && py manage.py runserver