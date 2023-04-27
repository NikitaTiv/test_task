style:
	flake8 .

types:
	mypy test_task
	
check:
	make style types
