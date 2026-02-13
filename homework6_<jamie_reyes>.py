web_users = ["jamiea", "jamieb", "jamiec", "jamied", "jamiee"]
new_users = ["jamiea", "jamieb" "jamiez", "jamiey", "jamiex"]
def has_common_value(web_users, new_users):
        for value in web_users:
                if value in new_users:
                    return True
        return False
if has_common_value(web_users, new_users):
        print("This user name is already in use. Please choose a different user name.")
else:
       print("This user name is available.")

cities = {
        'Seattle': {
              'city': 'Seattle',
              'country': 'United States',
              'population': '816_600',
              'fact': 'The Seattle Seahawks have won the superbowl in 2014 and 2026'
        },
        
        'Tokyo': { 
              'city': 'Tokyo',
              'country': 'Japan',
              'population': '14_000_000',
              'fact': 'Tokyo was formerly known as Edo, but changed to mark the shift from shogun rule to imperial power'
        },

        'Berlin': { 
              'city': 'Berlin',
              'country': 'Germany',
              'population': '8_000_000',
              'fact': 'Berlin has more bridges than Venice, along with more canals and rivers'
        }
}

original_dict_city = {
       "Seattle": {"city", "country", "population", "fact"},
       "Tokyo": {"city", "country", "population", "fact"},
       "Berlin": {"city", "country", "population", "fact"}
}

print("original_dict_city")
