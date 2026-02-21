# ============================================================
#  EPOQ — Developer Makefile
#  Run `make help` to see all available commands
# ============================================================

.PHONY: help install dev build clean

# Default target
help:
	@echo ""
	@echo "  EPOQ — Available Commands"
	@echo "  ========================="
	@echo "  make install      Install Node.js dependencies"
	@echo "  make dev          Start the development server"
	@echo "  make build        Build the production desktop app"
	@echo "  make clean        Remove build artifacts"
	@echo ""