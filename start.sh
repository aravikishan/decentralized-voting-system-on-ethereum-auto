#!/bin/bash
set -e
echo "Starting Decentralized Voting System on Ethereum..."
uvicorn app:app --host 0.0.0.0 --port 9016 --workers 1
