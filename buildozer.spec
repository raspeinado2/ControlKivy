[app]
# Título y paquete de tu aplicación
title = ControlKivy
package.name = controlkivy
package.domain = org.example

# Incluye tu código Python y recursos
source.include_exts = py,png,jpg,kv

# Dependencias
requirements = python3,kivy

# Orientación y permisos (añade permisos bluetooth si los llegas a necesitar)
orientation = portrait
# android.permissions = BLUETOOTH,BLUETOOTH_ADMIN

# Ajustes de compilación
log_level = 2
warn_on_root = 1

# (Opcional) icono
# icon.filename = icon.png

# FIXME: Buildozer instalará la versión de SDK/NDK que necesite automáticamente
