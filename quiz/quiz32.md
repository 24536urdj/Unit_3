### 
    import requests
    import matplotlib.pyplot as plt
    import numpy as np


    req = requests.get('http://192.168.6.142/readings')
    data = req.json()
    readings = data["readings"][0]

    # get only temperature
    T1 = []
    T2 = []
    for sample in readings:
        if sample["sensor_id"] == 10:
            T1.append(sample["value"])
        if sample["sensor_id"] == 9:
            T2.append(sample["value"])

    # every 12 samples calculate the mean and std
    number_samples_per_hour = 12
    mean_per_hour = []
    x = []
    for t in range(0, len(T1), number_samples_per_hour):
        t_hour = T1[t:t+number_samples_per_hour]    # 12 values
        mean_per_hour.append(sum(t_hour)/len(t_hour))
        x.append(t)

    # smoothing
    x2 = []
    mean_per_hour2 = []
    diff = []
    for i in range(len(mean_per_hour)):
        d = mean_per_hour[i]-mean_per_hour2[i]
    for t in range(0, len(T2), number_samples_per_hour):
        t_hour = T2[t:t+number_samples_per_hour]    # 12 values
        mean_per_hour2.append(sum(t_hour)/len(t_hour))
        diff.append(d)

        fig = plt.figure(figsize=(9, 6))
        plt.subplot(3, 1, 1)
        plt.title("Sensor 9")
        plt.plot(x2, mean_per_hour2)
        plt.subplot(3, 1, 2)
        plt.title("Sensor 10")
        plt.plot(x, mean_per_hour)
        plt.subplot(3, 1, 3)
        plt.plot(x, diff)
        plt.show()
