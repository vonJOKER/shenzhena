import pandas as pd
import matplotlib.pyplot as plt


csv_file_path = "data.csv"
data = pd.read_csv(csv_file_path, encoding='GBK')


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

drink_counts = data['是否饮酒'].value_counts()


labels = ['不饮酒', '饮酒', '已戒酒']
plt.figure(figsize=(8, 6))
plt.pie(drink_counts, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('饮酒情况分布')
plt.show()


drinkers_data = data[data['是否饮酒'] == 1]


average_years = drinkers_data['饮酒年数'].mean()


alcohol_columns = ['是否饮用高度白酒', '是否饮用低度白酒', '是否饮用啤酒', '是否饮用黄酒、糯米酒', '是否饮用葡萄酒']
alcohol_labels = ['高度白酒', '低度白酒', '啤酒', '黄酒、糯米酒', '葡萄酒']

average_freq = drinkers_data[alcohol_columns].mean()
average_amount = drinkers_data[alcohol_columns].mul(drinkers_data['饮用频率'], axis=0).sum() / drinkers_data['饮用频率'].sum()

print(f"平均饮酒年限：{average_years:.2f} 年")
print("每种酒类的饮用频率和饮用量：")
for label, freq, amount in zip(alcohol_labels, average_freq, average_amount):
    print(f"{label}：")
    print(f"  平均饮用频率：{freq:.2f} 次/周")
    print(f"  平均饮用量：{amount:.2f} 两")
