# LangChain Solutions


Basic LangChain solutions

## Prerequisites

### 1. Poetry

1. Ensure that you have Poetry installed on your system. You can install it using the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Add Poetry to path

- On Linux

```bash
echo $'\nexport PATH="/home/jovyan/.local/bin:$PATH"' >> ~/.bashrc

source ~/.bashrc
```

- On Mac

```bash
echo $'\nexport PATH="/home/jovyan/.local/bin:$PATH"' >> ~/.zshrc

source ~/.bashrc
```

3. Check result

```bash
poetry --version
```


## Streamlit application

### 1. Create virtual environment

```bash
conda create --prefix ./.venv -y
conda activate ./.venv
```

### 2. Install dependencies

```bash
poetry install --no-root
```

### 3. Run the application

```bash
streamlit run RestaurantGenerator/main.py
```

### 4. Test the application

Open the browser and navigate to `http://localhost:8501/`

### 5. Deactivate the virtual environment

```bash
conda deactivate
```
