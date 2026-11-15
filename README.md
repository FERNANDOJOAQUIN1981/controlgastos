# Sistema de Control de Gastos (Flask + SQLite)

Aplicación web desarrollada en **Python** con el microframework **Flask** y base de datos **SQLite** para el registro de gastos personales y generación de reportes descargables.

## Funcionamiento de la Aplicación
1. **Acceso al Sistema:** Pantalla de inicio de sesión protegida mediante sesiones de Flask.
   * **Usuario:** `admin`
   * **Contraseña:** `123`
2. **Registro de Gastos:** Formulario principal para ingresar la **fecha**, **descripción** y **monto** de cada gasto, guardando los registros en la base de datos local `gastos.db`.
3. **Cálculo Automático:** Muestra el historial completo en una tabla y calcula en tiempo real el total acumulado de los gastos.
4. **Generación de Reportes:** Permite exportar y descargar todo el historial registrado en un archivo de reporte (`.csv`).

## Capturas de Pantalla

### Panel Principal y Reporte

<img width="1348" height="534" alt="image" src="https://github.com/user-attachments/assets/c271a126-0615-4d32-aef5-027e301f3478" />
<img width="1345" height="435" alt="Captura 02" src="https://github.com/user-attachments/assets/6df74070-2a57-4a49-a3c1-607da8f01fba" />

