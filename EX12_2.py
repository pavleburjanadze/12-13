import boto3

client = boto3.client('rds')

def create_rds_snap(identifier):
    response = client.create_db_snapshot(
        DBInstanceIdentifier=identifier,
        DBSnapshotIdentifier='snapshot',
    )
    print(response)


def parse_args():
   parser = argparse.ArgumentParser()
   parser.add_argument("-i", "--instance", type=str, help="Instance id", required=True)
   args = parser.parse_args()
   return args


def main():
   args = parse_args()
   identifier = f"{args.instance}"
   create_rds_snap(identifier)


if __name__ == "__main__":
   main()








