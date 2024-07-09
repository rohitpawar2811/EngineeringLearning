#!/bin/bash

# Grafana Username and Password
grafana_username="admin"
grafana_password="@rohit12"

# Function to delete a rule by its UUID
delete_rule() {
    local rule_uuid=$1
    curl --location --request DELETE "http://localhost:3000/api/v1/provisioning/alert-rules/$rule_uuid" \
    --header 'X-Disable-Provenance;' \
    --header 'Content-Type: application/json' \
    --user $grafana_username:$grafana_password
}

# Get all rules
rules_response=$(curl --location --request GET 'http://localhost:3000/api/v1/provisioning/alert-rules' \
--header 'Authorization: Basic YWRtaW46QHJvaGl0MTI=')

# Extract UUIDs from the response and delete each rule
rule_uuids=$(echo "$rules_response" | jq -r '.[] | .uid')
for rule_uuid in $rule_uuids; do
    echo "Deleting rule with UUID: $rule_uuid"
    delete_rule $rule_uuid
done
