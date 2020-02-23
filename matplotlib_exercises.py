import matplotlib.pyplot as plt
import pandas as pd
import os
data = pd.read_csv('/Users/ozgecaylioglu/insurance.csv')
os.makedirs('plots',exist_ok = True)

plt.plot(data['charges'])
plt.title('charges')
plt.savefig(f'plots/charges_plt.png',format='png')
plt.show()
plt.clf()

plt.hist(data['bmi'], bins=5, color= 'r')
plt.title('bmi')
plt.savefig(f'plots/bmi_hist.png',format='png')
plt.show()
plt.clf()

plt.scatter(data['age'],data['charges'], c= 'm' )
plt.title('Age-Charge')
plt.xlabel('age')
plt.ylabel('charges')
plt.savefig(f'plots/age_charge_scatter.png', format='png')
plt.show()
plt.clf()

print(data[['charges','age','bmi','children']].corr())
plt.scatter(data['charges'], data['age'], data['bmi'],data['children'])
plt.scatter(data['charges'],data['age'], label= 'age')
plt.scatter(data['charges'],data['bmi'], label= 'bmi')
plt.scatter(data['charges'],data['children'], label= 'children')
plt.legend(loc='upper right',fontsize='small')
plt.xlabel('charges')
plt.title('Correlation of age, bmi, charges, children')
plt.savefig(f'plots/correlation.png',format='png')
plt.show()
plt.clf()
#correlation of charges and age
plt.scatter(data['charges'],data['age'], c= 'r')
plt.xlabel('charges')
plt.ylabel('age')
plt.title('Charges-Age')
plt.savefig(f'plots/charges-age.png',format='png')
plt.show()
plt.clf()

#correlation of children and bmi
plt.scatter(data['children'],data['bmi'], c= 'c')
plt.xlabel('children')
plt.ylabel('bmi')
plt.title('Bmi-Children')
plt.savefig(f'plots/children-bmi.png',format='png')
plt.show()
plt.clf()

#correlation of charges and children
plt.scatter(data['charges'],data['children'])
plt.title('Charges-Children')
plt.xlabel('charges')
plt.ylabel('children')
plt.savefig(f'plots/charges-children.png',format='png')
plt.show()
plt.clf()