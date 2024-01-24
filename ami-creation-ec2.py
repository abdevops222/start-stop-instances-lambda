import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')

    # Specify instance IDs you want to create AMIs from
    instance_ids = ['i-0f360c9bd9946d697']

    # Create AMI for each instance
    for instance_id in instance_ids:
        response = ec2_client.create_image(
            InstanceId=instance_id,
            Name='AMI_Backup',
            Description='AMI_Description',
            NoReboot=True  # Set to True if you want to avoid rebooting the instance
        )
        print(f"AMI {response['ImageId']} created for instance {instance_id}")
