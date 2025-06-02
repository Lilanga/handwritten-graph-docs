# Makefile for Sphinx documentation (Windows compatible)

# Detect operating system
ifeq ($(OS),Windows_NT)
    # Windows-specific settings
    PYTHON       ?= python
    PIP          ?= pip
    SPHINXBUILD  ?= $(PYTHON) -m sphinx
    RM           = del /Q /F
    RMDIR        = rmdir /S /Q
    MKDIR        = mkdir
    SEP          = \\
else
    # Unix-like systems (Linux, macOS)
    PYTHON       ?= python3
    PIP          ?= pip3
    SPHINXBUILD  ?= sphinx-build
    RM           = rm -f
    RMDIR        = rm -rf
    MKDIR        = mkdir -p
    SEP          = /
endif

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SOURCEDIR    = .
BUILDDIR     = _build

# Custom variables you can override
SPHINXPORT   ?= 8080
SPHINXHOST   ?= 127.0.0.1
ALLSPHINXOPTS = -d $(BUILDDIR)$(SEP)doctrees $(SPHINXOPTS) $(SOURCEDIR)

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile clean livehtml typedoc html-with-typedoc dev prod linkcheck spelling doctest install setup check-deps

# Check if dependencies are installed
check-deps:
	@echo "Checking dependencies..."
	@$(PYTHON) --version || (echo "ERROR: Python not found. Please install Python." && exit 1)
	@$(PIP) --version || (echo "ERROR: pip not found. Please install pip." && exit 1)
	@$(PYTHON) -c "import sphinx; print('Sphinx version:', sphinx.__version__)" || (echo "ERROR: Sphinx not installed. Run 'make install' first." && exit 1)
	@echo "All dependencies are available!"

# Installation and setup
install:
	@echo "Installing Python dependencies..."
	$(PIP) install -r requirements.txt
	@echo "Checking for npm..."
	@npm --version >/dev/null 2>&1 && npm install || echo "npm not found - skipping Node.js dependencies"

setup: install check-deps
	@echo "Documentation environment setup complete!"

# Custom targets
clean:
ifeq ($(OS),Windows_NT)
	@if exist "$(BUILDDIR)" $(RMDIR) "$(BUILDDIR)" 2>nul || echo "Build directory already clean"
	@if exist "_static$(SEP)typedoc" $(RMDIR) "_static$(SEP)typedoc" 2>nul || echo "TypeDoc directory already clean"
else
	$(RMDIR) $(BUILDDIR)/* 2>/dev/null || true
	$(RMDIR) _static/typedoc/ 2>/dev/null || true
endif
	@echo "Build directory cleaned."

# HTML build with dependency check
html: check-deps
	@echo "Building HTML documentation..."
	@$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)$(SEP)html
	@echo "HTML documentation built in $(BUILDDIR)$(SEP)html$(SEP)"

# HTML build with warnings as errors (strict mode)
html-strict: check-deps
	@echo "Building HTML documentation in strict mode..."
	@$(SPHINXBUILD) -b html -W --keep-going $(ALLSPHINXOPTS) $(BUILDDIR)$(SEP)html

# HTML build with verbose output
html-verbose: check-deps
	@echo "Building HTML documentation with verbose output..."
	@$(SPHINXBUILD) -b html -v $(ALLSPHINXOPTS) $(BUILDDIR)$(SEP)html

# Live reload for development
livehtml: check-deps
	@echo "Starting live reload server on http://$(SPHINXHOST):$(SPHINXPORT)"
	@$(PYTHON) -c "import sphinx_autobuild" 2>/dev/null || (echo "Installing sphinx-autobuild..." && $(PIP) install sphinx-autobuild)
	$(PYTHON) -m sphinx_autobuild -b html $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)$(SEP)html --port $(SPHINXPORT) --host $(SPHINXHOST) --open-browser

# Generate TypeScript documentation
typedoc:
	@echo "Generating TypeScript documentation..."
	@npm --version >/dev/null 2>&1 || (echo "ERROR: npm not found. Please install Node.js." && exit 1)
	@npx typedoc --version >/dev/null 2>&1 || (echo "Installing typedoc..." && npm install -g typedoc)
	npx typedoc --out _static$(SEP)typedoc ..$(SEP)src --exclude "**$(SEP)*.test.ts" --exclude "*$(SEP)setupTests.ts" --exclude "*$(SEP)node_modules$(SEP)**"

# Build with TypeScript docs
html-with-typedoc: typedoc html
	@echo "HTML documentation with TypeScript API built successfully!"

# Quick development build
dev: clean livehtml

# Production build (clean + typedoc + strict HTML)
prod: clean typedoc html-strict
	@echo "Production documentation build complete!"

# Check for broken links
linkcheck: check-deps
	@echo "Checking for broken links..."
	@$(SPHINXBUILD) -M linkcheck "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Spell check (requires sphinxcontrib-spelling)
spelling: check-deps
	@echo "Running spell check..."
	@$(SPHINXBUILD) -M spelling "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Check for common documentation issues
doctest: check-deps
	@echo "Running doctests..."
	@$(SPHINXBUILD) -M doctest "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# PDF build (requires LaTeX)
pdf: check-deps
	@echo "Building PDF documentation..."
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# EPUB build
epub: check-deps
	@echo "Building EPUB documentation..."
	@$(SPHINXBUILD) -M epub "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Serve built documentation
serve:
	@echo "Serving documentation on http://$(SPHINXHOST):$(SPHINXPORT)"
ifeq ($(OS),Windows_NT)
	@cd $(BUILDDIR)$(SEP)html && $(PYTHON) -m http.server $(SPHINXPORT) --bind $(SPHINXHOST)
else
	@cd $(BUILDDIR)/html && $(PYTHON) -m http.server $(SPHINXPORT) --bind $(SPHINXHOST)
endif

# Show build info
info:
	@echo "Sphinx build information:"
	@echo "  Operating System: $(OS)"
	@echo "  SPHINXBUILD: $(SPHINXBUILD)"
	@echo "  SOURCEDIR:   $(SOURCEDIR)"
	@echo "  BUILDDIR:    $(BUILDDIR)"
	@echo "  SPHINXOPTS:  $(SPHINXOPTS)"
	@echo "  PYTHON:      $(PYTHON)"
	@echo "  PIP:         $(PIP)"

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile check-deps
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)