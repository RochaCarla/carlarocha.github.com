#!/bin/bash

# Setup do Agente de IA para Organização de Downloads
# Autor: Carla Rocha
# Data: 2025-01-17

echo "🤖 Configurando Agente de IA para Organização de Downloads"
echo "=========================================================="

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Por favor, instale Python 3."
    exit 1
fi

echo "✅ Python 3 encontrado"

# Criar diretório do organizador
ORGANIZER_DIR="$HOME/.downloads_organizer"
mkdir -p "$ORGANIZER_DIR"

# Copiar arquivos
cp downloads_organizer.py "$ORGANIZER_DIR/"
cp organizer_config.json "$ORGANIZER_DIR/"

# Tornar executável
chmod +x "$ORGANIZER_DIR/downloads_organizer.py"

echo "✅ Arquivos copiados para $ORGANIZER_DIR"

# Criar alias para facilitar uso
SHELL_RC=""
if [[ "$SHELL" == *"zsh"* ]]; then
    SHELL_RC="$HOME/.zshrc"
elif [[ "$SHELL" == *"bash"* ]]; then
    SHELL_RC="$HOME/.bashrc"
fi

if [[ -n "$SHELL_RC" ]]; then
    echo "" >> "$SHELL_RC"
    echo "# Agente de IA para Organização de Downloads" >> "$SHELL_RC"
    echo "alias organize-downloads='python3 $ORGANIZER_DIR/downloads_organizer.py'" >> "$SHELL_RC"
    echo "alias organize-downloads-dry='python3 $ORGANIZER_DIR/downloads_organizer.py --dry-run'" >> "$SHELL_RC"
    echo "✅ Aliases adicionados ao $SHELL_RC"
fi

# Criar script de automação (cron)
CRON_SCRIPT="$ORGANIZER_DIR/auto_organize.sh"
cat > "$CRON_SCRIPT" << 'EOF'
#!/bin/bash
# Auto-organização de downloads
cd "$HOME/.downloads_organizer"
python3 downloads_organizer.py --confidence 0.5 >> "$HOME/.downloads_organizer/auto_organize.log" 2>&1
EOF

chmod +x "$CRON_SCRIPT"

echo "✅ Script de automação criado"

# Instruções finais
echo ""
echo "🎉 Instalação concluída!"
echo ""
echo "Como usar:"
echo "----------"
echo "1. Teste primeiro (simulação):"
echo "   organize-downloads-dry"
echo ""
echo "2. Executar organização:"
echo "   organize-downloads"
echo ""
echo "3. Com configurações personalizadas:"
echo "   organize-downloads --confidence 0.7"
echo ""
echo "4. Para automação (executar a cada hora):"
echo "   crontab -e"
echo "   Adicione: 0 * * * * $ORGANIZER_DIR/auto_organize.sh"
echo ""
echo "Arquivos de configuração em: $ORGANIZER_DIR"
echo ""
echo "⚠️  IMPORTANTE: Reinicie o terminal para usar os aliases!"
