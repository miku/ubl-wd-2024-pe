SHELL := /bin/bash

model.pkl:
	time python buildmodel.py
	#
# time python buildmodel.py # "L"
#
# real    1m29.320s
# user    1m25.075s
# sys     0m4.217s

.PHONY: generate
generate:
	python gentext.py

.PHONY: clean
clean:
	rm -f model.pkl

gutenberg-dammit-files-v002.zip:
	# https://github.com/aparrish/gutenberg-dammit/?tab=readme-ov-file
	wget http://static.decontextualize.com/gutenberg-dammit-files-v002.zip

corpus-l.txt: gutenberg-dammit-files-v002.zip
	time unzip -p gutenberg-dammit-files-v002.zip '*.txt' | head -2500000 > corpus-l.txt
