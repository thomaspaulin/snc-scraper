# Useful site: https://krzysztofzuraw.com/blog/2016/makefiles-in-python-projects.html
clean:
		find . -name '*.pyc' -exec rm --force {} +
