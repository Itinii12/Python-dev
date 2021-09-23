# AWS リソースへのアクセス
import boto3
# データ処理、機械学習のための計算がやりやすい。行列計算とかが出来る
import numpy as np
# Dataframe ぐらいしか分らん
import pandas as pd
# グラフがかける
import matplotlib.pyplot as plt
# parquetの提供元
import pyarrow as pa


def dynamodb_test():
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("dev-table")
    response = table.put_item(Item={'k': 'test01', 'date': '2021-8-11'})
    print(response)
    print(type(response['ResponseMetadata']))
    for key, value in response['ResponseMetadata'].items():
        print(key)
        print(value)


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


def pyarrow_test():
    data = b"qawsedrftgyhujikolp;"
    buf = pa.py_buffer(data)

    # buf分のメモリは確保されていないらしい
    print(f'{buf=}')
    print(f'{buf.size=}')


if __name__ == "__main__":
    print("main start.")
    pyarrow_test()
    print("main end.")

