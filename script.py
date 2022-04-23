# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

conversion = {"M": 1000000,
              "B": 1000000000}
# write your update damages function here:
up_damages_list = []
def up_damages():
    for damage in damages:
        if "M" in damage:
            up_damages_list.append(float(damage[:-1]) * conversion["M"])
        elif "B" in damage:
            up_damages_list.append(float(damage[:-1]) * conversion['B'])
        else:
            up_damages_list.append("Damages not recorded")

up_damages()
#print(up_damages_list)

# write your construct hurricane dictionary function here:
hurricane_data_dict = {}
def hurricane_data():
    for index in range(len(deaths)):
        hurricane_data_dict[names[index]] = {"Name": names[index],
                                             "Month": months[index],
                                             "Year" : years[index],
                                             "Max Sustained Wind" : max_sustained_winds[index],
                                             "Areas Affected" : areas_affected[index],
                                             "Damage" : damages[index],
                                             "Deaths" : deaths[index]}


hurricane_data()
#print(hurricane_data_dict)

# write your construct hurricane by year dictionary function here:

years_dict= []

for n, m, y, ma, a, da,  z in zip(names, months, years, max_sustained_winds, areas_affected, up_damages_list, deaths):
    dict = {y: {'Name': n, 'Month':m, 'Year': y, 'Max_sustained_wind': ma, 'Area_affected': a, 'Damage': da, 'Deaths': z}}
    years_dict.append(dict)

#print(years_dict)



# write your count affected areas function here:
affected_area_count = {}
def affected_areas():
    for i in areas_affected:
        for b in i:
            if b not in affected_area_count:
                affected_area_count[b] = 1
            else:
                affected_area_count[b] += 1

affected_areas()
#print(affected_area_count)

# write your find most affected area function here:

def max_areas_affected(affected_area_count):
    max_area = ""
    max_area_count = 0

    for a in affected_area_count:
        if affected_area_count[a] > max_area_count:
            max_area = a
            max_area_count = affected_area_count[a]
    return max_area, max_area_count


max_area, max_count = max_areas_affected(affected_area_count)
#print(max_area, max_count)




# write your greatest number of deaths function here:

def hurricane_by_deaths(hurricane):
    deadliest_area = ""
    deadliest_area_count = 0

    for index in hurricane:
        if hurricane[index]["Deaths"] > deadliest_area_count:
            deadliest_area = index
            deadliest_area_count = hurricane[index]["Deaths"]
    return deadliest_area, deadliest_area_count


deadliest_area, deadlist_area_count = hurricane_by_deaths(hurricane_data_dict)
#print(deadliest_area)
#print(deadlist_area_count)

# write your catgeorize by mortality function here:







# write your greatest damage function here:







# write your catgeorize by damage function here:
