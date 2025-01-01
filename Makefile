.PHONY: install test lint docs clean run

install:
	uv pip install ".[dev,test,docs]"

test:
	PYTHONPATH=. pytest tests/

lint:
	black src/
	flake8 src/

docs:
	mkdocs build

clean:
	rm -rf build/ dist/ *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +

run:
	streamlit run src/app.py 
