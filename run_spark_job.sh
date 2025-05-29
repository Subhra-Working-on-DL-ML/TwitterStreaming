SPARK_CONTAINER=$(docker ps --filter "ancestor=bitnami/spark:latest" --filter "name=spark" --format "{{.Names}}")

if [ -z "$SPARK_CONTAINER" ]; then
  echo "Spark container not running. Please run: docker-compose up -d"
  exit 1
fi

echo "Running Spark job inside container: $SPARK_CONTAINER"
docker exec -it "$SPARK_CONTAINER" spark-submit /opt/spark-apps/streaming.py