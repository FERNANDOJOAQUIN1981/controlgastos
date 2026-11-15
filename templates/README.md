# Sistema de Control de Gastos (Flask + SQLite)

Aplicación web desarrollada en Python utilizando el microframework **Flask** y base de datos **SQLite** para el registro de gastos personales y generación de reportes descargables.

## Características y Funcionamiento
1. **Autenticación:** Pantalla de inicio de sesión protegida con sesiones de Flask (Credenciales por defecto: Usuario `admin` / Clave `123`).
2. **Registro de Gastos:** Formulario para ingresar fecha, descripción y monto, almacenando los datos automáticamente en una base de datos local `gastos.db`.
3. **Cálculo en Tiempo Real:** Suma automática del total de gastos acumulados en el panel principal.
4. **Generación de Reportes:** Botón dedicado para exportar todo el historial de gastos a un archivo `.csv` compatible con Excel.

## Capturas de Pantalla

### 1. Pantalla de Acceso (Login)
![Login](screenshots/login.png)

### 2. Panel Principal y Reporte
![Dashboard](screenshots/dashboard.png)

## Instalación y Ejecución Local
1. Clonar el repositorio:
   ```bash
   git clone https://github.com
   cd control-gastos-flask
   ```
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar la aplicación:
   ```bash
   python app.py
   ```
4. Abrir en el navegador: `http://127.0.0.1:5000`