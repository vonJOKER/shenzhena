import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('data.csv',encoding='GBK')
not_eating_breakfast_avg = data['不吃早餐'].mean()
not_eating_lunch_avg = data['不吃中餐'].mean()
not_eating_dinner_avg = data['不吃晚餐'].mean()

eating_at_home_breakfast_avg = data['在家吃早餐'].mean()
eating_at_home_lunch_avg = data['在家吃中餐'].mean()
eating_at_home_dinner_avg = data['在家吃晚餐'].mean()

carry_to_work_breakfast_avg = data['早餐带餐到单位'].mean()
carry_to_work_lunch_avg = data['中餐带餐到单位'].mean()
carry_to_work_dinner_avg = data['晚餐带餐到单位'].mean()

cafeteria_breakfast_avg = data['单位食堂早餐'].mean()
cafeteria_lunch_avg = data['单位食堂中餐'].mean()
cafeteria_dinner_avg = data['单位食堂晚餐'].mean()

restaurant_breakfast_avg = data['在餐馆或街头吃早餐'].mean()
restaurant_lunch_avg = data['在餐馆或街头吃中餐'].mean()
restaurant_dinner_avg = data['在餐馆或街头吃晚餐'].mean()

home_weekday_breakfast_avg = data['工作日在家吃早餐人数'].mean()
home_weekday_lunch_avg = data['工作日在家吃中餐人数'].mean()
home_weekday_dinner_avg = data['工作日在家吃晚餐人数'].mean()

home_weekend_breakfast_avg = data['周末在家吃早餐人数'].mean()
home_weekend_lunch_avg = data['周末在家吃中餐人数'].mean()
home_weekend_dinner_avg = data['周末在家吃晚餐人数'].mean()


print("不吃早餐平均数:%.3f"%not_eating_breakfast_avg)
print("不吃中餐平均数:%.3f"%not_eating_lunch_avg)
print("不吃晚餐平均数:%.3f" %not_eating_dinner_avg)

print("在家吃早餐平均数:%.3f" %eating_at_home_breakfast_avg)
print("在家吃中餐平均数:%.3f" %eating_at_home_lunch_avg)
print("在家吃晚餐平均数:%.3f" %eating_at_home_dinner_avg)

print("早餐带餐到单位平均数:%.3f"% carry_to_work_breakfast_avg)
print("中餐带餐到单位平均数:%.3f"% carry_to_work_lunch_avg)
print("晚餐带餐到单位平均数:%.3f"% carry_to_work_dinner_avg)

print("单位食堂早餐平均数:%.3f"% cafeteria_breakfast_avg)
print("单位食堂中餐平均数:%.3f"% cafeteria_lunch_avg)
print("单位食堂晚餐平均数:%.3f"% cafeteria_dinner_avg)

print("在餐馆或街头吃早餐平均数:%.3f"% restaurant_breakfast_avg)
print("在餐馆或街头吃中餐平均数:%.3f"% restaurant_lunch_avg)
print("在餐馆或街头吃晚餐平均数:%.3f"% restaurant_dinner_avg)

print("工作日在家吃早餐人数平均数:%.3f"% home_weekday_breakfast_avg)
print("工作日在家吃中餐人数平均数:%.3f"% home_weekday_lunch_avg)
print("工作日在家吃晚餐人数平均数:%.3f"% home_weekday_dinner_avg)

print("周末在家吃早餐人数平均数:%.3f"% home_weekend_breakfast_avg)
print("周末在家吃中餐人数平均数:%.3f"% home_weekend_lunch_avg)
print("周末在家吃晚餐人数平均数:%.3f"% home_weekend_dinner_avg)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def plot_pie(labels, sizes, title):
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title(title)
    plt.show()


not_eating_avg = [not_eating_breakfast_avg, not_eating_lunch_avg, not_eating_dinner_avg]
plot_pie(['早餐', '中餐', '晚餐'], not_eating_avg, '不吃早、中、晚餐的平均比例')


eating_at_home_avg = [eating_at_home_breakfast_avg, eating_at_home_lunch_avg, eating_at_home_dinner_avg]
plot_pie(['早餐', '中餐', '晚餐'], eating_at_home_avg, '在家吃早、中、晚餐的平均比例')

carry_to_work_avg = [carry_to_work_breakfast_avg, carry_to_work_lunch_avg, carry_to_work_dinner_avg]
plot_pie(['早餐', '中餐', '晚餐'], carry_to_work_avg, '带餐到单位的平均比例')


cafeteria_avg = [cafeteria_breakfast_avg, cafeteria_lunch_avg, cafeteria_dinner_avg]
plot_pie(['早餐', '中餐', '晚餐'], cafeteria_avg, '单位食堂用餐的平均比例')


restaurant_avg = [restaurant_breakfast_avg, restaurant_lunch_avg, restaurant_dinner_avg]
plot_pie(['早餐', '中餐', '晚餐'], restaurant_avg, '餐馆或街头用餐的平均比例')


home_weekday_avg = [home_weekday_breakfast_avg, home_weekday_lunch_avg, home_weekday_dinner_avg]
plot_pie(['早餐', '中餐', '晚餐'], home_weekday_avg, '工作日在家用餐的平均比例')


home_weekend_avg = [home_weekend_breakfast_avg, home_weekend_lunch_avg, home_weekend_dinner_avg]
plot_pie(['早餐', '中餐', '晚餐'], home_weekend_avg, '周末在家用餐的平均比例')

