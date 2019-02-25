# Bitmovin Python Client
[![bitmovin](http://bitmovin-a.akamaihd.net/webpages/bitmovin-logo-github.png)](http://www.bitmovin.com)

Python-Client which enables you to seamlessly integrate the Bitmovin API into your projects. Using this API client requires an active account.
TypeScript/JavaScript-Client which enables you to seamlessly integrate the Bitmovin API into your projects. Using this API client requires an active account.

[Sign up for a Bitmovin Account!](https://dashboard.bitmovin.com/signup)

The full API reference can be found [here](https://bitmovin.com/docs).

## Installation
### pip install

#### Python 2.7
```sh
pip install git+https://github.com/bitmovin/bitmovin-python.git
```

#### Python 3.4+
```sh
pip3 install git+https://github.com/bitmovin/bitmovin-python.git
```

### Setuptools

#### Python 2.7
```sh
python setup.py install
```

#### Python 3.4+
```sh
python3 setup.py install
```

## Initialization

```python
import bitmovin_python.bitmovin_api import BitmovinApi


bitmovinApi = BitmovinApi(api_key='<YOUR_API_KEY>')
```
