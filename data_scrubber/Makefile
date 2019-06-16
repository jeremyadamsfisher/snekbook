run:
	snakemake -j
thumb:
	python thumbgen.py
clean:
	rm ./snake_db_*
regen: clean thumb run