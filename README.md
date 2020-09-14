# Cart Pricing Service

This is just a small example of Object Oriented modeling for a Cart 
Pricing Service.

## Problem statement
A store sells 3 types of fruits: Apples, Grapes and Bananas.

A bag of apples costs $7, a box of grapes costs $15 and a sack of bananas
costs $3.

If a customer buys 2 or more bags of apples, they get 20% off the price of
all apples. The store also offers a buy-one-get-one-free discount for 
grapes. There is no discount for bananas.

Create an implementation for this store pricing policy so that given a list
of items and their quantities, it returns the price after all discounts. 

## Running
```sh
# using docker
make run

# using python3
python3 -m cart_pricing_service
```

Example run:
```sh
How many Apples ($7.00)? 1
How many Bananas ($3.00)? 2
How many Grapes ($15.00)? 3
----------------------------
Your cart total is: $43.00
```

## Contributing
```sh
# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```


## Credits
This package was created with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template.
