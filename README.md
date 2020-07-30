# mockGoogleCodingInterview

So this is my take on Clément Mihailescu's Mock Googling Coding Interview that he did with Tech With Tim,you can see the video [here](https://www.youtube.com/watch?v=3Q_oYDQ2whs)

So the idea is you have two people who are trying to set up a meeting, and they have to figure out which time they can set the meeting in by factoring their other plans, office hours, and meeting duration.

# How I Solved It
1. Merge the two calendars together
2. Merge the office hours (bounds)
3. Look through the merged calendar for suitable time, which is the time in between their plans which are greater than or equals to the meeting duration

It is a very interesting problem and very fun to try to solve! I'm sure that my code is not perfect and might have some problems, let me know if you have anything to add to it.
