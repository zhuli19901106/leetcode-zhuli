# https://leetcode.com/problems/robot-room-cleaner/
# 1AC, gotta say this is the best interview question ever met
# challenging while very interesting, especially the simulation
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # up, right, down, left
        offsets = [(0, -1), (+1, 0), (0, +1), (-1, 0)]
        # start facing up
        oi = 0
        st = set()

        def dfs(x, y):
            nonlocal oi, st

            robot.clean()
            st.add((x, y))

            for i in range(4):
                x1, y1 = x + offsets[oi][0], y + offsets[oi][1]
                if (x1, y1) in st:
                    robot.turnRight()
                    oi = (oi + 1) % 4
                    continue

                ret = robot.move()
                if not ret:
                    st.add((x1, y1))
                    robot.turnRight()
                    oi = (oi + 1) % 4
                    continue

                dfs(x1, y1)
                for _ in range(2):
                    robot.turnRight()
                    oi = (oi + 1) % 4
                robot.move()
                robot.turnLeft()
                oi = (oi + 3) % 4

        # as a relative position (0, 0)
        dfs(0, 0)
