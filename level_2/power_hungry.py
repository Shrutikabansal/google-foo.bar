'''
Commander Lambda's space station is HUGE. And huge space stations take a LOT of power. Huge space stations with doomsday devices take even more power. To help meet the station's power needs, Commander Lambda has installed solar panels on the station's outer surface. But the station sits in the middle of a quasar quantum flux field, which wreaks havoc on the solar panels. You and your team of henchmen has been assigned to repair the solar panels, but you can't take them all down at once without shutting down the space station (and all those pesky life support systems!).

You need to figure out which sets of panels in any given array you can take offline to repair while still maintaining the maximum amount of power output per array, and to do THAT, you'll first need to figure out what the maximum output of each array actually is. Write a function answer(xs) that takes a list of integers representing the power output levels of each panel in an array, and returns the maximum product of some non-empty subset of those numbers. So for example, if an array contained panels with power output levels of [2, -3, 1, 0, -5], then the maximum product would be found by taking the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30. So answer([2,-3,1,0,-5]) will be "30".

Each array of solar panels contains at least 1 and no more than 50 panels, and each panel will have a power output level whose absolute value is no greater than 1000 (some panels are malfunctioning so badly that they're draining energy, but you know a trick with the panels' wave stabilizer that lets you combine two negative-output panels to produce the positive output of the multiple of their power values). The final products may be very large, so give the answer as a string representation of the number.

Languages
=========
To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java
Test cases
==========


Inputs:

(int list) xs = [2, 0, 2, 2, 0]
Output:

(string) "8"
Inputs:

(int list) xs = [-2, -3, 4, -5]
Output:

(string) "60"

Time to solve: 72 hours.
'''


def solution(xs):
    if len(xs) == 0:
        return str(0)
    if len(xs) == 1:
        return str(xs[0])

    p_array = []
    n_array = []
    for n in xs:
        if n > 0:
            p_array.append(n)
        elif n < 0:
            n_array.append(n)

    p_length = len(p_array)
    n_length = len(n_array)

    if (n_length == 1 and p_length == 0) or (n_length == 0 and p_length == 0):
        return str(0)

    ans = 1
    for n in p_array:
        ans *= n

    if n_length % 2 == 1:
        n_array.remove(max(n_array))

    for n in n_array:
        ans *= n

    return str(ans)

xs = [2, 0, 2, 2, 0]
print(solution(xs))
xs = [-2, -3, 4, -5]
print(solution(xs))
