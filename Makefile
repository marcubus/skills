SHELL := bash
PYTHON ?= python3
VERSION := $(shell cat VERSION)
TAG := v$(VERSION)

.PHONY: help check version tag

help: ## Show this help
	@grep -hE '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  %-10s %s\n", $$1, $$2}'

check: ## Run the repository checks (frontmatter, manifests, links, version, secrets)
	$(PYTHON) scripts/check.py
	bash -n scripts/install.sh

version: ## Print the CalVer version
	@echo $(VERSION)

tag: ## Create the annotated release tag from VERSION
	@if [[ -n "$$(git status --porcelain --untracked-files=no)" ]]; then \
		echo "working tree is dirty; commit first" >&2; exit 1; fi
	@if git rev-parse -q --verify "refs/tags/$(TAG)" >/dev/null; then \
		echo "tag $(TAG) already exists" >&2; exit 1; fi
	git tag -a "$(TAG)" -m "$(TAG)"
	@echo "created $(TAG); push with: git push origin main --follow-tags"
