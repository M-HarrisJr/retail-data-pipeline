#!/bin/bash

echo "Starting retail data pipeline..."

echo "Running ETL script..."
python scripts/etl_pipeline.py

echo "Pipeline completed successfully."
