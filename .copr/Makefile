.PHONY: srpm
srpm:
	# Find the subdirectory from the source JSON if available
	$(eval SOURCE_JSON := $(shell cat .git/copr-source-json 2>/dev/null || echo '{}'))
	$(eval PARSED_SUBDIR := $(shell echo '$(SOURCE_JSON)' | grep -Po '"subdirectory"\s*:\s*"\K[^"]+'))
	
	# Use the parsed subdirectory or fallback to the command line argument
	$(eval ACTUAL_SUBDIR := $(or $(subdir),$(PARSED_SUBDIR)))
	
	@if [ -z "$(ACTUAL_SUBDIR)" ]; then \
		echo "Error: Could not determine subdirectory. Neither 'subdir' variable nor source JSON subdirectory found."; \
		exit 1; \
	fi
	
	@echo "Building SRPM from subdirectory: $(ACTUAL_SUBDIR)"
	
	# Delegate to the package-specific Makefile
	$(MAKE) -C $(ACTUAL_SUBDIR) -f .copr/Makefile srpm outdir="$(outdir)" spec="$(spec)"
