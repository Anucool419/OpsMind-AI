knowledge_base = [
    {
        "incident": """
        Incident Pattern:
        OOMKilled Pod CrashLoopBackOff memory limit allocation slice

        Root Cause:
        The container exceeded its configured cgroup memory boundaries specified in the Kubernetes deployment manifest.

        Recommended Remediation:
        kubectl set resources deployment/{{deployment_name}} --limits=memory=1Gi -n default
        """
    },

    {
        "incident": """
        Incident Pattern:
        ConnectionTimeoutException HikariPool Connection lease leak database connection pool exhausted postgres

        Root Cause:
        The application layer is holding on to unclosed connections or suffering from unindexed nested database lock waits.

        Recommended Remediation:
        Check application metrics for active connections.
        Run:
        SELECT pg_terminate_backend(pid)
        FROM pg_stat_activity
        WHERE state = 'idle';
        """
    },

    {
        "incident": """
        Incident Pattern:
        HTTP 429 Too Many Requests downstream unhandled KeyError payment crashed

        Root Cause:
        The system hit a vendor API threshold, and the code failed to safely catch and parse a non-200 JSON object wrapper.

        Recommended Remediation:
        Implement exponential backoff retry logic utilizing the Retry-After header.
        """
    }
]