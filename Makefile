.PHONY: install dev up analyze analyze-url write test threads clean help

# Default target
help:
	@echo "Commit Critic - Available commands:"
	@echo ""
	@echo "  make install      Install dependencies and package"
	@echo "  make dev          Start LangGraph dev server (for Studio/API)"
	@echo "  make up           Start LangGraph dev server on 0.0.0.0 (remote access)"
	@echo ""
	@echo "  make analyze      Analyze last 50 commits (CLI)"
	@echo "  make analyze-url  Analyze anthropic-cookbook repo (CLI)"
	@echo "  make write        Help write a commit message (CLI)"
	@echo "  make threads      List conversation threads (CLI)"
	@echo ""
	@echo "  make test         Run all CLI tests"
	@echo "  make clean        Clear thread history and temp files"

# Installation
install:
	pip install -r requirements.txt
	pip install -e .

# LangGraph Platform (Server/Studio)
dev:
	langgraph dev

up:
	langgraph dev --host 0.0.0.0

# CLI Commands (no server needed)
analyze:
	python commit_critic.py --analyze --limit 50

analyze-url:
	python commit_critic.py --analyze --url "https://github.com/anthropics/anthropic-cookbook" --limit 10

write:
	python commit_critic.py --write

threads:
	python commit_critic.py --threads

# Testing
test: test-local test-url
	@echo "All tests passed!"

test-local:
	@echo "Testing local analysis..."
	python commit_critic.py --analyze --limit 5 --quiet

test-url:
	@echo "Testing URL analysis..."
	python commit_critic.py --analyze --url "https://github.com/anthropics/anthropic-cookbook" --limit 3 --quiet

# Cleanup
clean:
	python commit_critic.py --clear-threads
	rm -rf /tmp/commit_critic_*
	rm -rf .langgraph_api/
	@echo "Cleaned up threads and temp files"
