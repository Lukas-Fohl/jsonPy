# Small JSON Parser

A minimal JSON parser and stringifier in Python.

## Table of Contents

- [Small JSON Parser](#small-json-parser)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Running Tests](#running-tests)
    - [Running Examples](#running-examples)
  - [File Structure](#file-structure)

## Overview

This project provides a simple JSON parser and stringifier. It allows you to parse JSON strings into Python objects and convert Python objects back into JSON strings.

## Installation

No installation is required. Just clone or download the repository and use Python 3.

## Usage

### Running Tests

To run the test suite, execute:

```
python3 -m test.test
```

This will run a series of assertions to verify the correctness of the parser and stringifier.

### Running Examples

To run the example scripts:

- For reading and accessing JSON data:

  ```
  python3 -m examples.read
  ```

- For stringifying JSON data:

  ```
  python3 -m examples.stringify
  ```

## File Structure

- `jsonMod/` - Contains the JSON parser and stringifier implementation.
- `examples/` - Example scripts demonstrating usage.
- `test/` - Test suite for the parser and stringifier.
