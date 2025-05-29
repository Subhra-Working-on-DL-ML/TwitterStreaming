# Twitter Stream Analysis with PySpark & Elasticsearch

This project captures real-time tweets using Twitter API, processes them using PySpark, and stores them in Elasticsearch for visualization in Kibana.

## 🚀 Setup

```bash
# Clone repo
cd twitter-stream-analysis

# Set up virtual env
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Set Twitter token
cp .env.example .env
# Edit .env to include your Twitter Bearer Token

# Start services
docker-compose up -d

# Run tweet producer
python ingestion/twitter_producer.py

# Start Spark job via helper script
chmod +x run_spark_job.sh
./run_spark_job.sh
```

## 📊 Kibana Dashboard
- Visit: http://localhost:5601
- Create index pattern: `tweets*`
- Use `created_at` as time field
- Start visualizing your tweet stream!

---
