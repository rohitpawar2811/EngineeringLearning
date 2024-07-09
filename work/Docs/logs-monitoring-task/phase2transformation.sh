# #!/bin/bash

# transform_json() {
#     local input_json="$1"

#     # Rule-group name changes SM-uat -> SM-prod errors
#     input_json=$(echo "$input_json" | jq '.name |= gsub("SM-uat"; "SM-prod errors")')

#     # # Folder-name changed SM-uat -> SM-Prod-MAIN
#     input_json=$(echo "$input_json" | jq '.folder |= gsub("SM-uat"; "SM-Prod-MAIN")')

#     # # expr change to this job="sm-prod.hotwax.io"
#     # input_json=$(echo "$input_json" | jq '.rules[].data[].model.expr |= gsub("job=\"sm-uat.hotwax.io\""; "job=\"sm-prod.hotwax.io\"")')

#     # # Annotations: instance-url change, sm-uat.hotwax.io -> https://hc.stevemadden.com/
#     # input_json=$(echo "$input_json" | jq '.rules[].annotations."Instance URL" |= gsub("sm-uat.hotwax.io"; "https://hc.stevemadden.com")')

#     # # Team change SM-UAT -> SM-Prod
#     # input_json=$(echo "$input_json" | jq '.rules[].labels.Team |= gsub("SM-UAT"; "SM-Prod")')

#     # # alert-rule-id-type name change from sm-uat-alerts ->sm-prod-alerts
#     # input_json=$(echo "$input_json" | jq '.rules[].labels."alert-rule-id-type" |= gsub("sm-uat-alert"; "sm-prod-alert")')

#     # # In alert-name might we include the instance name
#     # input_json=$(echo "$input_json" | jq '.rules[].name |= sub("(Out Of Memory Error Monitoring)"; "\\1 (sm-prod.hotwax.io)")')

#     echo "$input_json"
# }

# # Example JSON data
# json_data='{
#     "orgId": 1,
#     "name": "SM-uat Errors",
#     "folder": "SM-uat-main",
#     "interval": "5m",
#     "rules": [
#         {
#             "uid": "f69b047c-9b06-4563-846e-36bb7a4ecf75",
#             "title": "Out Of Memory Error Monitoring",
#             "condition": "C",
#             "data": [
#                 {
#                     "refId": "A",
#                     "queryType": "instant",
#                     "relativeTimeRange": {
#                         "from": 600,
#                         "to": 0
#                     },
#                     "datasourceUid": "b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5",
#                     "model": {
#                         "datasource": {
#                             "type": "loki",
#                             "uid": "b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5"
#                         },
#                         "editorMode": "code",
#                         "expr": "sum by(errorMessage) (count_over_time({job=\"sm-uat.hotwax.io\"} |~ `java\\.lang\\.OutOfMemoryError.*(?:\\n\\s+.*)*` | pattern `<_> <errorMessage> duration<_>` [5m]))",
#                         "intervalMs": 1000,
#                         "maxDataPoints": 43200,
#                         "queryType": "instant",
#                         "refId": "A"
#                     }
#                 }
#             ],
#             "noDataState": "OK",
#             "execErrState": "OK",
#             "for": "5m",
#             "annotations": {
#                 "ErrorMessage": "Out Of Memory Error Occurred",
#                 "Instance URL": "https://sm-uat.hotwax.io/",
#                 "summary": "Out Of Memory Error Occurred"
#             },
#             "labels": {
#                 "Team": "SM-Uat",
#                 "Type": "Error Alerts",
#                 "alert-rule-id-type": "sm-uat-alert",
#                 "severity": "error"
#             },
#             "isPaused": false
#         }
#     ]
# }'

# # Transform the JSON
# transformed_json=$(transform_json "$json_data")

# # Print the transformed JSON
# echo "$transformed_json"

# {job=\"sm-uat.hotwax.io\"}
# https://sm-uat.hotwax.io/

# &Instance -> adoc-sv-oms
# &Folder -> adoc-sv-oms
# &JobName ->  {job=\"sm-uat.hotwax.io\"}
# &InstanceURL -> https://sm-uat.hotwax.io/


# json_data='{
#     "orgId": 1,
#     "name": "&Instance errors",
#     "folder": "&Folder-main",
#     "interval": "5m",
#     "rules": [
#         {
#             "uid": "f69b047c-9b06-4563-846e-36bb7a4ecf75",
#             "title": "Out Of Memory Error Monitoring",
#             "condition": "C",
#             "data": [
#                 {
#                     "refId": "A",
#                     "queryType": "instant",
#                     "relativeTimeRange": {
#                         "from": 600,
#                         "to": 0
#                     },
#                     "datasourceUid": "b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5",
#                     "model": {
#                         "datasource": {
#                             "type": "loki",
#                             "uid": "b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5"
#                         },
#                         "editorMode": "code",
#                         "expr": "sum by(errorMessage) (count_over_time(&JobName |~ `java\\.lang\\.OutOfMemoryError.*(?:\\n\\s+.*)*` | pattern `<_> <errorMessage> duration<_>` [5m]))",
#                         "intervalMs": 1000,
#                         "maxDataPoints": 43200,
#                         "queryType": "instant",
#                         "refId": "A"
#                     }
#                 }
#             ],
#             "noDataState": "OK",
#             "execErrState": "OK",
#             "for": "5m",
#             "annotations": {
#                 "ErrorMessage": "Out Of Memory Error Occurred",
#                 "Instance URL": "&InstanceURL",
#                 "summary": "Out Of Memory Error Occurred"
#             },
#             "labels": {
#                 "Team": "&Instance",
#                 "Type": "Error Alerts",
#                 "alert-rule-id-type": "&Instance-alert",
#                 "severity": "error"
#             },
#             "isPaused": false
#         }
#     ]
# }'


# #!/bin/bash

# transform_json() {
#     local input_json="$1"

#     # Define replacements
#     local instance="adoc-sv-oms"
#     local folder="adoc-sv-oms"
#     local job_name="{job=\"sm-uat.hotwax.io\"}"
#     local instance_url="https://sm-uat.hotwax.io/"

#     # Use jq to replace placeholders
#     input_json=$(echo "$input_json" | jq --arg instance "$instance" \
#                                          --arg folder "$folder" \
#                                          --arg job_name "$job_name" \
#                                          --arg instance_url "$instance_url" \
#                                          '.name |= gsub("&Instance"; $instance) | 
#                                            .folder |= gsub("&Folder"; $folder) | 
#                                            .rules[].labels.Team |= gsub("&Instance"; $instance) | 
#                                            .rules[].labels."alert-rule-id-type" |= gsub("&Instance"; $instance) | 
#                                            .rules[].annotations."Instance URL" |= gsub("&InstanceURL"; $instance_url) | 
#                                            .rules[].data[].model.expr |= gsub("&JobName"; $job_name)' -)

#     echo "$input_json"
# }

# # Example JSON data
# json_data='{
#     "orgId": 1,
#     "name": "&Instance errors",
#     "folder": "&Folder-main",
#     "interval": "5m",
#     "rules": [
#         {
#             "uid": "f69b047c-9b06-4563-846e-36bb7a4ecf75",
#             "title": "Out Of Memory Error Monitoring",
#             "condition": "C",
#             "data": [
#                 {
#                     "refId": "A",
#                     "queryType": "instant",
#                     "relativeTimeRange": {
#                         "from": 600,
#                         "to": 0
#                     },
#                     "datasourceUid": "b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5",
#                     "model": {
#                         "datasource": {
#                             "type": "loki",
#                             "uid": "b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5"
#                         },
#                         "editorMode": "code",
#                         "expr": "sum by(errorMessage) (count_over_time(&JobName |~ `java\\.lang\\.OutOfMemoryError.*(?:\\n\\s+.*)*` | pattern `<_> <errorMessage> duration<_>` [5m]))",
#                         "intervalMs": 1000,
#                         "maxDataPoints": 43200,
#                         "queryType": "instant",
#                         "refId": "A"
#                     }
#                 }
#             ],
#             "noDataState": "OK",
#             "execErrState": "OK",
#             "for": "5m",
#             "annotations": {
#                 "ErrorMessage": "Out Of Memory Error Occurred",
#                 "Instance URL": "&InstanceURL",
#                 "summary": "Out Of Memory Error Occurred"
#             },
#             "labels": {
#                 "Team": "&Instance",
#                 "Type": "Error Alerts",
#                 "alert-rule-id-type": "&Instance-alert",
#                 "severity": "error"
#             },
#             "isPaused": false
#         }
#     ]
# }'

# # Transform the JSON
# transformed_json=$(transform_json "$json_data")

# # Print the transformed JSON
# echo "$transformed_json"



#!/bin/bash

transform_json() {
    local input_json="$1"

    # Define replacements
    local instance="adoc-sv-oms"
    local folder="adoc-sv-oms"
    local job_name="{job=\"sm-uat.hotwax.io\"}"
    local instance_url="https://sm-uat.hotwax.io/"

    # Use jq to replace placeholders
    input_json=$(echo "$input_json" | jq --arg instance "$instance" \
                                         --arg folder "$folder" \
                                         --arg job_name "$job_name" \
                                         --arg instance_url "$instance_url" '
                .groups |= map(                         
                    .name |= gsub("&Instance"; $instance) | 
                    .folder |= gsub("&Folder"; $folder) | 
                    .rules |= map(.labels.Team |= gsub("&Instance"; $instance)) |
                    .rules |= map(.labels."alert-rule-id-type" |= gsub("&Instance"; $instance)) |
                    .rules |= map(.annotations."Instance URL" |= gsub("&InstanceURL"; $instance_url)) |
                    .rules |= map(.data[0].model.expr |= gsub("&JobName"; $job_name))
                )
                ')

    echo "$input_json"
}

# # Example JSON data
# json_data='{
#     "orgId": 1,
#     "name": "&Instance errors",
#     "folder": "&Folder-main",
#     "interval": "5m",
#     "rules": [
#         {
#             "uid": "f69b047c-9b06-4563-846e-36bb7a4ecf75",
#             "title": "Out Of Memory Error Monitoring",
#             "condition": "C",
#             "data": [
#                 {
#                     "refId": "A",
#                     "queryType": "instant",
#                     "relativeTimeRange": {
#                         "from": 600,
#                         "to": 0
#                     },
#                     "datasourceUid": "b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5",
#                     "model": {
#                         "datasource": {
#                             "type": "loki",
#                             "uid": "b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5"
#                         },
#                         "editorMode": "code",
#                         "expr": "sum by(errorMessage) (count_over_time(&JobName |~ `java\\.lang\\.OutOfMemoryError.*(?:\\n\\s+.*)*` | pattern `<_> <errorMessage> duration<_>` [5m]))",
#                         "intervalMs": 1000,
#                         "maxDataPoints": 43200,
#                         "queryType": "instant",
#                         "refId": "A"
#                     }
#                 }
#             ],
#             "noDataState": "OK",
#             "execErrState": "OK",
#             "for": "5m",
#             "annotations": {
#                 "ErrorMessage": "Out Of Memory Error Occurred",
#                 "Instance URL": "&InstanceURL",
#                 "summary": "Out Of Memory Error Occurred"
#             },
#             "labels": {
#                 "Team": "&Instance",
#                 "Type": "Error Alerts",
#                 "alert-rule-id-type": "&Instance-alert",
#                 "severity": "error"
#             },
#             "isPaused": false
#         },
#         {
#             "uid": "f69b047c-9b06-4563-846e-36bb7a4ecf76",
#             "title": "Another Rule",
#             "condition": "C",
#             "data": [
#                 {
#                     "refId": "A",
#                     "queryType": "instant",
#                     "relativeTimeRange": {
#                         "from": 600,
#                         "to": 0
#                     },
#                     "datasourceUid": "b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5",
#                     "model": {
#                         "datasource": {
#                             "type": "loki",
#                             "uid": "b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5"
#                         },
#                         "editorMode": "code",
#                         "expr": "sum by(errorMessage) (count_over_time(&JobName |~ `java\\.lang\\.OutOfMemoryError.*(?:\\n\\s+.*)*` | pattern `<_> <errorMessage> duration<_>` [5m]))",
#                         "intervalMs": 1000,
#                         "maxDataPoints": 43200,
#                         "queryType": "instant",
#                         "refId": "A"
#                     }
#                 }
#             ],
#             "noDataState": "OK",
#             "execErrState": "OK",
#             "for": "5m",
#             "annotations": {
#                 "ErrorMessage": "Another Error Occurred",
#                 "Instance URL": "&InstanceURL",
#                 "summary": "Another Error Occurred"
#             },
#             "labels": {
#                 "Team": "&Instance",
#                 "Type": "Another Type",
#                 "alert-rule-id-type": "&Instance-alert",
#                 "severity": "error"
#             },
#             "isPaused": false
#         }
#     ]
# }'

# # Transform the JSON
# transformed_json=$(transform_json "$json_data")

# # Print the transformed JSON
# echo "$transformed_json"



# #!/bin/bash

# transform_json() {
#     local input_json="$1"

#     # Define replacements
#     local instance="adoc-sv-oms"

#     # Use jq to replace placeholders
#     input_json=$(echo "$input_json" | jq --arg instance "$instance" '
#                 .contactPoints |= map(
#                     .name |= gsub("&Instance"; $instance) |
#                     .receivers[].settings.subject |= gsub("&Instance"; $instance)
#                 )
#                 ')

#     echo "$input_json"
# }

# # Example JSON data
# json_data='{
#     "apiVersion": 1,
#     "contactPoints": [
#         {
#             "orgId": 1,
#             "name": "&Instance monitoring",
#             "receivers": [
#                 {
#                     "uid": "ee81af31-fbe4-44c2-962d-b1738c598094",
#                     "type": "email",
#                     "settings": {
#                         "addresses": "rohit.pawar@hotwax.co;arvind.tomar@hotwaxsystems.com;",
#                         "singleEmail": false,
#                         "subject": "Error on &Instance instance"
#                     },
#                     "disableResolveMessage": true
#                 }
#             ]
#         },
#         {
#             "orgId": 1,
#             "name": "&Instance Monitoring",
#             "receivers": [
#                 {
#                     "uid": "fdjlbyfb8ra4gd",
#                     "type": "email",
#                     "settings": {
#                         "addresses": "rohit.pawar@hotwax.co;",
#                         "singleEmail": false,
#                         "subject": "Error on nifi-uat instance"
#                     },
#                     "disableResolveMessage": true
#                 }
#             ]
#         }
#     ]
# }'

# # Transform the JSON
# transformed_json=$(transform_json "$json_data")

# # Print the transformed JSON
# echo "$transformed_json"



# #!/bin/bash

# function transform_json() {
#     local input_json="$1"

#     # Define replacements
#     local instance="adoc-sv-oms"
#     local folder="adoc-sv-oms-main"
#     local job_name="{job=\"sm-uat.hotwax.io\"}"
#     local instance_url="https://sm-uat.hotwax.io/"

#     # Use jq to replace placeholders
#     input_json=$(echo "$input_json" | jq --arg instance "$instance" \
#                                          --arg folder "$folder" \
#                                          --arg job_name "$job_name" \
#                                          --arg instance_url "$instance_url" '
#                 .groups |= map(
#                     .name |= gsub("&Instance"; $instance) |
#                     .folder |= gsub("&Folder"; $folder) |
#                     .rules |= map(.labels.Team |= gsub("&Instance"; $instance)) |
#                     .rules |= map(.labels."alert-rule-id-type" |= gsub("&Instance"; $instance)) |
#                     .rules |= map(.annotations."Instance URL" |= gsub("&InstanceURL"; $instance_url))
#                     )
#                 ')

#     echo "$input_json"
# }

# # Example JSON data
json_data='{
    "apiVersion": 1,
    "groups": [
        {
            "orgId": 1,
            "name": "&Instance errors",
            "folder": "&Folder-main",
            "interval": "5m",
            "rules": [
                {
                    "uid": "f69b047c-9b06-4563-846e-36bb7a4ecf75",
                    "title": "Out Of Memory Error Monitoring",
                    "condition": "C",
                    "data": [
                        {
                            "refId": "A",
                            "queryType": "instant",
                            "relativeTimeRange": {
                                "from": 600,
                                "to": 0
                            },
                            "datasourceUid": "b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5",
                            "model": {
                                "datasource": {
                                    "type": "loki",
                                    "uid": "b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5"
                                },
                                "editorMode": "code",
                                "expr": "sum by(errorMessage) (count_over_time(&JobName |~ `java\\.lang\\.OutOfMemoryError.*(?:\\n\\s+.*)*` | pattern `<_> <errorMessage> duration<_>` [5m]))",
                                "intervalMs": 1000,
                                "maxDataPoints": 43200,
                                "queryType": "instant",
                                "refId": "A"
                            }
                        },
                        {
                            "refId": "B",
                            "relativeTimeRange": {
                                "from": 600,
                                "to": 0
                            },
                            "datasourceUid": "__expr__",
                            "model": {
                                "conditions": [
                                    {
                                        "evaluator": {
                                            "params": [],
                                            "type": "gt"
                                        },
                                        "operator": {
                                            "type": "and"
                                        },
                                        "query": {
                                            "params": [
                                                "B"
                                            ]
                                        },
                                        "reducer": {
                                            "params": [],
                                            "type": "last"
                                        },
                                        "type": "query"
                                    }
                                ],
                                "datasource": {
                                    "type": "__expr__",
                                    "uid": "__expr__"
                                },
                                "expression": "A",
                                "intervalMs": 1000,
                                "maxDataPoints": 43200,
                                "reducer": "sum",
                                "refId": "B",
                                "type": "reduce"
                            }
                        },
                        {
                            "refId": "C",
                            "relativeTimeRange": {
                                "from": 600,
                                "to": 0
                            },
                            "datasourceUid": "__expr__",
                            "model": {
                                "conditions": [
                                    {
                                        "evaluator": {
                                            "params": [
                                                0
                                            ],
                                            "type": "gt"
                                        },
                                        "operator": {
                                            "type": "and"
                                        },
                                        "query": {
                                            "params": [
                                                "C"
                                            ]
                                        },
                                        "reducer": {
                                            "params": [],
                                            "type": "last"
                                        },
                                        "type": "query"
                                    }
                                ],
                                "datasource": {
                                    "type": "__expr__",
                                    "uid": "__expr__"
                                },
                                "expression": "A",
                                "intervalMs": 1000,
                                "maxDataPoints": 43200,
                                "refId": "C",
                                "type": "threshold"
                            }
                        }
                    ],
                    "noDataState": "OK",
                    "execErrState": "OK",
                    "for": "5m",
                    "annotations": {
                        "ErrorMessage": "Out Of Memory Error Occurred",
                        "Instance URL": "&InstanceURL",
                        "summary": "Out Of Memory Error Occurred"
                    },
                    "labels": {
                        "Team": "&Instance",
                        "Type": "Error Alerts",
                        "alert-rule-id-type": "&Instance-alert",
                        "severity": "error"
                    },
                    "isPaused": false
                }
            ]
        }
    ]
}'

# Example JSON data
# json_data='{
#     "apiVersion": 1,
#     "groups": [
#         {
#             "orgId": 1,
#             "name": "&Instance errors",
#             "folder": "&Folder-main",
#             "interval": "5m",
#                 "rules": [
#                 {
#                     "uid": "f69b047c-9b06-4563-846e-36bb7a4ecf75",
#                     "title": "Out Of Memory Error Monitoring",
#                     "condition": "C",
#                     "data": [
#                         {
#                             "refId": "A",
#                             "queryType": "instant",
#                             "relativeTimeRange": {
#                                 "from": 600,
#                                 "to": 0
#                             },
#                             "datasourceUid": "b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5",
#                             "model": {
#                                 "datasource": {
#                                     "type": "loki",
#                                     "uid": "b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5"
#                                 },
#                                 "editorMode": "code",
#                                 "expr": "sum by(errorMessage) (count_over_time(&JobName |~ `java\\.lang\\.OutOfMemoryError.*(?:\\n\\s+.*)*` | pattern `<_> <errorMessage> duration<_>` [5m]))",
#                                 "intervalMs": 1000,
#                                 "maxDataPoints": 43200,
#                                 "queryType": "instant",
#                                 "refId": "A"
#                             }
#                         }
#                     ],
#                     "noDataState": "OK",
#                     "execErrState": "OK",
#                     "for": "5m",
#                     "annotations": {
#                         "ErrorMessage": "Out Of Memory Error Occurred",
#                         "Instance URL": "&InstanceURL",
#                         "summary": "Out Of Memory Error Occurred"
#                     },
#                     "labels": {
#                         "Team": "&Instance",
#                         "Type": "Error Alerts",
#                         "alert-rule-id-type": "&Instance-alert",
#                         "severity": "error"
#                     },
#                     "isPaused": false
#                 },
#                 {
#                     "uid": "f69b047c-9b06-4563-846e-36bb7a4ecf76",
#                     "title": "Another Rule",
#                     "condition": "C",
#                     "data": [
#                         {
#                             "refId": "A",
#                             "queryType": "instant",
#                             "relativeTimeRange": {
#                                 "from": 600,
#                                 "to": 0
#                             },
#                             "datasourceUid": "b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5",
#                             "model": {
#                                 "datasource": {
#                                     "type": "loki",
#                                     "uid": "b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5"
#                                 },
#                                 "editorMode": "code",
#                                 "expr": "sum by(errorMessage) (count_over_time(&JobName |~ `java\\.lang\\.OutOfMemoryError.*(?:\\n\\s+.*)*` | pattern `<_> <errorMessage> duration<_>` [5m]))",
#                                 "intervalMs": 1000,
#                                 "maxDataPoints": 43200,
#                                 "queryType": "instant",
#                                 "refId": "A"
#                             }
#                         }
#                     ],
#                     "noDataState": "OK",
#                     "execErrState": "OK",
#                     "for": "5m",
#                     "annotations": {
#                         "ErrorMessage": "Another Error Occurred",
#                         "Instance URL": "&InstanceURL",
#                         "summary": "Another Error Occurred"
#                     },
#                     "labels": {
#                         "Team": "&Instance",
#                         "Type": "Another Type",
#                         "alert-rule-id-type": "&Instance-alert",
#                         "severity": "error"
#                     },
#                     "isPaused": false
#                 }
#             ]
#         }
#     ]
# }'


# Call the transformation function
transform_json "$json_data"



    # "rules": [
    #     {
    #         "uid": "f69b047c-9b06-4563-846e-36bb7a4ecf75",
    #         "title": "Out Of Memory Error Monitoring",
    #         "condition": "C",
    #         "data": [
    #             {
    #                 "refId": "A",
    #                 "queryType": "instant",
    #                 "relativeTimeRange": {
    #                     "from": 600,
    #                     "to": 0
    #                 },
    #                 "datasourceUid": "b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5",
    #                 "model": {
    #                     "datasource": {
    #                         "type": "loki",
    #                         "uid": "b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5"
    #                     },
    #                     "editorMode": "code",
    #                     "expr": "sum by(errorMessage) (count_over_time(&JobName |~ `java\\.lang\\.OutOfMemoryError.*(?:\\n\\s+.*)*` | pattern `<_> <errorMessage> duration<_>` [5m]))",
    #                     "intervalMs": 1000,
    #                     "maxDataPoints": 43200,
    #                     "queryType": "instant",
    #                     "refId": "A"
    #                 }
    #             }
    #         ],
    #         "noDataState": "OK",
    #         "execErrState": "OK",
    #         "for": "5m",
    #         "annotations": {
    #             "ErrorMessage": "Out Of Memory Error Occurred",
    #             "Instance URL": "&InstanceURL",
    #             "summary": "Out Of Memory Error Occurred"
    #         },
    #         "labels": {
    #             "Team": "&Instance",
    #             "Type": "Error Alerts",
    #             "alert-rule-id-type": "&Instance-alert",
    #             "severity": "error"
    #         },
    #         "isPaused": false
    #     },
    #     {
    #         "uid": "f69b047c-9b06-4563-846e-36bb7a4ecf76",
    #         "title": "Another Rule",
    #         "condition": "C",
    #         "data": [
    #             {
    #                 "refId": "A",
    #                 "queryType": "instant",
    #                 "relativeTimeRange": {
    #                     "from": 600,
    #                     "to": 0
    #                 },
    #                 "datasourceUid": "b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5",
    #                 "model": {
    #                     "datasource": {
    #                         "type": "loki",
    #                         "uid": "b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5"
    #                     },
    #                     "editorMode": "code",
    #                     "expr": "sum by(errorMessage) (count_over_time(&JobName |~ `java\\.lang\\.OutOfMemoryError.*(?:\\n\\s+.*)*` | pattern `<_> <errorMessage> duration<_>` [5m]))",
    #                     "intervalMs": 1000,
    #                     "maxDataPoints": 43200,
    #                     "queryType": "instant",
    #                     "refId": "A"
    #                 }
    #             }
    #         ],
    #         "noDataState": "OK",
    #         "execErrState": "OK",
    #         "for": "5m",
    #         "annotations": {
    #             "ErrorMessage": "Another Error Occurred",
    #             "Instance URL": "&InstanceURL",
    #             "summary": "Another Error Occurred"
    #         },
    #         "labels": {
    #             "Team": "&Instance",
    #             "Type": "Another Type",
    #             "alert-rule-id-type": "&Instance-alert",
    #             "severity": "error"
    #         },
    #         "isPaused": false
    #     }
    # ]