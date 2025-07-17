#!/usr/bin/env python3
"""
Script helper para actualizar el CHANGELOG.md
Facilita agregar nuevas entradas y preparar releases.
"""

import sys
import os
from datetime import datetime
from typing import List, Tuple

class ChangelogManager:
    """Gestor para actualizar el changelog del proyecto"""
    
    def __init__(self, changelog_path: str = "CHANGELOG.md"):
        self.changelog_path = changelog_path
        self.sections = ["Added", "Changed", "Deprecated", "Removed", "Fixed", "Security", "Technical Details"]
    
    def add_entry(self, section: str, description: str, details: str = "") -> None:
        """
        Agrega una nueva entrada al changelog en la sección Unreleased.
        
        Args:
            section: Sección donde agregar (Added, Changed, etc.)
            description: Descripción del cambio
            details: Detalles técnicos adicionales (opcional)
        """
        if section not in self.sections:
            print(f"❌ Sección '{section}' no válida. Secciones disponibles: {', '.join(self.sections)}")
            return
        
        # Leer archivo actual
        try:
            with open(self.changelog_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"❌ No se encontró el archivo {self.changelog_path}")
            return
        
        # Buscar la sección Unreleased
        unreleased_start = content.find("## [Unreleased]")
        if unreleased_start == -1:
            print("❌ No se encontró la sección [Unreleased] en el changelog")
            return
        
        # Buscar la sección específica dentro de Unreleased
        section_header = f"### {section}"
        section_start = content.find(section_header, unreleased_start)
        
        if section_start == -1:
            # La sección no existe, agregarla
            next_section_start = self._find_next_section_in_unreleased(content, unreleased_start)
            if next_section_start == -1:
                # Agregar al final de Unreleased
                next_version_start = content.find("## [", unreleased_start + 1)
                if next_version_start == -1:
                    insert_pos = len(content)
                else:
                    insert_pos = next_version_start - 1
            else:
                insert_pos = next_section_start
            
            new_section = f"\n### {section}\n- {description}\n"
            if details:
                new_section += f"  - {details}\n"
        else:
            # La sección existe, agregar entrada
            section_end = content.find('\n\n', section_start)
            if section_end == -1:
                section_end = content.find('### ', section_start + 1)
                if section_end == -1:
                    section_end = content.find('## [', section_start + 1)
                    if section_end == -1:
                        section_end = len(content)
            
            # Encontrar la última línea de la sección
            last_line_end = content.rfind('\n', section_start, section_end)
            insert_pos = last_line_end + 1
            
            new_section = f"- {description}\n"
            if details:
                new_section += f"  - {details}\n"
        
        # Insertar la nueva entrada
        new_content = content[:insert_pos] + new_section + content[insert_pos:]
        
        # Escribir archivo actualizado
        with open(self.changelog_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Agregada entrada en sección '{section}': {description}")
    
    def _find_next_section_in_unreleased(self, content: str, unreleased_start: int) -> int:
        """Encuentra la siguiente sección dentro de Unreleased"""
        for section in self.sections:
            section_pos = content.find(f"### {section}", unreleased_start)
            if section_pos != -1:
                return section_pos
        return -1
    
    def create_release(self, version: str) -> None:
        """
        Convierte la sección Unreleased en una nueva versión.
        
        Args:
            version: Número de versión (ej: "0.3.0")
        """
        try:
            with open(self.changelog_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"❌ No se encontró el archivo {self.changelog_path}")
            return
        
        # Obtener fecha actual
        today = datetime.now().strftime("%Y-%m-%d")
        
        # Reemplazar [Unreleased] con la versión y fecha
        old_unreleased = "## [Unreleased]"
        new_version = f"## [Unreleased]\n\n## [{version}] - {today}"
        
        new_content = content.replace(old_unreleased, new_version, 1)
        
        # Escribir archivo actualizado
        with open(self.changelog_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Creada release {version} con fecha {today}")
        print(f"💡 No olvides hacer commit: git add CHANGELOG.md && git commit -m 'Release {version}'")
    
    def show_unreleased(self) -> None:
        """Muestra los cambios pendientes en Unreleased"""
        try:
            with open(self.changelog_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"❌ No se encontró el archivo {self.changelog_path}")
            return
        
        unreleased_start = content.find("## [Unreleased]")
        if unreleased_start == -1:
            print("❌ No se encontró la sección [Unreleased]")
            return
        
        next_version_start = content.find("## [", unreleased_start + 1)
        if next_version_start == -1:
            unreleased_content = content[unreleased_start:]
        else:
            unreleased_content = content[unreleased_start:next_version_start]
        
        print("📋 Cambios pendientes (Unreleased):")
        print("=" * 50)
        print(unreleased_content.strip())

def main():
    """Función principal del script"""
    manager = ChangelogManager()
    
    if len(sys.argv) < 2:
        print("🔧 Changelog Manager - Mario Bros Game")
        print("\nUso:")
        print("  python tools/changelog.py add <sección> \"<descripción>\" [\"detalles\"]")
        print("  python tools/changelog.py release <versión>")
        print("  python tools/changelog.py show")
        print("\nSecciones disponibles:")
        for section in manager.sections:
            print(f"  - {section}")
        print("\nEjemplos:")
        print("  python tools/changelog.py add Added \"Sistema de power-ups implementado\"")
        print("  python tools/changelog.py add Fixed \"Corregido bug en colisiones\" \"Mejorada detección AABB\"")
        print("  python tools/changelog.py release 0.3.0")
        print("  python tools/changelog.py show")
        return
    
    command = sys.argv[1]
    
    if command == "add":
        if len(sys.argv) < 4:
            print("❌ Uso: add <sección> \"<descripción>\" [\"detalles\"]")
            return
        
        section = sys.argv[2]
        description = sys.argv[3]
        details = sys.argv[4] if len(sys.argv) > 4 else ""
        
        manager.add_entry(section, description, details)
    
    elif command == "release":
        if len(sys.argv) < 3:
            print("❌ Uso: release <versión>")
            return
        
        version = sys.argv[2]
        manager.create_release(version)
    
    elif command == "show":
        manager.show_unreleased()
    
    else:
        print(f"❌ Comando '{command}' no reconocido")
        print("Comandos disponibles: add, release, show")

if __name__ == "__main__":
    main()
