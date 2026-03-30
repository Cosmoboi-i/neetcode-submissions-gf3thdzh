class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speeds = {}

        for i in range(len(position)):
            speeds[position[i]] = speed[i]
        
        speeds = dict(sorted(speeds.items(), reverse=True))

        timeTakenPrev = -1

        ans = 0

        for pos in speeds:
            speed = speeds[pos]
            dist = target - int(pos)

            if timeTakenPrev == -1:
                timeTakenPrev = dist / speed
                continue
            timeTaken = dist / speed

            if timeTaken > timeTakenPrev:
                timeTakenPrev = timeTaken
                ans += 1

        
        return ans + 1
