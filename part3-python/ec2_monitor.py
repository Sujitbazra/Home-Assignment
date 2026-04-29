import boto3
    import argparse
    import logging
    from datetime import datetime, timedelta
    import json
    
    logging.basicConfig(level=logging.INFO)
    
    def get_instances(region):
        ec2 = boto3.client('ec2', region_name=region)
        return ec2.describe_instances()
    
    def get_cpu_metrics(instance_id, region):
        cw = boto3.client('cloudwatch', region_name=region)
        end = datetime.utcnow()
        start = end - timedelta(hours=1)
    
        metrics = cw.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
            StartTime=start,
            EndTime=end,
            Period=300,
            Statistics=['Average', 'Minimum', 'Maximum']
        )
        return metrics
    
    def main():
        parser = argparse.ArgumentParser()
        parser.add_argument('--region', required=True)
        parser.add_argument('--threshold', type=int, default=80)
        parser.add_argument('--output', default='report.json')
    
        args = parser.parse_args()
    
        instances = get_instances(args.region)
    
        report = []
    
        for res in instances['Reservations']:
            for inst in res['Instances']:
                if inst['State']['Name'] != 'running':
                    continue
    
                metrics = get_cpu_metrics(inst['InstanceId'], args.region)
    
                datapoints = metrics['Datapoints']
                if not datapoints:
                    continue
    
                avg = sum(d['Average'] for d in datapoints) / len(datapoints)
                report.append({
                    "InstanceId": inst['InstanceId'],
                    "AvgCPU": avg,
                    "Alert": avg > args.threshold
                })
    
        with open(args.output, 'w') as f:
            json.dump(report, f, indent=2)
    
    if __name__ == "__main__":
        main()