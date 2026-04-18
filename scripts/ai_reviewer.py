import json
import sys
import boto3
import os

def get_bedrock_client():
    return boto3.client(service_name='bedrock-runtime', region_name=os.environ.get('AWS_REGION', 'us-east-1'))

def analyze_plan(plan_json):
    client = get_bedrock_client()
    
    # Extract meaningful parts of the plan to keep the prompt size manageable
    resource_changes = plan_json.get('resource_changes', [])
    summary = []
    
    for change in resource_changes:
        address = change.get('address')
        actions = change.get('change', {}).get('actions', [])
        summary.append(f"Resource: {address}, Actions: {actions}")

    prompt = f"""
    You are a Senior Cloud Security and DevOps Engineer. Your task is to review a Terraform plan and decide if it should be APPROVED or REJECTED.
    
    Focus on:
    1. Security risks (e.g., public S3 buckets, open security groups, lack of encryption).
    2. Cost anomalies (e.g., accidental deletion of expensive resources, provisioning of high-cost instances).
    3. Best practices (e.g., missing tags, non-compliant naming).

    Terraform Plan Summary:
    {json.dumps(summary, indent=2)}

    Full Plan Details (partial):
    {json.dumps(resource_changes, indent=2)[:10000]} 

    Provide your review in the following format:
    DECISION: [APPROVED or REJECTED]
    REASON: [Short explanation of your decision]
    SUGGESTIONS: [Any improvements]
    """

    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 2048,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    })

    model_id = 'anthropic.claude-sonnet-4-6'
    
    try:
        response = client.invoke_model(
            body=body,
            modelId=model_id,
            accept='application/json',
            contentType='application/json'
        )
        
        response_body = json.loads(response.get('body').read())
        review_text = response_body['content'][0]['text']
        return review_text
    except Exception as e:
        print(f"Error calling Bedrock: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python ai_reviewer.py <plan_json_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    with open(file_path, 'r') as f:
        plan_json = json.load(f)

    print("--- Starting AI Review of Terraform Plan ---")
    review = analyze_plan(plan_json)
    print(review)
    print("--- End of AI Review ---")

    if "DECISION: REJECTED" in review:
        print("AI Review failed. Deployment blocked.")
        sys.exit(1)
    else:
        print("AI Review passed. Deployment can proceed.")
        sys.exit(0)

if __name__ == "__main__":
    main()
