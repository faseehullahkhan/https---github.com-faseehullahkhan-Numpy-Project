import numpy as na
import matplotlib.pyplot as plt
taxi = na.genfromtxt('nyc_taxis.csv' , delimiter=',' ,dtype= str, skip_header=True)
print(taxi)


# speed = taxi[:, 7] / (taxi[:, 8] / 3600)
# mean_speed = speed.mean()
# # print(mean_speed)

# rides_feb = taxi[taxi[:, 1] == 2  , 1]  
# # print(rides_feb.shape[0])

# tips= taxi[taxi[:, -3] > 50 , -3].shape[0]
# # print(tips)

# code= taxi[taxi[:, 6] == 2 , 6].shape[0]
# # print(code)

# plt.figure()  # Create a new figure
# plt.scatter('trip_distance', mean_speed, alpha=0.5)  # Plot scatter
# plt.xlabel('Trip Distance (miles)')  # X-axis label
# plt.ylabel('Mean Speed (mph)')       # Y-axis label
# plt.title('Trip Distance vs Mean Speed')  # Plot title
# plt.show()

# months = taxi[:, 1]
# rides_per_month = [na.sum(months == i) for i in range(1, 13)]
# plt.figure()
# plt.bar(range(1, 13), rides_per_month, color='green', edgecolor='black')
# plt.xlabel('Month')
# plt.ylabel('Number of Rides')
# plt.title('Rides Per Month')
# plt.xticks(range(1, 13))  # Label each month
# plt.show()


# plt.figure()
# plt.scatter(taxi[:, 7], taxi[:, -4] , alpha=0.5 , color = 'red')
# plt.xlabel('Trip Distance (miles)')
# plt.ylabel('Fare Amount ($)')
# plt.title('Trip Distance vs Fare Amount')
# plt.show()

# high_tips = taxi[taxi[:, -3] > 20]
# low_tips = taxi[taxi[:, -3] <= 20]

# avg_distance_high = high_tips[:, 7].mean()
# avg_distance_low = low_tips[:, 7].mean()

# avg_length_high = high_tips[:, 8].mean()
# avg_length_low = low_tips[:, 8].mean()

# labels = ['High Tips', 'Low Tips']
# distances = [avg_distance_high, avg_distance_low]
# lengths = [avg_length_high, avg_length_low]

# plt.figure()
# plt.bar(labels, distances, color='blue', alpha=0.7, label='Avg Distance (miles)')
# plt.bar(labels, lengths, color='green', alpha=0.7, label='Avg Trip Length (sec)', bottom=distances)
# plt.xlabel('Tip Category')
# plt.ylabel('Average Value')
# plt.title('Comparison of High and Low Tip Rides')
# plt.legend()
# plt.show()


