import boto3
client = boto3.client('ec2')
ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
for region in ec2_regions:
    ec2 = boto3.resource('ec2', region_name=region)
    volumes = ec2.volumes.filter(Filters=[{'Name': 'status', 'Values': ['in-use']}])
            for volume in volumes:
                        print(volume.id) 



volumes = ec2.volumes.all() 
