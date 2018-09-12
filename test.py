import boto3
ec2 = boto3.client('ec2')
response = client.describe_volumes(
    Filters=[
        {
            'Name': 'string',
            'Values': [
                'string',
            ]
        },
    ],
    VolumeIds=[
        'string',
    ],
    DryRun=True|False,
    MaxResults=123,
    NextToken='string'
)