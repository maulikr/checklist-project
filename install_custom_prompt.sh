#!/bin/bash
# ------------------------------------------------------------------
# install_custom_prompt.sh
# Appends a custom fancy PS1 setup to ~/.bashrc (if not already added)
# ------------------------------------------------------------------

BASHRC="$HOME/.bashrc"
MARKER="# --- Fancy Prompt Setup (Optimized for light/dark backgrounds) ---"

# Check if the prompt is already present
if grep -q "$MARKER" "$BASHRC"; then
    echo "✅ Custom prompt already exists in ~/.bashrc. Skipping..."
    exit 0
fi

# Append the custom prompt block
cat <<'EOF' >> "$BASHRC"

# --- Fancy Prompt Setup (Optimized for light/dark backgrounds) ---

# Git branch parser
parse_git_branch() {
    git rev-parse --abbrev-ref HEAD 2>/dev/null
}

# Show virtual environment name (if active)
show_venv() {
    if [[ -n "\$VIRTUAL_ENV" ]]; then
        echo "(\$(basename "\$VIRTUAL_ENV"))"
    fi
}

# ANSI colors - optimized for both light and dark backgrounds
DARK_BLUE="\[\033[0;94m\]"      # Bright but not fluorescent blue
DARK_GREEN="\[\033[0;32m\]"     # Medium green
DARK_RED="\[\033[0;91m\]"       # Bright red (not fluorescent)
MAROON="\[\033[0;31m\]"         # Medium purple
DARK_GRAY="\[\033[0;90m\]"      # Dark gray
MEDIUM_GRAY="\[\033[0;37m\]"    # Medium gray
BOLD="\[\033[1m\]"
ITALIC="\[\033[3m\]"
RESET="\[\033[0m\]"

# Final PS1 - colors optimized for readability
export PS1="\${DARK_RED}\u\${RESET} \${MEDIUM_GRAY}@ \h\${RESET} \${DARK_BLUE}\w\${RESET} \${MAROON}\${ITALIC}\$(show_venv)\${RESET} \${BOLD}\${DARK_GREEN}\$(parse_git_branch)\${RESET} \${MEDIUM_GRAY}\\$\${RESET}"

# Function to restore custom PS1
restore_prompt() {
    export PS1="\${DARK_RED}\u\${RESET} \${MEDIUM_GRAY}@ \h\${RESET} \${DARK_BLUE}\w\${RESET} \${MAROON}\${ITALIC}\$(show_venv)\${RESET} \${BOLD}\${DARK_GREEN}\$(parse_git_branch)\${RESET} \${MEDIUM_GRAY}\\$\${RESET}"
}

# Restore prompt after any command (this will override virtualenv's PS1 changes)
PROMPT_COMMAND="restore_prompt"

EOF

echo "✨ Custom fancy prompt appended to ~/.bashrc!"
echo "➡️ Run 'source ~/.bashrc' to activate it now."
