"""Program takes 3 variables as inputs I.E. Number of test cases Number of People and The cost array in the given order respectively"""

no_of_test_cases=int(input())
for _ in range(no_of_test_cases):
    no_of_people=int(input())
    cost_list=list(map(int,input().split()))
    cost_list.sort()
    cost=0
    while(no_of_people>3):
        """ As seen in the sample test cases, either the lowest costing person can make 2 round trips with the highest costing people
            or the 2 lowest costing people can go first followed by the lowest costing person returning and then the 2 highest costing person going
            to the temple and the second lowest person returning, whichever is the lowest among these 2(As seen in 1st and 4th test case)"""
        #2*cost_list[0]+cost_list[no_of_people-1]+cost_list[no_of_people-2] for when the lowest cost returns twice
        #cost_list[0]+2*cost_list[1]+cost_list[no_of_people-1] for when the 2 of the lowest go first and then each one retuns starting with the lowest
        #this can also be done by checking if the lowest cost+ second highest cost is greater or lesser than 2 times 2nd lowest cost 
        cost+=min((2*cost_list[0]+cost_list[no_of_people-1]+cost_list[no_of_people-2]),(cost_list[0]+2*cost_list[1]+cost_list[no_of_people-1]))
        """Loop will run until there are less than 3 people left to go to the temple, reducing the length of the list by 2 each time the above method
           is repeated"""
        no_of_people-=2
    if(no_of_people==3):
        #cost of 3 people can be seen as the highest and lowest going, the lowest returning then the second highest and lowest going, that is the sum of thier costs
        cost+=cost_list[0]+cost_list[1]+cost_list[2]
    elif(no_of_people==2):
        #whichever of the two is higher should be added to the cost
        cost+=cost_list[1]
    else:
        cost+=cost_list[0]
    print(cost)
