months = [
            'Jan',
			'Feb',
			'Marc',
			'April',
			'May',
			'June',
			'July',
			'Aug',
			'Sept',
			'October',
			'Nov',
			'Dec'
			]
endings=['st','nd','rd']+17*['th']\
         +['st','nd','rd']+7*['th']+['st']

year = raw_input('Year:')
month = raw_input('Month:')
day = raw_input('Day:')
month_num = int(month)
day_num = int(day)

month_name = months[month_num-1]
ordi = day + endings[day_num-1]

print month_name + ' ' + ordi + ',' + year 
