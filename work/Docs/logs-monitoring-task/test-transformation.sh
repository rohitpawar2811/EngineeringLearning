#!/bin/bash

# Your JSON data
json_data='
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
            "datasourceUid": "fdhe50ulz2i9sc",
            "model": {
                "datasource": {
                    "type": "loki",
                    "uid": "fdhe50ulz2i9sc"
                },
                "editorMode": "code",
                "expr": "sum by(errorMessage) (count_over_time({job=\"sm-uat.hotwax.io\"} |~ `java\\.lang\\.OutOfMemoryError.*(?:\\n\\s+.*)*` | pattern `<_> <errorMessage> duration<_>` [5m]))",
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
        "Instance URL": "https://sm-uat.hotwax.io/",
        "summary": "Out Of Memory Error Occurred"
    },
    "labels": {
        "Team": "SM-Uat",
        "Type": "Error Alerts",
        "alert-rule-id-type": "sm-uat-alert",
        "severity": "error"
    },
    "isPaused": false
}'

# Assign the Loki datasource UUID
loki_datasource_uuid="YOUR_LOKI_DATASOURCE_UUID"


if [[ $(echo "$json_data" | jq -r '.data[0].model.datasource.type') == "loki" ]]; then
    echo "Worked condition"
    # json_data=$(echo "$json_data" | jq '.data[0].model.datasource |= . + {"uid": "$loki_datasource_uuid"} | .data[0]. |= . + {"datasourceUid": "$loki_datasource_uuid"}')
    json_data=$(echo "$json_data" | jq --arg loki_datasource_uuid "$loki_datasource_uuid" '.data[0].model.datasource |= . + {"uid": $loki_datasource_uuid} | .data[0] |= . + {"datasourceUid": $loki_datasource_uuid}')
fi


echo "$json_data"
