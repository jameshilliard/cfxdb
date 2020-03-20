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
	@echo
	@find ./cfxdb -name "*.fbs" -exec grep -Hi "^table" {} \; | cut -d" " -f1,2 | sort
	@echo
	@find ./cfxdb -name "*.fbs" -exec grep -Hi "^enum" {} \; | cut -d" " -f1,2 | sort
	@echo
	@find ./cfxdb -name "*.fbs" -exec grep -Hi "^struct" {} \; | cut -d" " -f1,2 | sort
	@echo
	@wc -l cfxdb/*.fbs
	@echo
	@cloc cfxdb
	@echo

# list all basic table round-trip tests
list_tests:
	find ./cfxdb/tests/test_*.py -exec grep -Hi "def test_.*roundtrip(" {} \;

test:
	pytest -v -s ./cfxdb/tests/

test_xbr_roundtrip:
	pytest -v -s ./cfxdb/tests/test_xbr.py::test_actor_roundtrip
	pytest -v -s ./cfxdb/tests/test_xbr.py::test_member_roundtrip
	pytest -v -s ./cfxdb/tests/test_xbr.py::test_market_roundtrip
	pytest -v -s ./cfxdb/tests/test_xbr.py::test_token_transfer_roundtrip
	pytest -v -s ./cfxdb/tests/test_xbr.py::test_token_approval_roundtrip
	pytest -v -s ./cfxdb/tests/test_xbr.py::test_payment_channel_roundtrip
	pytest -v -s ./cfxdb/tests/test_xbr.py::test_paying_channel_req_roundtrip
	pytest -v -s ./cfxdb/tests/test_xbr.py::test_payment_channel_bal_roundtrip
	pytest -v -s ./cfxdb/tests/test_xbr.py::test_offer_roundtrip
	pytest -v -s ./cfxdb/tests/test_xbr.py::test_transaction_roundtrip

test_single:
	pytest -v -s ./cfxdb/tests/test_user.py::test_user_fbs_roundtrip


# auto-format code - WARNING: this my change files, in-place!
# use "pip install yapf==0.29.0"
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

build_fbs: build_fbs_bfbs build_fbs_python fix_fbs_python

# generate schema type library (.bfbs binary) from schema files
build_fbs_bfbs:
	$(FLATC) -o $(FBS_OUTPUT) --binary --schema --bfbs-comments --bfbs-builtins $(FBS_FILES)

# generate python3 bindings from schema files
build_fbs_python:
	$(FLATC) -o $(FBS_OUTPUT) --python $(FBS_FILES)

fix_fbs_python:
	# those are not generated, but required
	touch $(FBS_OUTPUT)/__init__.py

	# FIXME: wrong import:
	# "from oid_t import oid_t" => "from ..oid_t import oid_t"
	find $(FBS_OUTPUT) -name "*.py" -exec sed -i'' 's/from oid_t/from ..oid_t/g' {} \;
