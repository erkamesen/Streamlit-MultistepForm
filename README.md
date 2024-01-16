# Streamlit Multistep Form

*You can see an example of a multi-step form in this project with streamlit, a library that we can make web applications with Python without front end technologies such as CSS JS etc..*

## Install & Usage

- *Clone the repository*
```
git clone https://github.com/erkamesen/Streamlit-MultistepForm.git
```
- *Change Directory*
```
cd ./Streamlit-MultistepForm/
```

### Without Docker

- *Set your own virtual environment*
```
python3 -m venv venv
```
*Linux & MacOS*
```
source venv/bin/activate
```
*Windows*
```
.\venv\Scripts\activate
```

- *Install dependecies*
```
pip install -r requirements.txt
```

- *Run server*
```
streamlit run main.py
```

### With Docker

- *Build your image*
```
docker build -t <image_name> .
```
- *Run image*
```
docker run -p 8501:8501 <image_name>
```
- *Now you can connect to the server on port 8501.*
