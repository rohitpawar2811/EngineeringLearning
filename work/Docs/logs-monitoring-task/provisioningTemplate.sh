#!/bin/bash

# Define variables
# git_host="https://git.hotwax.co"
# git_token="glpat-S3UmVoenNR7ferypNJwP"
# grafana_host="http://localhost:3000"
# grafana_username="admin"
# grafana_password="@rohit12"
# project_id="304" 
# folder_path="sm-uat-templates"
# # file_name="alert.yml"
# branch="JsonTemplates"
# loki_datasource_uuid="YOUR_LOKI_DATASOURCE_UUID"

git_host=$1
git_token=$2
grafana_host=$4
grafana_username=$5
grafana_password=$6
folder_path=$7
project_id="304"
branch="JsonTemplates"
loki_datasource_uuid="YOUR_LOKI_DATASOURCE_UUID"


function folderExistsOrCreate() {
    local folder_name=$1

    local response=$(curl -sS --location --request GET "${grafana_host}/api/folders" \
        --header 'Content-Type: application/json' \
        --user $grafana_username:$grafana_password)
    local folder_uid=$(echo "$response" | jq -r ".[] | select(.title == \"$folder_name\") | .uid")

    if [ -z "$folder_uid" ]; then
        local folder_payload="{\"title\": \"$folder_name\"}"
        response=$(curl -sS --location --request POST "${grafana_host}/api/folders" \
            --header 'Content-Type: application/json' \
            --user $grafana_username:$grafana_password \
            --data-raw "$folder_payload")

        folder_uid=$(echo "$response" | jq -r '.uid')
    fi

    echo "$folder_uid"
}


function processAlerts() {
    # Extracting alert-json file from folder to current 
    fetchJsonFileToCurrent "alerts" "alert-rules.json"

    # Extract group inside folder_name and name
    local folder_name=$(jq -r '.groups[0].folder' input.json)
    local rule_group_name=$(jq -r '.groups[0].name' input.json)
    folder_name="SM-PROD-MAIN"

    echo "folder_name and rule_group name $folder_name $rule_group_name"

    #Check Folder Exists or not Otherwise Create
    local folder_uid=$(folderExistsOrCreate "$folder_name")
    
    # Iteration and adding part
    local rules=$(jq -c '.groups[0].rules[]' input.json)
    while IFS= read -r rule; do
        local rule_without_uid=$(echo "$rule" | jq 'del(.uid)')
        local folder_json=$(jq -n --arg folder "$folder_uid" '{folderUID: $folder}')
        local rule_group_json=$(jq -n --arg ruleGroup "$rule_group_name" '{ruleGroup: $ruleGroup}')
        local final_payload=$(echo "$folder_json $rule_group_json $rule_without_uid" | jq -s add)

        #Datasource Replacing Current only handled for Loki
        if [[ $(echo "$final_payload" | jq -r '.data[0].model.datasource.type') == "loki" ]]; then
            echo "Datasource Replaced---"
            final_payload=$(echo "$final_payload" | jq --arg loki_datasource_uuid "$loki_datasource_uuid" '.data[0].model.datasource |= . + {"uid": $loki_datasource_uuid} | .data[0] |= . + {"datasourceUid": $loki_datasource_uuid}')
        fi

        local curl_command="curl -sS --location "${grafana_host}/api/v1/provisioning/alert-rules/" \
            --header 'X-Disable-Provenance;' \
            --header 'Content-Type: application/json' \
            --user $grafana_username:$grafana_password \
            --data '$final_payload'"
        
        # echo "Executing curl command: $final_payload"
        # eval "$curl_command"
        local status=$(eval "$curl_command" 2>/dev/null)
    done <<< "$rules"

    local fileDeletionStatus=$(rm -rv input.json )
}

function processContactPoints() {
    echo "Processing contact points..."
     # Extracting alert-json file from folder to current 
    fetchJsonFileToCurrent "contact-points" "contact-points.json"

    #1. Uid remove , name extraction, extract the json inside receivers [] and then include the name details inside 
    contactPoint=$(jq -r '.contactPoints[0].name' input.json)

    local receivers=$(jq -c '.contactPoints[0].receivers[]' input.json)
    while IFS= read -r receiver; do
        local receiver_without_uid=$(echo "$receiver" | jq 'del(.uid)')
        local receiver_with_cp=$(jq -n --arg contact "$contactPoint" '{name: $contact}')

        local final_receiver=$(echo "$receiver_with_cp $receiver_without_uid" | jq -s add)

        local curl_command="curl -sS --location "${grafana_host}/api/v1/provisioning/contact-points/" \
            --header 'X-Disable-Provenance;' \
            --header 'Content-Type: application/json' \
            --user $grafana_username:$grafana_password \
            --data '$final_receiver'"
        
        # eval "$curl_command"
        # Execute the curl command, capture stdout and suppress stderr
        local status=$(eval "$curl_command" 2>/dev/null)

    done <<< "$receivers"

    local fileDeletionStatus=$(rm -rv input.json )
}

function processNotificationPolicies() {
    echo "Processing notification policies..."
    
    fetchJsonFileToCurrent "notification-policies" "notification-policies.json"
    local policies=$(jq -c '.policies[]' input.json)
    while IFS= read -r policy; do
        local curl_command="curl -sS --location '${grafana_host}/api/v1/provisioning/policies/' \
            --header 'X-Disable-Provenance;' \
            --header 'Content-Type: application/json' \
            --user '${grafana_username}:${grafana_password}' \
            --request PUT \
            --data '${policy}'"
            
        eval "$curl_command"
    done <<< "$policies"
    local fileDeletionStatus=$(rm -rv input.json )
}


function fetchJsonFileToCurrent() {
    # Extracting .json file from folder-fetched-throw-gitlab to current 
    # Change directory to tempContentRepo
    local specific_folder=$1
    local specific_file=$2
    cd tempContentRepo || exit

    # Navigate two folders ahead
    cd */*/ || exit

    # Copy alerts.json to current directory and rename it to input.json
    cp "$specific_folder/$specific_file" ../../../

    # Move back to the original directory
    cd ../../../ || exit
    mv "$specific_file" input.json
}

function cleanUP() {
    local fileDeletionStatus=$( rm -rv tempContentRepo* )
    fileDeletionStatus=$(rm -rv app_archive* )
}


function featchTemplatesFromGitRepo() {
    # Fetch file from GitLab repository
    curl -sS --header "PRIVATE-TOKEN: ${git_token}" "${git_host}/api/v4/projects/${project_id}/repository/archive.tar.gz?sha=${branch}&path=${folder_path}" -o app_archive.tar.gz
    mkdir tempContentRepo
    tar -xzf app_archive.tar.gz -C tempContentRepo
}


function controller() {
    featchTemplatesFromGitRepo
    processAlerts
    processContactPoints
    processNotificationPolicies
    cleanUP
}

function start() {
    controller
}

start



                                
# 1. Git Branch pai update kar do json :done
# 2. Import/export doc I have to update : preparing
# 3. Where to push this script. : 
# 4. Currently not going for Jenkins because of something.

