PYTHON=python
CONFIG=config/ecuador_ipc_oni.yaml

setup:
	$(PYTHON) -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

demo:
	$(PYTHON) scripts/generate_demo_data.py
	$(PYTHON) scripts/run_pipeline.py --config config/demo.yaml

run:
	$(PYTHON) scripts/run_pipeline.py --config $(CONFIG)

test:
	pytest -q

lint:
	ruff check src scripts tests

dashboard:
	cd dashboard && npm install && npm run dev
