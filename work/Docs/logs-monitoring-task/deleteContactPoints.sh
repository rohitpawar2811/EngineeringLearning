#!/bin/bash

# Grafana server details
GRAFANA_HOST="http://localhost:3000"
GRAFANA_USERNAME="admin"
GRAFANA_PASSWORD="@rohit12"

# Function to delete all contact points
delete_contact_points() {
    # Fetch list of contact points
    contact_points=$(curl -sS --location --request GET "${GRAFANA_HOST}/api/v1/provisioning/contact-points" \
        --header 'Content-Type: application/json' \
        --user "${GRAFANA_USERNAME}:${GRAFANA_PASSWORD}")

    # Check if any contact points exist
    if [ "$(echo "$contact_points" | jq length)" -eq 0 ]; then
        echo "No contact points found."
        return
    fi

    # Loop through and delete each contact point
    for row in $(echo "${contact_points}" | jq -r '.[] | @base64'); do
        contact_point=$(echo "${row}" | base64 -d)
        contact_point_uid=$(echo "$contact_point" | jq -r '.uid')
        contact_point_name=$(echo "$contact_point" | jq -r '.name')

        # Delete contact point
        response=$(curl -sS --location --request DELETE "${GRAFANA_HOST}/api/v1/provisioning/contact-points/${contact_point_uid}" \
            --header 'Content-Type: application/json' \
            --user "${GRAFANA_USERNAME}:${GRAFANA_PASSWORD}")

        echo "Deleted contact point: $contact_point_name"
    done
}

# Run the function
delete_contact_points
