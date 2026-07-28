from pathlib import Path
from dotenv import load_dotenv
import os

# ----------------------------------------------------
# Load docker/.env
# ----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]
ENV_PATH = BASE_DIR / "docker" / ".env"

load_dotenv(ENV_PATH)

# ----------------------------------------------------
# Environment
# ----------------------------------------------------

APP_ENV = os.getenv("APP_ENV", "local")

# ----------------------------------------------------
# Kafka
# ----------------------------------------------------

if APP_ENV == "docker":
    KAFKA_BOOTSTRAP_SERVERS = "kafka:9092"
else:
    KAFKA_BOOTSTRAP_SERVERS = f"localhost:{os.getenv('KAFKA_PORT')}"

KAFKA_TOPIC = "orders"

# ----------------------------------------------------
# PostgreSQL
# ----------------------------------------------------

if APP_ENV == "docker":
    POSTGRES_HOST = "postgres"
else:
    POSTGRES_HOST = "localhost"

POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

# ----------------------------------------------------
# Spark
# ----------------------------------------------------

SPARK_MASTER = os.getenv(
    "SPARK_MASTER",
    "spark://localhost:7077"
)