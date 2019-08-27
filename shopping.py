#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Author: Mathew McDade
    Date: 1/27/2019
    Description: A Dynamic Programming implementation of a complex 0-1 knapsack problem. The
    program reads input from a file, shopping.txt, and prints the results including Total Price
    and Item selection to an output file, results.txt. The program achieves efficiency by
    creating a single memoized knapsack table for the largest capacity member of a family and
    simply backtracing from earlier points in the table for smaller capacity members.
"""


# The shopping function performs the primary knapsack function, taking a family and list of items,
#   memoizing a table for the families maximum capacity, and returning that table.
def shopping(family, items):
    sack = [[0 for x in range(max(family)+1)] for y in range(len(items)+1)]

    for item in range(1, len(items)+1):
        val = items[item-1]['price']
        wt = items[item-1]['weight']
        for load in range(1, max(family) + 1):
            if wt > load:
                sack[item][load] = sack[item-1][load]
            else:
                sack[item][load] = max(sack[item-1][load], sack[item-1][load-wt] + val)

    fam_cart = []
    for member in family:
        fam_cart.append(backtrace_items(member, sack, items))

    print(fam_cart)
    print(sack)
    return sack


# Backtraces the table for a member and returns a cart listing the items that member should select.
def backtrace_items(member, sack, items):
    cart = []
    capacity = member
    for item in range(len(items), 0, -1):
        keep = sack[item][member] != sack[item-1][member]

        if keep:
            val = items[item-1]['price']
            wt = items[item-1]['weight']
            cart.append(items[item-1])
            member -= wt

    return cart

# MAIN
if __name__ == "__main__":
    with open("shopping.txt", "r") as ifile:  # read and parse integer lists from file.
        with open("results.txt", "w+") as ofile:  # write formatted output to file.
            Test_Cases = int(ifile.readline())
            for i in range(Test_Cases):
                Items = []  # array of dicts for item prices and weights.
                Family = []  # array of for family member maximum weight capacities.
                N = int(ifile.readline())
                for n in range(N):
                    line = ifile.readline()
                    data = line.split()
                    Items.append({'price': int(data[0]), 'weight': int(data[1])})
                F = int(ifile.readline())
                for f in range(F):
                    Family.append(int(ifile.readline()))

                test_case = shopping(Family,Items)
                print(test_case)
                family_total = 0
                for member in Family:
                    print(member, test_case[len(Items)][member])
                    print("\n")
                    family_total += test_case[len(Items)][member]
                print(family_total)
                    # write results to file.
                # ofile.write("Test Case: %i \n" % (i + 1))
                # ofile.write("Total Price: {} \n".format(family_total))
                # ofile.write("Member Items\n")
                # for member in range(1, len(Family)+1):
                #     family_items = (backtrace_items(test_case, member, Items))
                #     ofile.write(
                #         "Member:{} Capacity:{}: Items:{} Value:{}\n".format(member, Family[member-1], family_items, max(test_case[member])))
                # ofile.write("\n")
