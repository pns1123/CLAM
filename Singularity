Bootstrap: docker
From: ubuntu:20.04

%post
    # Update and install system dependencies
    apt-get update && apt-get install -y \
        python3 \
        python3-pip \
        curl \
        git

    # Install uv
    curl -LsSf https://astral.sh/uv/install.sh | sh

    # Add uv to PATH
    echo 'export PATH="/root/.cargo/bin:$PATH"' >> $SINGULARITY_ENVIRONMENT

    # Copy the project files (GitHub Actions will handle this)
    # COPY . /app

    # Change to the project directory
    cd /app

    # Use uv to install project dependencies
    /root/.cargo/bin/uv pip install -r requirements.txt

%environment
    export PYTHONPATH=/app:$PYTHONPATH

%runscript
    python3 /app/your_training_script.py

%labels
    Author Your Name
    Version v1.0
