# Quarto's sass cache lives under XDG_CACHE_HOME; ~/.cache is read-only
# in some environments, so keep the cache project-local.
export XDG_CACHE_HOME := $(CURDIR)/.cache

preview:
	quarto preview

render:
	quarto render

figs:
	python3 figs/makefigs.py
