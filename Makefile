start:
	uvicorn aschii_chars.main:app --reload --port 8889

lint:
	black .

tests:
	pytest
