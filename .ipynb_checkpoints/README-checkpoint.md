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