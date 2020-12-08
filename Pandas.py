from pandas import Series

date = ['2018-08-01', '2018-08-02','2018-08-03', '2018-08-04', '2018-08-05']
xrp_close = [512,508,507,500,501]
s = Series(xrp_close,index=date)

s['2018-08-06'] = 400
print(s.drop('2018-08-01'))
print(s)

my_list = [100,200,300,400]

new_list = []
for val in my_list:
    new_list.append(val/10)

print(new_list)
