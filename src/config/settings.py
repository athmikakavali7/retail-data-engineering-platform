from pathlib import Path
from dotenv import load_dotenv
import os

# Load .env from docker directory
BASE_DIR = Path(__file__).resolve().parents[2]
ENV_PATH = BASE_DIR / "docker" / ".env"

load_dotenv(ENV_PATH)

# Kafka Configuration
KAFKA_BOOTSTRAP_SERVERS = f"localhost:{os.getenv('KAFKA_PORT')}"
KAFKA_TOPIC = "orders"

# PostgreSQL Configuration
POSTGRES_HOST = "localhost"
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")