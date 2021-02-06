# Web Automation Project (web bot) Prototype
This web bot prototype provides a template for building a web automation framework using python selenium with unittest.
Selenium provides the web automatiom functionality, and unittest provides a testing framework for validating expected
web bot behaviors. Pip will be used to install and manage python packages.  Virtualenv will be used to create an encapsulated
development evironment. This way, the packages installed with pip will only be available inside the dev enviroment while it
is activated. More information can found at the links below:

- [Selenium](https://selenium-python.readthedocs.io/installation.html)
- [Unittest](https://docs.python.org/3/library/unittest.html)
- [Pip](https://pip.pypa.io/en/stable/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)

# Setup
Use the following instructions to setup the dev environment.  All instructions must be performed from your terminal:

## 1. Install pip
First, see if pip is already install. Open terminal and run
    which pip
The location of pip should be displayed in the terminal, if not, download and install it:
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py

## 2. Install virtualenv
confirm if virtualenv is already installed
    which virtualenv
if not installed run the following
    pip install virtualenv

## 3. Clone web automation repo
Run the following
    git clone https://github.com/otkinsey/web_automation

## 4. Create virtualenv
Run the following
    virtualenv projectenv --python=python3

## 5. Install testing and web automation dpendencies
pip install -r requirements.txt

## 6. Run automation test script
    python test_automate_browser.py