import boto3

ec2_client = boto3.client("ec2")

vpc_id = "vpc-0adbe85ec200e9dba"


def create_security_group(name, description):
   response = ec2_client.create_security_group(
       Description=description,
       GroupName=name,
       VpcId=vpc_id
   )
   group_id = response.get("GroupId")
   print(group_id)
   return group_id


def add_access_sg():
   response = ec2_client.authorize_security_group_ingress(
       CidrIp=ip_address,
       FromPort=22,
       GroupId=sg_id,
       IpProtocol='tcp',
       ToPort=22,
   )





def create_postgres_instance():
   response = rds_client.create_db_instance(
       DBName='mysql',
       DBInstanceIdentifier='btu',
       AllocatedStorage=60,
       DBInstanceClass='db.t3.micro',
       Engine='mysql',
       MasterUsername='btu',
       MasterUserPassword='test',
       BackupRetentionPeriod=7,
       Port=3306,
       MultiAZ=False,
       EngineVersion='8.0',
       AutoMinorVersionUpgrade=False,
       PubliclyAccessible=True,
       Tags=[
           {
               'Key': 'Name',
               'Value': 'btu rds'
           },
       ],
       StorageType='gp2',
       EnablePerformanceInsights=True,
       PerformanceInsightsRetentionPeriod=7,
       DeletionProtection=False,
   )
   _id = response.get("DBInstance").get("DBInstanceIdentifier")
   print(f"Instance {_id} was created")


def main():
    create_security_group("RDS", "RDS for btu")
    create_postgres_instance()


if __name__ == "__main__":
   main()








