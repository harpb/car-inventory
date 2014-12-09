##  Installation

1. Create and activate virtualenv:

	    virtualenv pyenv --prompt="Inventory"
		. pyenv/bin/activate

2. Install py modules
	
		pip install django django-tastypie pyyaml

3. Run Server

		webapp/manage.py runserver

##  HTTP API
Replace `<string>` with any of following to filter by a brand: `Sport`, `Compact`, `Luxury`
	
	http://127.0.0.1:8000/api/v1/car_model/?format=json&brand__name=<string>