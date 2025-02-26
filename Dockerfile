# Use official Python image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Install Poetry (recommended way)
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy only the necessary files first to leverage Docker caching
COPY pyproject.toml poetry.lock ./

# Install dependencies (without virtualenv inside the container)
RUN poetry config virtualenvs.create false && poetry install --no-root

# Copy the rest of the project files
COPY . .

RUN poetry install

# Default command (change as needed)
CMD ["poetry", "install"]
