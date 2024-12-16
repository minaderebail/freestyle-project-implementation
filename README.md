# freestyle-project-implementation

## Setup

Create a new virtual environment (first time only):

```sh
conda create -n freestyle-env python=3.10
```

Activate the virtual environment (whenever you come back to this project): 

```sh
conda activate freestyle-env
```


Install packages:

```sh
pip install -r requirements.txt
```

## API Keys

This app uses the AlphaVantage API.
To obtain an API key, go to
https://www.alphavantage.co/support/#api-key

Create a ".env" file and add AlphaVantage API key:

```sh
# this is the ".env" file:
ALPHAVANTAGE_API_KEY="..."
```

## Usage

Run the inflation rate analysis:

```sh
python -m app.inflation
```

Run the interest rate analysis:

```sh
python -m app.interest
```

Run the 10-year treasury yield rate analysis:

```sh
python -m app.treasury_yield
```

Run the unemployment rate analysis:

```sh
python -m app.unemployment
```

## Web App
Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

## Testing

Run tests:
```sh
pytest
```