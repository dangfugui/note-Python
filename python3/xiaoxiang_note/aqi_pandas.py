# coding=utf-8


import pandas as pd
import matplotlib.pylab as plt
# 解决中文输出
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
"""
    统计
"""


def main():
    aqi_data = pd.read_csv("aqi.csv")
    print("基本数据：")
    print(aqi_data.info())
    print("数据预览")
    print(aqi_data.head(5))
    # print("AQI最大值：", aqi_data["AQI"].max)
    # print("AQI最小值：", aqi_data["AQI"].min)
    # print("AQI均值：", aqi_data["AQI"].mean)
    # top 10
    bottom10_city = aqi_data.sort_values(by=["AQI"], ascending=False).head(10)
    print("空气质量最坏的10个城市")
    print(bottom10_city)
    # top10.to_csv("aqi_top10.csv")
    clean_aqi_data = aqi_data[aqi_data["AQI"] > 0]  # 清洗掉 AQI = 0 的
    top10 = clean_aqi_data.sort_values(by=["AQI"]).head(10)
    print("空气质量最好的10个城市")
    print(top10)
    top10.plot(kind="bar", x="city_name", y="AQI", title="空气质量最好的城市", figsize=(20,10))
    # plt.save("image.png")
    plt.show()


if __name__ == '__main__':
    main()
