"""
The key observation is that cars cannot pass one another, so a faster car behind a slower car may eventually catch up and become part of the same fleet. 
Instead of simulating the cars' movement, compute the time each car would take to reach the target using `(target - position) / speed`. 
Then sort the cars by position in descending order so that you process them from closest to the target to farthest. 
As you scan through the sorted cars, keep track of the arrival time of the fleet directly ahead. 
If the current car's arrival time is greater than the maximum arrival time seen so far, it cannot catch the fleet in front and therefore forms a new fleet. 
Otherwise, its arrival time is less than or equal to the fleet ahead's arrival time, meaning it will catch up before reaching the target and merge into that fleet. 
By counting how many times a new maximum arrival time appears during the scan, you obtain the total number of car fleets.
 This approach avoids simulation and runs in (O(n \log n)) time due to sorting, with a single (O(n)) pass afterward.
"""



class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        cars = sorted(zip(position, speed), reverse=True)
    
        fleets = 0
        max_time = 0.0
        
        for pos, spd in cars:
            time = float(target - pos) / spd
            if time > max_time:
                fleets += 1
                max_time = time
        
        return fleets
        