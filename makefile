# ===============================
# 🧰 Makefile (Windows friendly)
# Ubicación: backend/Makefile
# ===============================

# --- Variables ---
PY         := .\.venv\Scripts\python.exe
DJANGO     := $(PY) manage.py
UVICORN_M  := $(PY) -m uvicorn
BACKEND_PORT := 8000
NOTIFY_PORT  := 8081
NOTIFY_DIR   := ..\notification_service

.PHONY: help env install run-back run-notify run-all clean migrate superuser test clean-users

help:
	@echo.
	@echo Targets:
	@echo   make install        - Instala deps backend y notification_service
	@echo   make run-back       - Levanta Django en 127.0.0.1:$(BACKEND_PORT)
	@echo   make run-notify     - Levanta Notification Service en 127.0.0.1:$(NOTIFY_PORT)
	@echo   make run-all        - Levanta ambos (abre otra consola para notify)
	@echo   make clean          - Limpia __pycache__ y *.pyc/*.pyo (Windows)
	@echo   make migrate        - makemigrations + migrate
	@echo   make superuser      - Crea superusuario
	@echo   make test           - Ejecuta tests Django
	@echo   make clean-users    - Borra todos los usuarios (users.User)
	@echo.

# --- Entorno / deps ---
install:
	@echo Instalando dependencias del backend...
	@$(PY) -m pip install -r requirements.txt
	@echo Instalando dependencias del notification service...
	@pushd $(NOTIFY_DIR) && $(PY) -m pip install -r requirements.txt && popd

# --- Ejecución ---
run-back:
	@echo Iniciando Django en http://127.0.0.1:$(BACKEND_PORT)
	@$(DJANGO) runserver 127.0.0.1:$(BACKEND_PORT)

run-notify:
	@echo Iniciando Notification Service en http://127.0.0.1:$(NOTIFY_PORT)
	@pushd $(NOTIFY_DIR) && $(UVICORN_M) app.main:app --reload --port $(NOTIFY_PORT) && popd

run-all:
	@echo Levantando Django + Notification Service 🚀
	@echo --------------------------------------------
	@echo Backend (Django):      http://127.0.0.1:$(BACKEND_PORT)
	@echo Notification Service:  http://127.0.0.1:$(NOTIFY_PORT)
	@echo --------------------------------------------
	@start powershell -NoExit -Command "cd '$(NOTIFY_DIR)'; $(UVICORN_M) app.main:app --reload --port $(NOTIFY_PORT)"
	@$(DJANGO) runserver 127.0.0.1:$(BACKEND_PORT)

# --- Limpieza ---
clean:
	@echo Limpiando archivos temporales...
	@powershell -Command "Get-ChildItem -Recurse -Force -Include __pycache__ | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue"
	@powershell -Command "Get-ChildItem -Recurse -Force -Include *.pyc,*.pyo | Remove-Item -Force -ErrorAction SilentlyContinue"
	@echo ✅ Limpieza completada

# --- Migraciones / DB ---
migrate:
	@$(DJANGO) makemigrations
	@$(DJANGO) migrate

superuser:
	@$(DJANGO) createsuperuser

# --- Tests ---
test:
	@$(DJANGO) test -v 2

# --- Datos (helpers) ---
clean-users:
	@echo Borrando todos los usuarios del modelo users.User...
	@$(DJANGO) clear_users --yes
