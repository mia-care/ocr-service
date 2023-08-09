# OCR Plugin

[![Python version](https://img.shields.io/badge/python-v3.10-blue)](.coverage/html/index.html)
[![FastAPI version](https://img.shields.io/badge/fastapi-v0.78.0-blue)](.coverage/html/index.html)
[![Coverage](.badges/coverage-badge.svg)](.coverage/html/index.html)

---

The OCR plugin (aka Optical Character Recognition) is a microservice which allows users to extract text from images.

---

## Local development

To develop the service locally you need:

- python 3.10

A virtual environment is a Python tool for dependency management and project
isolation. For further info about the creation and management of a virtual environment,
please check the [Python official documentation](https://docs.python.org/3/library/venv.html).
To activate your virtual envirorment run the following command on
your terminal:

```
source /path/to/virtual/environment/bin/activate
```

When finished, to deactive the virtual envirorment run the following
command:

```
deactivate
```

During development, you will probably have to perform the same operations many
times: start the application locally, check the code quality, run tests and compute coverage. Therefore,
to avoid to remember each time the syntax of the commands to be executed, the
main commands were collected in a Makefile. [Makefile](https://www.gnu.org/software/make/manual/make.html) is a Unix automation tool
that contains the recipe to build and run your program. So, listed below are the
commands that can be executed by the make command:

Install requirements and pre-commit:
```
make setup
```

Run application locally:
```
make start
```

Run linter:
```
make lint
```

Run tests:
```
make test
```

Run the dashboard for load tests:
```
make start-load-test-dashboard
```

Compute the coverage:
```
make coverage
```