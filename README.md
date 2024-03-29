# Web_Interaction_Package (ask_pepperonit)

This is a small part collection of methods from a Pepper project. This package does not have any value by itself, but is rather customized for our colleagues to call upon certain methods within their block-programming module.

Functionality mainly revolves around doing calls to Google's and Wikipedia's API with text(string) input and having Pepper display the results in an appropriate way.

## Installation

Run the following to install:

```bash
pip install ask_pepperonit
```

## Usage / Example
Usage will be demonstrated with bash/terminal use.


In order to use the module, we import the Ask class from the module:

```bash
python
```

```python
from ask_pepperonit import Ask
```

Then we instatiate the Ask class with your Google search engine information.

```python
ask = Ask("YOUR_GOOGLE_API_KEY", "YOUR_GOOGLE_CX_KEY")
```

Now we can simply call either ask_google_api or ask_wikipedia_api with a string input

```python
ask.ask_google_api("Cats and dogs")
```

To which the method returns a string, a link to a google image (Link provided in the terminal aswell)

## Contribution
```bash
python setup.py bdist_wheel sdist
```
then:
```bash
twine upload .\dist\ask_pepperonit-x.x.x-py3-none-any.whl .\dist\ask_pepperonit-x.x.x.tar.gz
```
Where "x.x.x" is the version number set in the setup.py file, e.g. "0.0.1"

## LICENSE
MIT License