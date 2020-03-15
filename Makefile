# input .fbs files for schema
FBS_FILES=./cfxdb/*.fbs
FBS_OUTPUT=./cfxdb/gen

#FLATC=${HOME}/scm/3rdparty/flatbuffers/flatc
FLATC=/usr/local/bin/flatc

build_flatc:
	cd /tmp
	wget https://github.com/google/flatbuffers/archive/v1.12.0.tar.gz
	tar xvf v1.12.0.tar.gz
	cd v1.12.0
	cmake .
	make
	sudo cp ./flatc $(FLATC)
	cd ..
	rm -rf v1.12.0 && rm v1.12.0.tar.gz

clean:
	-find . -type d -name "__pycache__" -exec rm -rf {} \;
	-rm -rf ./.pytest_cache
	-rm -rf ./build
	-rm -rf ./dist
	-rm -rf ./*.egg-info

install:
	pip install -e .

publish: clean
	python setup.py sdist bdist_wheel --universal
	twine upload dist/*


stats:
	@clear
	@find ./cfxdb -name "*.fbs" -exec grep -Hi "^table" {} \; | cut -d" " -f1,2 | sort
	@echo
	@wc -l cfxdb/*.fbs
	@echo
	@cloc cfxdb
	@echo

test:
	pytest -v -s ./cfxdb/tests/

test_single:
	pytest -v -s ./cfxdb/tests//test_user.py::test_user_fbs_roundtrip


# auto-format code - WARNING: this my change files, in-place!
autoformat:
	yapf -ri --style=yapf.ini \
		--exclude="cfxdb/gen/*" \
		cfxdb

# flatbuffer schema processing / binding code generation
flatc_version:
	$(FLATC) --version

clean_fbs:
	rm -rf $(FBS_OUTPUT)
	mkdir -p $(FBS_OUTPUT)

build_fbs: build_fbs_bfbs build_fbs_python

# generate schema type library (.bfbs binary) from schema files
build_fbs_bfbs:
	$(FLATC) -o $(FBS_OUTPUT) --binary --schema --bfbs-comments --bfbs-builtins $(FBS_FILES)

# generate python3 bindings from schema files
build_fbs_python:
	$(FLATC) -o $(FBS_OUTPUT) --python $(FBS_FILES)

	# those are not generated, but required
	#touch $(FBS_OUTPUT)/__init__.py

	# FIXME: wrong import:
	# "from .oid_t import oid_t" => "from ..oid_t import oid_t"
	# "from .ObjRef import ObjRef" => "from ..ObjRef import ObjRef"
	#find $(FBS_OUTPUT) -name "*.py" -exec sed -i'' 's/from .oid_t/from ..oid_t/g' {} \;
