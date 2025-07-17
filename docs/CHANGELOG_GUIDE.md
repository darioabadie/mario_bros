# Sistema de Changelog - Mario Bros Game

Este proyecto utiliza un sistema automatizado de changelog que ayuda a mantener un registro claro y organizado de todos los cambios realizados.

## 🎯 ¿Por qué usar un changelog?

- **Transparencia**: Cualquiera puede ver qué cambió y cuándo
- **Organización**: Mantiene un historial estructurado del desarrollo
- **Comunicación**: Facilita la comunicación entre desarrolladores
- **Releases**: Simplifica la preparación de nuevas versiones

## 📋 Estructura del Changelog

El changelog sigue el formato [Keep a Changelog](https://keepachangelog.com/) con estas secciones:

- **Added**: Nuevas funcionalidades
- **Changed**: Cambios en funcionalidades existentes  
- **Deprecated**: Funcionalidades que serán removidas
- **Removed**: Funcionalidades removidas
- **Fixed**: Corrección de bugs
- **Security**: Vulnerabilidades corregidas
- **Technical Details**: Detalles técnicos específicos

## 🛠️ Herramientas Disponibles

### 1. Script de Changelog (`tools/changelog.py`)

**Agregar nuevos cambios:**
```bash
# Agregar una nueva funcionalidad
python tools/changelog.py add Added "Sistema de power-ups implementado"

# Agregar un cambio con detalles técnicos
python tools/changelog.py add Fixed "Corregido bug en colisiones" "Mejorada detección AABB"

# Agregar cambio técnico
python tools/changelog.py add "Technical Details" "Refactorizado sistema de sprites"
```

**Ver cambios pendientes:**
```bash
python tools/changelog.py show
```

**Crear una nueva release:**
```bash
python tools/changelog.py release 0.3.0
```

### 2. Git Hooks Automatizados

**Instalar hooks:**
```bash
./tools/install-hooks.sh
```

**Hook pre-commit:**
- Verifica automáticamente que el changelog esté actualizado cuando haces commit
- Previene commits sin documentar cambios en código
- Te guía para actualizar el changelog si es necesario

## 🔄 Flujo de Trabajo Recomendado

### Para Cada Cambio de Código:

1. **Hacer cambios en el código**
2. **Documentar en changelog:**
   ```bash
   python tools/changelog.py add Added "Nueva funcionalidad X"
   ```
3. **Commit incluyendo changelog:**
   ```bash
   git add .
   git commit -m "feat: agregar funcionalidad X"
   ```

### Para Preparar una Release:

1. **Verificar cambios pendientes:**
   ```bash
   python tools/changelog.py show
   ```
2. **Crear la release:**
   ```bash
   python tools/changelog.py release 0.3.0
   ```
3. **Commit de la release:**
   ```bash
   git add CHANGELOG.md
   git commit -m "release: version 0.3.0"
   git tag v0.3.0
   ```

## 📝 Ejemplos de Uso

### Ejemplos de Entradas por Sección:

**Added (Nuevas funcionalidades):**
```bash
python tools/changelog.py add Added "Sistema de enemigos Koopa Troopa"
python tools/changelog.py add Added "Menú de pausa durante el juego"
python tools/changelog.py add Added "Sistema de guardado automático"
```

**Changed (Cambios):**
```bash
python tools/changelog.py add Changed "Mejorada velocidad de Mario"
python tools/changelog.py add Changed "Rediseñada interfaz de usuario"
```

**Fixed (Correcciones):**
```bash
python tools/changelog.py add Fixed "Corregido bug donde Mario atravesaba plataformas"
python tools/changelog.py add Fixed "Solucionado problema de audio en macOS"
```

**Technical Details (Detalles técnicos):**
```bash
python tools/changelog.py add "Technical Details" "Refactorizado sistema de colisiones para mejor performance"
python tools/changelog.py add "Technical Details" "Migrado sistema de sprites a arquitectura modular"
```

## 🎨 Formato de Mensajes de Commit

Se recomienda usar prefijos estándar en los commits:

- `feat:` - Nueva funcionalidad
- `fix:` - Corrección de bug
- `refactor:` - Refactorización de código
- `docs:` - Cambios en documentación
- `style:` - Cambios de formato (no afectan funcionalidad)
- `test:` - Agregar o modificar tests
- `chore:` - Tareas de mantenimiento

**Ejemplos:**
```bash
git commit -m "feat: agregar sistema de power-ups"
git commit -m "fix: corregir colisiones con enemigos"
git commit -m "refactor: modularizar sistema de sprites"
```

## 🔍 Verificación Automática

El hook pre-commit verificará:

- ✅ Si hay cambios en código (archivos .py, .js, .ts)
- ✅ Si CHANGELOG.md fue actualizado cuando hay cambios en código
- ✅ Mostrará los archivos que necesitan documentación
- ❌ Bloqueará el commit si falta documentar cambios

## 🚀 Beneficios del Sistema

1. **Historial Claro**: Siempre sabes qué cambió y cuándo
2. **Automatización**: Los hooks reducen errores humanos
3. **Consistencia**: Formato uniforme en toda la documentación
4. **Colaboración**: Facilita el trabajo en equipo
5. **Releases**: Preparación sencilla de nuevas versiones

## 📚 Recursos Adicionales

- [Keep a Changelog](https://keepachangelog.com/) - Guía del formato
- [Semantic Versioning](https://semver.org/) - Versionado semántico
- [Conventional Commits](https://www.conventionalcommits.org/) - Estándar de mensajes de commit

---

💡 **Tip**: Siempre documenta los cambios inmediatamente después de hacerlos, ¡así no se te olvida qué implementaste!
