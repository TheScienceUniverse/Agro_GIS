import sys
import csv

S = [
	['Andhra Pradesh', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Arunachal Pradesh', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Assam', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Bihar', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Chhattisgarh', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Goa', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Gujarat', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Haryana', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Himachal Pradesh', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Jammu and Kashmir', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Jharkhand', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Karnataka', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Kerala', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Madhya Pradesh', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Maharashtra', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Manipur', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Meghalaya', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Mizoram', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Nagaland', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Odisha', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Punjab', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Rajasthan', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Sikkim', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Tamil Nadu', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Telangana', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Tripura', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Uttar Pradesh', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Uttarakhand', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['West Bengal', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Andaman and Nicobar Islands', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Chandigarh', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Dadra and Nagar Haveli', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Daman and Diu', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Delhi', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Lakshadweep', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['Puducherry', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

state = [
	'Apple.csv', 'Carrot.csv', 'Grapes.csv', 'Moong_Green_Gram.csv', 'Peas_vegetable.csv',
	'Sesamum.csv', 'Arcanut_Processed.csv', 'Cashewnut.csv', 'Groundnut.csv', 'Moth.csv',
	'Perilla.csv', 'Small_millets.csv', 'Arecanut.csv', 'Cashewnut_Processed.csv', 'Guar_seed.csv',
	'Niger_seed.csv', 'Pineapple.csv', 'Snak_Guard.csv', 'Arhar_Tur.csv', 'Cashewnut_Raw.csv',
	'Horse-gram.csv', 'Oilseeds_total.csv', 'Plums.csv', 'Soyabean.csv', 'Ash_Gourd.csv',
	'Castor_seed.csv', 'Jack_Fruit.csv', 'Onion.csv', 'Pome_Fruit.csv', 'Sugarcane.csv',
	'Atcanut_Raw.csv', 'Cauliflower.csv', 'Jobster.csv', 'Orange.csv', 'Pome_Granet.csv',
	'Sunflower.csv', 'Bajra.csv', 'Citrus_Fruit.csv', 'Jowar.csv', 'Other_Cereals_Millets.csv',
	'Potato.csv', 'Sweet_potato.csv', 'Banana.csv', 'Coconut.csv', 'Jute.csv',
	'Other_Citrus_Fruit.csv', 'Pulses_total.csv', 'Tapioca.csv', 'Barley.csv', 'Coffee.csv',
	'Jute_mesta.csv', 'Other_Dry_Fruit.csv', 'Pump_Kin.csv', 'Tea.csv', 'Bean.csv',
	'Colocosia.csv', 'Kapas.csv', 'other_fibres.csv', 'Ragi.csv', 'Tobacco.csv',
	'Beans_Mutte_Vegetable.csv', 'Cond-spcs_other.csv', 'Khesari.csv', 'Other_Fresh_Fruits.csv', 'Rajmash_Kholar.csv',
	'Tomato.csv', 'Beet_Root.csv', 'Coriander.csv', 'Korra.csv', 'Other_Kharif_pulses.csv',
	'Rapeseed_Mustard.csv', 'Total_foodgrain.csv', 'Ber.csv', 'Cotton_lint.csv', 'Lab-Lab.csv',
	'other_misc_pulses.csv', 'Redish.csv', 'Turmeric.csv', 'Bhindi.csv', 'Cowpea_Lobia.csv',
	'Lemon.csv', 'other_oilseeds.csv', 'Ribed_Guard.csv', 'Turnip.csv', 'Bitter_Gourd.csv',
	'Cucumber.csv', 'Lentil.csv', 'Other_Rabi_pulses.csv', 'Ricebean_nagadal.csv', 'Urad.csv',
	'Blackgram.csv', 'Drum_Stick.csv', 'Linseed.csv', 'Other_Vegetables.csv', 'Rice.csv',
	'Varagu.csv', 'Black_pepper.csv', 'Dry_chillies.csv', 'Litchi.csv', 'Paddy.csv',
	'Rubber.csv', 'Water_Melon.csv', 'Bottle_Gourd.csv', 'Dry_ginger.csv', 'Maize.csv',
	'Papaya.csv', 'Safflower.csv', 'Wheat.csv', 'Brinjal.csv', 'Garlic.csv',
	'Mango.csv', 'Peach.csv', 'Samai.csv', 'Yam.csv', 'Cabbage.csv', 'Ginger.csv',
	'Masoor.csv', 'Pear.csv', 'Sannhamp.csv', 'Cardamom.csv', 'Gram.csv',
	'Mesta.csv', 'Peas_beans_Pulses.csv', 'Sapota.csv'
]


# f_nm = sys.argv[1]

def find_index(s_nm):
	for i in range(36):
		if S[i][0] == s_nm:
			break
	return i

def find_year(s_yr):
	yi = int(s_yr)
	yi = yi - 1997 + 1
	return yi

# state_name,district_name,crop_year,season,crop,area,production

for s in range(124):
	T = S
	with open('data/' + state[s], 'r') as csv_fr:
		next(csv_fr)
		csv_r = csv.reader(csv_fr)
		for row in csv_r:
			i = find_index(row[0])
			y = find_year(row[2])
			T[i][y] = round(T[i][y] + float(row[5]), 2)
	csv_fr.close()

	with open('./out/' + state[s], 'w') as csv_fw:
		csv_w = csv.writer(csv_fw)
		csv_w.writerows(T)
	csv_fw.close()
	print(state[s])
