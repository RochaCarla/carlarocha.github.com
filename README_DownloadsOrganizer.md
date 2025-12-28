# 🤖 Agente de IA para Organização de Downloads

Um agente inteligente que organiza automaticamente sua pasta de downloads usando técnicas de IA para categorização de arquivos.

## 🎯 Características

### IA Inteligente
- **Análise multi-fator**: Extensão, nome, tipo MIME, padrões
- **Aprendizado de padrões**: Reconhece convenções de nomenclatura
- **Confiança adaptável**: Só move arquivos com alta confiança
- **Categorização contextual**: Entende o contexto dos arquivos

### Organização Automática
- **10+ categorias**: Documentos, imagens, vídeos, código, etc.
- **Organização por data**: Para arquivos com baixa confiança
- **Prevenção de conflitos**: Renomeia automaticamente duplicatas
- **Estrutura visual**: Pastas com emojis para fácil identificação

### Segurança e Controle
- **Modo simulação**: Teste antes de mover arquivos
- **Logs detalhados**: Rastreamento completo das ações
- **Backup automático**: Opção de backup antes de mover
- **Configuração flexível**: Personalize categorias e regras

## 📦 Instalação

### Instalação Automática
```bash
# Tornar o script executável
chmod +x setup_organizer.sh

# Executar instalação
./setup_organizer.sh
```

### Instalação Manual
```bash
# Criar diretório
mkdir -p ~/.downloads_organizer

# Copiar arquivos
cp downloads_organizer.py ~/.downloads_organizer/
cp organizer_config.json ~/.downloads_organizer/

# Tornar executável
chmod +x ~/.downloads_organizer/downloads_organizer.py
```

## 🚀 Como Usar

### Comandos Básicos
```bash
# Teste (simulação - não move arquivos)
organize-downloads-dry

# Organização real
organize-downloads

# Com confiança personalizada
organize-downloads --confidence 0.7

# Pasta específica
organize-downloads --path /caminho/para/pasta
```

### Exemplos Práticos
```bash
# Primeira execução (recomendado)
python3 downloads_organizer.py --dry-run

# Organização conservadora (alta confiança)
python3 downloads_organizer.py --confidence 0.8

# Organização completa
python3 downloads_organizer.py --confidence 0.3
```

## 🎛️ Configuração

### Arquivo de Configuração
Edite `~/.downloads_organizer/organizer_config.json`:

```json
{
  "settings": {
    "downloads_path": "~/Downloads",
    "min_confidence": 0.3,
    "backup_before_move": true
  },
  "custom_categories": {
    "Pesquisa": {
      "extensions": [".pdf", ".doc"],
      "keywords": ["pesquisa", "paper", "artigo"],
      "folder": "🔬 Pesquisa Acadêmica"
    }
  }
}
```

### Categorias Padrão
- 📄 **Documentos**: PDF, DOC, TXT
- 📊 **Planilhas**: XLSX, CSV, ODS  
- 📽️ **Apresentações**: PPTX, PPT
- 🖼️ **Imagens**: JPG, PNG, GIF
- 🎥 **Vídeos**: MP4, AVI, MKV
- 🎵 **Áudio**: MP3, WAV, FLAC
- 📦 **Arquivos**: ZIP, RAR, 7Z
- 💻 **Código**: PY, JS, HTML
- 📚 **E-books**: EPUB, MOBI
- ⚙️ **Instaladores**: EXE, DMG, DEB

## 🔄 Automação

### Cron Job (Execução Automática)
```bash
# Editar crontab
crontab -e

# Executar a cada hora
0 * * * * ~/.downloads_organizer/auto_organize.sh

# Executar diariamente às 9h
0 9 * * * ~/.downloads_organizer/auto_organize.sh
```

### LaunchAgent (macOS)
Crie `~/Library/LaunchAgents/com.carlarocha.downloads-organizer.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.carlarocha.downloads-organizer</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/Users/carla/.downloads_organizer/downloads_organizer.py</string>
        <string>--confidence</string>
        <string>0.5</string>
    </array>
    <key>StartInterval</key>
    <integer>3600</integer>
</dict>
</plist>
```

## 📊 Relatórios

O agente gera relatórios detalhados:

```
==================================================
RELATÓRIO DE ORGANIZAÇÃO - DOWNLOADS
==================================================
Data: 17/01/2025 14:30
Arquivos processados: 45

ARQUIVOS POR CATEGORIA:
------------------------------
📄 Documentos: 12 arquivos
🖼️ Imagens: 8 arquivos
🎥 Vídeos: 5 arquivos
💻 Código: 3 arquivos
📦 Arquivos: 2 arquivos

ARQUIVOS COM BAIXA CONFIANÇA:
------------------------------
• arquivo_desconhecido.xyz (confiança: 0.25)
• temp_file.tmp (confiança: 0.10)
```

## 🛠️ Personalização

### Adicionar Nova Categoria
```python
# No arquivo de configuração
"MinhasNotas": {
    "extensions": [".md", ".txt"],
    "keywords": ["nota", "lembrete", "todo"],
    "folder": "📝 Minhas Notas"
}
```

### Padrões Personalizados
```python
# Adicionar padrões regex específicos
"patterns": {
    "Trabalho": [r"trabalho_\d+", r"projeto_[a-z]+"],
    "Pessoal": [r"foto_familia", r"viagem_\d{4}"]
}
```

## 🔍 Algoritmo de IA

### Fatores de Decisão
1. **Extensão do arquivo** (40% do peso)
2. **Palavras-chave no nome** (30% do peso)  
3. **Tipo MIME** (20% do peso)
4. **Padrões específicos** (10% do peso)

### Lógica de Confiança
- **≥ 0.8**: Alta confiança - move imediatamente
- **0.5-0.7**: Média confiança - move com log
- **0.3-0.4**: Baixa confiança - organiza por data
- **< 0.3**: Muito baixa - mantém na pasta original

## 📝 Logs

### Localização dos Logs
- **Log principal**: `~/Downloads/organizer.log`
- **Log automático**: `~/.downloads_organizer/auto_organize.log`
- **Relatórios**: `~/Downloads/_Organizados/relatorio_YYYYMMDD_HHMM.txt`

### Níveis de Log
- **INFO**: Operações normais
- **WARNING**: Situações que requerem atenção
- **ERROR**: Erros que impedem operação

## 🚨 Solução de Problemas

### Problemas Comuns

**Erro: "Pasta de downloads não encontrada"**
```bash
# Verificar caminho
ls ~/Downloads

# Especificar caminho manualmente
organize-downloads --path /caminho/correto
```

**Arquivos não sendo movidos**
```bash
# Verificar confiança
organize-downloads --confidence 0.1 --dry-run

# Ver logs detalhados
tail -f ~/Downloads/organizer.log
```

**Permissões negadas**
```bash
# Verificar permissões
ls -la ~/Downloads

# Corrigir permissões
chmod 755 ~/Downloads
```

## 🤝 Contribuição

### Melhorias Sugeridas
- [ ] Interface gráfica (GUI)
- [ ] Integração com serviços de nuvem
- [ ] Machine learning para padrões pessoais
- [ ] Suporte a mais formatos de arquivo
- [ ] Desfazer operações

### Como Contribuir
1. Fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.

## 👩‍💻 Autora

**Carla Rocha**
- Email: caguiar@unb.br
- GitHub: [@rochacarla](https://github.com/rochacarla)
- Site: [carlarocha.github.io](https://carlarocha.github.io)

---

*Desenvolvido com ❤️ para automatizar e organizar sua vida digital*
