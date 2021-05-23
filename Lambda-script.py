import json
import boto3

regionBoto = boto3.client('ec2')
response = regionBoto.describe_regions()['Regions']

def lambda_handler(event, context):
    i = 0
    regions=response
    #print(regions)
    all_region = [region['RegionName'] for region in regions]
    while i < len(all_region):
         j = all_region[i]
         ec2 = boto3.resource('ec2',region_name=j)
         instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])  #this will terminate only running instance
         #instances = ec2.instances.filter()     # this will help you to terminate all instances
         for instance in instances:
           print(j, instance.id, instance.instance_type)
           instance = ec2.Instance(instance.id)
           print(instance.terminate())
         i += 1
