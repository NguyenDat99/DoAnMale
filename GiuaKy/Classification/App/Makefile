all:
	python3 setup.py build_ext --inplace
	rm *.c
	rm ../BUS/*.c
	rm ../DAO/*.c
	rm ../DTO/*.c
	python3 index.py
	rm -rf build
	rm *.so
