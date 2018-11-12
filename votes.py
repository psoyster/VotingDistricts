import re
import requests
import matplotlib.pyplot as plt
import numpy as np

states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
          "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
          "Illinois",
          "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
          "Maryland",
          "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
          "Montana",
          "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
          "New York",
          "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
          "Pennsylvania",
          "Rhode Island", "South Carolina", "South Dakota", "Tennessee",
          "Texas", "Utah",
          "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin",
          "Wyoming"]


def party_count(state_):
    d_count = 0
    r_count = 0
    i = 0
    j = 0
    for i in range(len(state_)):
        for j in state_:
            if state_[i][2] == 'R':
                r_count += 1
                break
            elif state_[i][2] == 'D':
                d_count += 1
                break
    return d_count, r_count


def pvi(state_):
    diff = 0
    i = 0
    avg = 0
    # for i in range(len(state_)):

    for i in range(len(state_)):
        name = state_[0][0]
        if state_[i][2] == 'R':
            diff += int(state_[i][3])

        elif state_[i][2] == 'D':
            diff -= int(state_[i][3])
        else:
            continue
        # i += 1


    avg = diff / (i+1)
    if diff > 0:
        return "%s leans Right with an average of %.3f" % (name, abs(avg))
    elif diff < 0:
        return "%s leans Left with an average of %.3f" % (name, abs(avg))


def tipover(dists):
    dem_w = 0
    rep_w = 0
    i = 0

    for i in dists:
        if (dists[i][2] == 'R' & dists[i][3] >= '+1') or (dists[i][2] == 'D'):
            dem_w = +1

        if (dists[i][3] == 'D' & dists[i][3] >= '+6') or (dists[
                                                              i][2] == 'R'):
            rep_w

    return "Dem Wins: %d\n Rep wins: %d" % dem_w, rep_w


# def state_group(country):

def main():
    url = r"http://euclid.nmu.edu/~rappleto/Classes/CS295.Python/Assignments/elections-data.txt"


    text = requests.get(url).text

    # print(text)

    regex = r'^([A-Z][a-z ]+) ([A-Z]?[\d]+),([A-Z]+)([\+]?[\d]+)?$'
    districts = re.findall(regex, text, (re.I | re.M))
    state = []

    i = 0
    j = 0
    for i in range(len(districts)):
        for j in range(len(states)):
            if districts[i][0] != states[j]:
                continue
            elif districts[i][0] == states[j]:
                state.append(districts[i])
                break

    # i=0
    # j=0
    # for i in range(len(state)):
    #     for j in state:
    #         state[i][1] = int(state[i][1])
    #         if state[i][2] == 'R':
    #             state[i][3] *= -1
    # d_count = 0
    # r_count = 0
    pc = party_count(state)
    print("The number of Dem districts is: {0}\n"
          "While the number of Rep districts is: {1}".format(pc[0], pc[1]))

    # tipover(state)

    pvi_req = input("Input a state to calculate PVI:")
    pvi_data = []
    for i in range(len(state)):
        if state[i][0] == pvi_req:
            pvi_data.append(state[i])

    print(pvi(pvi_data))

    global cont
    cont = input("Continue?").lower()







if __name__ == '__main__':
    cont = 'yes'
    while cont != 'no':
        main()
