# Updating this client
```shell
pyenv install 3.11
pyenv local 3.11
pip install openapi-python-client
curl https://api.vantage.sh/v2/oas_v3.json > openapiv3-spec.json
openapi-python-client generate --url https://api.vantage.sh/v2/oas_v3.json --output-path ./ --overwrite
```
