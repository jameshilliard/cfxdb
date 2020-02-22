# input .fbs files for schema
FBS_FILES=./cfxdb/*.fbs
FBS_OUTPUT=./cfxdb/gen

#FLATC=${HOME}/scm/3rdparty/flatbuffers/flatc
FLATC=/usr/local/bin/flatc

clean:
	-rm -rf ./.pytest_cache
	-rm -rf ./build
	-rm -rf ./dist
	-rm -rf ./*.egg-info
	-find . -type d -name "__pycache__" -exec rm -rf {} \;

install:
	pip install -e .

publish: clean
	python setup.py sdist bdist_wheel --universal
	twine upload dist/*


# flatbuffer schema processing / binding code generation
#
#
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
	touch $(FBS_OUTPUT)/__init__.py

	# FIXME: wrong import:
	# "from .oid_t import oid_t" => "from ..oid_t import oid_t"
	# "from .ObjRef import ObjRef" => "from ..ObjRef import ObjRef"
	find $(FBS_OUTPUT) -name "*.py" -exec sed -i'' 's/from .oid_t/from ..oid_t/g' {} \;


test_fbs:
	clear && make clean_fbs build_fbs && find crossbarfx/master/database/ && cloc crossbarfx/master/database/

test_database:
	clear && pytest -v -s crossbarfx/master/database/tests/test_user.py

test_database_single:
	pytest -v -s crossbarfx/master/database/tests/test_user.py::test_user_fbs_roundtrip

