import boto3


def dynamodb_test():
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("dev-table")
    response = table.put_item(Item={'k': 'test01', 'date': '2021-8-11'})
    print(response)
    print(type(response['ResponseMetadata']))
    for key, value in response['ResponseMetadata'].items():
        print(key)
        print(value)


def python_study():
    a = 1
    print(a)


if __name__ == "__main__":
    dynamodb_test()

