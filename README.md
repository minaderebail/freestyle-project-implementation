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

Run the unemployment analysis:

```sh
python -m app.unemployment
```