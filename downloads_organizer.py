#!/usr/bin/env python3
"""
Agente de IA para Organização de Downloads
==========================================

Este agente usa IA para categorizar e organizar automaticamente
arquivos na pasta de downloads baseado em:
- Tipo de arquivo
- Conteúdo do nome
- Data de criação
- Tamanho do arquivo

Autor: Carla Rocha
Data: 2025-01-17
"""

import os
import shutil
import json
import logging
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import mimetypes
import re

class DownloadsOrganizerAI:
    """Agente de IA para organizar pasta de downloads"""
    
    def __init__(self, downloads_path: str = None):
        """
        Inicializa o organizador
        
        Args:
            downloads_path: Caminho para pasta de downloads (padrão: ~/Downloads)
        """
        self.downloads_path = Path(downloads_path or Path.home() / "Downloads")
        self.organized_path = self.downloads_path / "_Organizados"
        
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.downloads_path / 'organizer.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        # Regras de categorização inteligente
        self.categories = {
            "Documentos": {
                "extensions": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],
                "keywords": ["documento", "relatorio", "artigo", "paper", "manual", "guia"],
                "folder": "📄 Documentos"
            },
            "Planilhas": {
                "extensions": [".xlsx", ".xls", ".csv", ".ods"],
                "keywords": ["planilha", "dados", "tabela", "excel"],
                "folder": "📊 Planilhas"
            },
            "Apresentações": {
                "extensions": [".pptx", ".ppt", ".odp"],
                "keywords": ["apresentacao", "slides", "powerpoint"],
                "folder": "📽️ Apresentações"
            },
            "Imagens": {
                "extensions": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
                "keywords": ["foto", "imagem", "screenshot", "captura"],
                "folder": "🖼️ Imagens"
            },
            "Videos": {
                "extensions": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv"],
                "keywords": ["video", "filme", "aula", "tutorial"],
                "folder": "🎥 Vídeos"
            },
            "Audio": {
                "extensions": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
                "keywords": ["audio", "musica", "podcast", "som"],
                "folder": "🎵 Áudio"
            },
            "Arquivos": {
                "extensions": [".zip", ".rar", ".7z", ".tar", ".gz"],
                "keywords": ["arquivo", "compactado", "backup"],
                "folder": "📦 Arquivos"
            },
            "Codigo": {
                "extensions": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c"],
                "keywords": ["codigo", "script", "programa", "source"],
                "folder": "💻 Código"
            },
            "Ebooks": {
                "extensions": [".epub", ".mobi", ".azw"],
                "keywords": ["ebook", "livro", "book"],
                "folder": "📚 E-books"
            },
            "Instaladores": {
                "extensions": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm"],
                "keywords": ["installer", "setup", "install"],
                "folder": "⚙️ Instaladores"
            }
        }
        
    def analyze_file(self, file_path: Path) -> Dict:
        """
        Analisa um arquivo usando IA para determinar categoria
        
        Args:
            file_path: Caminho do arquivo
            
        Returns:
            Dict com informações do arquivo
        """
        try:
            stats = file_path.stat()
            file_info = {
                "name": file_path.name,
                "extension": file_path.suffix.lower(),
                "size": stats.st_size,
                "created": datetime.fromtimestamp(stats.st_ctime),
                "modified": datetime.fromtimestamp(stats.st_mtime),
                "mime_type": mimetypes.guess_type(str(file_path))[0],
                "category": "Outros",
                "confidence": 0.0
            }
            
            # IA para categorização
            category, confidence = self._categorize_with_ai(file_info)
            file_info["category"] = category
            file_info["confidence"] = confidence
            
            return file_info
            
        except Exception as e:
            self.logger.error(f"Erro ao analisar {file_path}: {e}")
            return None
    
    def _categorize_with_ai(self, file_info: Dict) -> Tuple[str, float]:
        """
        Usa IA para categorizar arquivo baseado em múltiplos fatores
        
        Args:
            file_info: Informações do arquivo
            
        Returns:
            Tupla (categoria, confiança)
        """
        name_lower = file_info["name"].lower()
        extension = file_info["extension"]
        
        best_category = "Outros"
        best_confidence = 0.0
        
        for category, rules in self.categories.items():
            confidence = 0.0
            
            # Pontuação por extensão (peso 40%)
            if extension in rules["extensions"]:
                confidence += 0.4
            
            # Pontuação por palavras-chave no nome (peso 30%)
            keyword_matches = sum(1 for keyword in rules["keywords"] 
                                if keyword in name_lower)
            if keyword_matches > 0:
                confidence += 0.3 * min(keyword_matches / len(rules["keywords"]), 1.0)
            
            # Pontuação por tipo MIME (peso 20%)
            if file_info["mime_type"]:
                mime_category = file_info["mime_type"].split('/')[0]
                if (mime_category == "image" and category == "Imagens") or \
                   (mime_category == "video" and category == "Videos") or \
                   (mime_category == "audio" and category == "Audio") or \
                   (mime_category == "text" and category == "Documentos"):
                    confidence += 0.2
            
            # Pontuação por padrões específicos (peso 10%)
            confidence += self._pattern_bonus(name_lower, category) * 0.1
            
            if confidence > best_confidence:
                best_confidence = confidence
                best_category = category
        
        return best_category, best_confidence
    
    def _pattern_bonus(self, filename: str, category: str) -> float:
        """Bônus baseado em padrões específicos no nome do arquivo"""
        patterns = {
            "Documentos": [r"relat[oó]rio", r"documento", r"manual", r"guia"],
            "Imagens": [r"screenshot", r"captura", r"foto", r"img"],
            "Videos": [r"aula", r"tutorial", r"video", r"filme"],
            "Codigo": [r"source", r"src", r"project", r"codigo"],
            "Ebooks": [r"livro", r"book", r"ebook", r"manual"]
        }
        
        if category in patterns:
            matches = sum(1 for pattern in patterns[category] 
                         if re.search(pattern, filename))
            return min(matches / len(patterns[category]), 1.0)
        
        return 0.0
    
    def organize_by_date(self, file_info: Dict) -> str:
        """Organiza por data se necessário"""
        age_days = (datetime.now() - file_info["created"]).days
        
        if age_days <= 7:
            return "📅 Esta Semana"
        elif age_days <= 30:
            return "📅 Este Mês"
        elif age_days <= 90:
            return "📅 Últimos 3 Meses"
        else:
            return "📅 Antigos"
    
    def create_folder_structure(self):
        """Cria estrutura de pastas organizadas"""
        self.organized_path.mkdir(exist_ok=True)
        
        for category_info in self.categories.values():
            folder_path = self.organized_path / category_info["folder"]
            folder_path.mkdir(exist_ok=True)
        
        # Pastas especiais
        (self.organized_path / "📅 Esta Semana").mkdir(exist_ok=True)
        (self.organized_path / "📅 Este Mês").mkdir(exist_ok=True)
        (self.organized_path / "📅 Últimos 3 Meses").mkdir(exist_ok=True)
        (self.organized_path / "📅 Antigos").mkdir(exist_ok=True)
        (self.organized_path / "❓ Outros").mkdir(exist_ok=True)
    
    def move_file(self, file_path: Path, file_info: Dict, dry_run: bool = False):
        """
        Move arquivo para pasta apropriada
        
        Args:
            file_path: Caminho atual do arquivo
            file_info: Informações do arquivo
            dry_run: Se True, apenas simula o movimento
        """
        try:
            # Determinar pasta de destino
            if file_info["confidence"] >= 0.5:
                category_folder = self.categories[file_info["category"]]["folder"]
                dest_folder = self.organized_path / category_folder
            else:
                # Se confiança baixa, organizar por data
                dest_folder = self.organized_path / self.organize_by_date(file_info)
            
            dest_path = dest_folder / file_path.name
            
            # Evitar conflitos de nome
            counter = 1
            while dest_path.exists():
                name_parts = file_path.stem, counter, file_path.suffix
                dest_path = dest_folder / f"{name_parts[0]}_{name_parts[1]}{name_parts[2]}"
                counter += 1
            
            if dry_run:
                self.logger.info(f"[SIMULAÇÃO] {file_path.name} → {dest_folder.name}")
            else:
                shutil.move(str(file_path), str(dest_path))
                self.logger.info(f"Movido: {file_path.name} → {dest_folder.name}")
                
        except Exception as e:
            self.logger.error(f"Erro ao mover {file_path}: {e}")
    
    def generate_report(self, processed_files: List[Dict]) -> str:
        """Gera relatório da organização"""
        report = []
        report.append("=" * 50)
        report.append("RELATÓRIO DE ORGANIZAÇÃO - DOWNLOADS")
        report.append("=" * 50)
        report.append(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        report.append(f"Arquivos processados: {len(processed_files)}")
        report.append("")
        
        # Estatísticas por categoria
        category_stats = {}
        for file_info in processed_files:
            category = file_info["category"]
            category_stats[category] = category_stats.get(category, 0) + 1
        
        report.append("ARQUIVOS POR CATEGORIA:")
        report.append("-" * 30)
        for category, count in sorted(category_stats.items()):
            folder_name = self.categories.get(category, {}).get("folder", "❓ Outros")
            report.append(f"{folder_name}: {count} arquivos")
        
        report.append("")
        report.append("ARQUIVOS COM BAIXA CONFIANÇA:")
        report.append("-" * 30)
        low_confidence = [f for f in processed_files if f["confidence"] < 0.5]
        for file_info in low_confidence:
            report.append(f"• {file_info['name']} (confiança: {file_info['confidence']:.2f})")
        
        return "\n".join(report)
    
    def run(self, dry_run: bool = False, min_confidence: float = 0.3):
        """
        Executa a organização da pasta de downloads
        
        Args:
            dry_run: Se True, apenas simula sem mover arquivos
            min_confidence: Confiança mínima para mover arquivo
        """
        self.logger.info("🤖 Iniciando Agente de IA para Organização de Downloads")
        
        if not self.downloads_path.exists():
            self.logger.error(f"Pasta de downloads não encontrada: {self.downloads_path}")
            return
        
        # Criar estrutura de pastas
        if not dry_run:
            self.create_folder_structure()
        
        # Processar arquivos
        processed_files = []
        files_to_process = [f for f in self.downloads_path.iterdir() 
                          if f.is_file() and not f.name.startswith('.')]
        
        self.logger.info(f"Encontrados {len(files_to_process)} arquivos para processar")
        
        for file_path in files_to_process:
            # Pular arquivos do próprio organizador
            if file_path.name in ['organizer.log', 'downloads_organizer.py']:
                continue
                
            file_info = self.analyze_file(file_path)
            if file_info and file_info["confidence"] >= min_confidence:
                processed_files.append(file_info)
                self.move_file(file_path, file_info, dry_run)
            elif file_info:
                self.logger.info(f"Pulado (baixa confiança): {file_path.name} "
                               f"(confiança: {file_info['confidence']:.2f})")
        
        # Gerar relatório
        report = self.generate_report(processed_files)
        self.logger.info("\n" + report)
        
        # Salvar relatório
        if not dry_run:
            report_path = self.organized_path / f"relatorio_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report)
        
        self.logger.info("✅ Organização concluída!")


def main():
    """Função principal"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Agente de IA para Organização de Downloads")
    parser.add_argument("--path", type=str, help="Caminho para pasta de downloads")
    parser.add_argument("--dry-run", action="store_true", help="Apenas simular, não mover arquivos")
    parser.add_argument("--confidence", type=float, default=0.3, help="Confiança mínima (0.0-1.0)")
    
    args = parser.parse_args()
    
    organizer = DownloadsOrganizerAI(args.path)
    organizer.run(dry_run=args.dry_run, min_confidence=args.confidence)


if __name__ == "__main__":
    main()
