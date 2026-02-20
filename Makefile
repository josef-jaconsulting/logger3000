install:
	pip install -r requirements.txt

doc:
	sphinx-gherkindoc -G glossary ./features ./docs/source/features
	$(MAKE) -C docs html
