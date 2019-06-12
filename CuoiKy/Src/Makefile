All:
	cd Apps && clear && python3 setup.py build_ext --inplace
	cd Apps && rm *.c && rm ../BUS/*.c
	cd Apps && rm ../DAO/*.c && rm ../DTO/*.c
	cd Apps && clear && python3 index.py
	cd Apps && rm *.so && rm -rf build
	clear && echo "Tạm Biệt!"
