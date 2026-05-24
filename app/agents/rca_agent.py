from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_incident(logs, retrieved_context, monitoring_source='Unknown', incident_type='Unknown'):

    prompt = f"""
    You are an expert Site Reliability Engineer.

    Analyze the production incident.

    Relevant historical incidents:
    {retrieved_context}

    Current logs:
    {logs}
    
    Monitoring Platform:
    {monitoring_source}
    
    Expected Incident type:
    {incident_type}

    Tasks:
    1. Identify probable root cause
    2. Explain why the issue happened
    3. Identify impacted services
    4. Suggest remediation
    5. Assign severity level
    
    

Return the response in professional markdown format.

Include:

## 🧩 Root Cause

## 🛠 Affected Services

## 🔎 Evidence

## ✅ Recommended Fixes

## 🛡 Prevention Strategies

## 🚦 Severity

Return severity as ONLY one of:
CRITICAL
HIGH
MEDIUM
LOW
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

#Prompt strategy with st.code
# ROOT CAUSE:
# ...

# AFFECTED SERVICES:
# ...

# SEVERITY:
# ...

# EVIDENCE:
# ...

# RECOMMENDED FIXES:
# ...

# PREVENTION STRATEGIES:
# ...
def generate_timeline(logs):

    prompt = f"""
    Extract a chronological incident timeline from these logs.

    Return ONLY bullet points.

    Logs:
    {logs}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

def extract_impacted_services(logs):

    prompt = f"""
    Extract impacted services from these logs.

    Return ONLY bullet points.

    Logs:
    {logs}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

def classify_incident(logs):

    prompt = f"""
    Analyze these logs.

    Identify:

    1. Monitoring Source
    2. Incident Type
    3. Severity

    Return ONLY in this format:

    Monitoring Source: ...
    Incident Type: ....
    Severity: ..

    Do not add explanations.
    Do not add markdown.
    Do not add bullet points.
    
    Logs:
    {logs}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content