.PHONY: run

run:
	docker build --tag cart_pricing_service:1.0 .
	docker run --rm --interactive cart_pricing_service:1.0
