#!/bin/bash
# Script para instalar git hooks personalizados

echo "🔧 Instalando git hooks para Mario Bros Game..."

# Verificar que estamos en un repositorio git
if [ ! -d ".git" ]; then
    echo "❌ Error: No estás en un repositorio git"
    exit 1
fi

# Crear directorio de hooks de git si no existe
mkdir -p .git/hooks

# Instalar pre-commit hook
if [ -f ".githooks/pre-commit" ]; then
    cp .githooks/pre-commit .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit
    echo "✅ Hook pre-commit instalado"
else
    echo "❌ Error: No se encontró .githooks/pre-commit"
    exit 1
fi

echo ""
echo "🎉 Git hooks instalados correctamente!"
echo ""
echo "📋 Hooks activos:"
echo "  - pre-commit: Verifica que el changelog esté actualizado"
echo ""
echo "💡 Uso del sistema de changelog:"
echo "  - Agregar cambio: python tools/changelog.py add Added \"Nueva funcionalidad\""
echo "  - Ver pendientes: python tools/changelog.py show"
echo "  - Crear release: python tools/changelog.py release 0.3.0"
echo ""
echo "🔄 El hook pre-commit verificará automáticamente que documentes tus cambios"
