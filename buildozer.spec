[app]
# (Requerido) Nombre visible de tu aplicación
title = ControlKivy

# Nombre del paquete y dominio inverso
package.name = controlkivy
package.domain = org.example

# (Requerido) Directorio donde está tu código (el punto significa raíz del proyecto)
source.dir = .

# Extensiones de archivo que incluirá en la compilación
source.include_exts = py,png,jpg,kv

# (Requerido) Versión de tu app
version = 1.0

# Dependencias Python y Kivy
requirements = python3,kivy

# Orientación de la pantalla
orientation = portrait

# (Opcional) Ajustes de registro
log_level = 2
warn_on_root = 1

# ----------------------------------------
# Las siguientes secciones son opcionales
#
# (Opcional) Icono de la app
# icon.filename = icon.png
#
# (Opcional) Permisos Android
# android.permissions = INTERNET,BLUETOOTH,BLUETOOTH_ADMIN
#
# (Opcional) SDK y NDK específicos
# android.sdk = 24
# android.ndk = 23b
#
# (Opcional) Grado de optimización de la APK
# android.release = 1
#
# Fin de buildozer.spec
