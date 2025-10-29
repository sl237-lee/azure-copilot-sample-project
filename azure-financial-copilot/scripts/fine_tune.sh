#!/usr/bin/env bash
set -euo pipefail

# Variables to set
RESOURCE_GROUP=${RESOURCE_GROUP:-"your-rg"}
AOAI_NAME=${AOAI_NAME:-"your-aoai-resource"}
LOCATION=${LOCATION:-"eastus"}
MODEL_DEPLOYMENT=${MODEL_DEPLOYMENT:-"gpt-35-turbo"} # base model
TRAIN_FILE="data/train.jsonl"
SUFFIX="finance-copilot"

echo "Creating fine-tune job on $AOAI_NAME using $TRAIN_FILE ..."

az openai fine-tunes create   --resource-group "$RESOURCE_GROUP"   --deployment-name "$MODEL_DEPLOYMENT"   --name-suffix "$SUFFIX"   --training-file "@${TRAIN_FILE}"

echo "Fine-tune submitted. Check status with:"
echo "az openai fine-tunes list --resource-group $RESOURCE_GROUP"
