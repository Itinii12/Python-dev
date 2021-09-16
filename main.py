import boto3
import numpy
import pandas
import drawdata
import matplotlib.pyplot as plt


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


def draw_data_test():
    # リファレンスには描画ウィンドウが出てくるとあるが、何故か出てこない
    drawdata.draw_scatter()


def draw_graph_test():
    price = [100, 250, 380, 500, 700]
    number = [1, 2, 3, 4, 5]

    # グラフを書く
    plt.plot(price, number)

    # グラフのタイトル
    plt.title("price / number")

    # x軸のラベル
    plt.xlabel("price")

    # y軸のラベル
    plt.ylabel("number")

    # グリッドを表示する
    plt.grid(True)

    # 表示する
    plt.show()


if __name__ == "__main__":
    draw_graph_test()

