
init:
	virtualenv .

reset:
	virtualenv -clear .

clean:
	rm -fR bin

activate:
	source bin/activate
