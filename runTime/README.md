### Question
- Input: a file with the following content
```
timestamp               PID     action
10:00:01 12/23/2020     1234    start
10:00:03 12/23/2020     5678    start
10:00:06 12/23/2020     4321    start
10:00:11 12/23/2020     1234    pause
10:00:21 12/23/2020     2212    start
10:00:25 12/23/2020     1234    resume
10:00:32 12/23/2020     5678    pause
10:00:51 12/23/2020     2212    exit
10:01:01 12/24/2020     1234    exit
```
- Output: PIDs and and their run time

Note:
1) start -> exit marks the run time of a process
2) time paused (pause -> resume) is not counted into run time
3) disregard processes that never exit

### Thoughts
- All scenerio that can happen:
    - Start -> pause: time = pause - start
    - Start -> exit: time = exit - start
    - Pause -> resume: don't count time
    - Pause -> exit: don't count time
    - Resume -> pause: time = pause - resume
    - Resume -> exit: time = exit - resume
- Imagine there's a timeline array of the process run. Things will work like this
    - Encounter a start: add to the timeline
    - Encounter a pause: caluculate time from start to pause, then remove the start time (as we have done with it). Don't do anything with this pause because we don't count this time.
    - Encounter a resume: add to the timeline
    - Encounter an exit: calculate time from exit to start/resume. Write to output

### Pseudocode
- Keep 2 dictionaries: 1 to record the "current start time", the other for time it has been running
- Read through all lines
    - If time starts or resumes, add the time to current start time.
    - If time pause or exit, calculate the time from this moment to the current start time recorded.
    - If time exit, write to output file.

### BigO
- Go through all the lines once to do add/calculate operation -> O(N)
- 2 dictionaries -> O(2N) -> O(N)