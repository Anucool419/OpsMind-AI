test_cases = [

    {
        "name": "Kubernetes OOM",
        "monitoring_source": "Kubernetes",
        "incident_type": "OOM Crash",
        "query": "Pod restarted due to memory exhaustion",
        "expected_keyword": "OOMKilled",
        "expected_severity": "CRITICAL",
        "expected_root_cause": "memory"
    },

    {
        "name": "Database Exhaustion",
        "monitoring_source": "Database",
        "incident_type": "Database Exhaustion",
        "query": "Database connection timeout and HikariPool exhaustion",
        "expected_keyword": "ConnectionTimeoutException",
        "expected_severity": "HIGH",
        "expected_root_cause": "connection"
    },

    {
        "name": "API Failure",
        "monitoring_source": "API Gateway",
        "incident_type": "API Failure",
        "query": "HTTP 429 downstream API failure",
        "expected_keyword": "Too Many Requests",
        "expected_severity": "HIGH",
        "expected_root_cause": "rate limit"
    }
]