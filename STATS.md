If you use the session-stats plugin, you will end up with many json files (one per each session/day)

It's a good idea to clean up the directory once in a while... but if you don't, you can experiment with all the data points you collected...

I made a [python script](scripts/stats_vis.py) that runs on the stats directory (where those json files are), and combines the data points to an aggregate graph

The resulting graphs may look a bit wonky