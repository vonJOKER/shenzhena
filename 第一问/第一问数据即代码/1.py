import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set(style="whitegrid", font='SimHei')


data = pd.read_csv('data.csv', encoding='GBK')


smoking_status_count = data['是否吸烟'].value_counts()


plt.figure(figsize=(8, 6))
plt.pie(smoking_status_count, labels=['不吸烟', '吸烟', '过去吸烟现已戒烟'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title('吸烟情况比例')
plt.axis('equal')
plt.show()


smokers_data = data[data['是否吸烟'] == 1]
average_start_age = smokers_data['开始吸烟年龄'].mean()
average_weekly_days = smokers_data['平均每周吸烟天数'].mean()
average_daily_amount = smokers_data['一天吸烟支数'].mean()


passive_smoking_days = data[data['是否吸烟'] == 3]['被动吸烟天数'].mean()


print(f"吸烟者开始吸烟的平均年龄: {average_start_age:.2f} 岁")
print(f"吸烟者平均每周吸烟天数: {average_weekly_days:.2f} 天")
print(f"吸烟者平均每天吸烟支数: {average_daily_amount:.2f} 支")
plt.savefig('吸烟情况.png', dpi=600)

print(f"不吸烟或已戒烟者被动吸烟超过15分钟的平均天数: {passive_smoking_days:.2f} 天")
