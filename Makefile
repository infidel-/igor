all: clean main

main:
	python3 test.py

play:
	python3 test.py -i

clean:
