# Purpose
Quick knockoff of Denver Python website at `https://denver-python.github.io/` using `streamlit`.

# Development
## Install pyenv
### MacOS
```
brew install pyenv
```
or:
```
curl https://pyenv.run | bash
```
### UNIX
```
curl https://pyenv.run | bash
```

## Create virtualenv
```
pyenv install 3.12.0
pyenv virtualenv 3.12.0 denver-python
pyenv local denver-python

pip install --upgrade pip
pip install -r requirements.txt
```

## Run locally
```
streamlit run streamlit_app.py
```

## View in browser
Direct browser to `http://localhost:8501/`

# Known bugs
- Default display does not show with home page at first.
I think the fix would be related to this bug report from 2023:
https://discuss.streamlit.io/t/how-to-set-the-default-page-in-multipage-app-i-dont-want-to-use-main-welcome-page/51270/2
