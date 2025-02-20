from command import cli
from util import output
                    # problem with negative h(n) https://stackoverflow.com/questions/30067813/are-heuristic-functions-that-produce-negative-values-inadmissible
                    #           Uninformed                                           Informed    
                    # BFS           DLS             GBFS1_v0(-)                GBFS1_v1 (1/)                       GBFS2_v0(-)                                 GBFS2_v1_v2(1/a - b)           A* [ negative h(n) -> causing problem]          A* [ g(n) and possitive h(n) -> still causing problem ]
# grid1 = data1()     #                               OK                                   [ out of memory ]             OK                                        OK [ faster ]                           [ out of memory ]                         [ out of memory ]
# grid2 = data2()     # OK                            OK                                OK                               OK                                        OK                                   OK                                        OK
# grid3 = data3()     # OK            OK              OK                                OK                               OK                                        OK                                   OK                                        OK
# grid4 = data4()     # OK                            OK                                OK                               OK                                        OK                                   OK                                        OK
# grid5 = data5()     # OK            OK              OK                                OK                               OK                                        OK                                   OK                                        OK
# grid6 = data6()     #                                                                 OK                               OK                                        OK                                   OK                                        OK
# grid7 = data7()     #                                                                                                  OK                                        OK                                   OK [ long time ]                          OK [ out of memory ]
# grid8 = data8()     # OK            OK              OK                                OK                               OK                                        OK                                   OK                                           [ out of memory ]
# grid9 = data9()     # OK                            OK                                OK                               OK                                        OK                                   OK                                        OK [ out of memory ]
# grid10 = data10()   #               OK              OK                                OK                               OK                                        OK                                   OK                                        OK
# grid12 = data12()   #                               OK                                OK                               OK                                        OK                                   OK                                        OK [ out of memory ]
# grid13 = data13()   #                               OK                                OK [ long time]                  OK [ faster and better solution ]         OK [ faster and better solution ]    OK [ longer but better solution]          OK [ out of memory ]
# real puzzles       from https://www.puzzle-pipes.com/
# grid11 = data11()   #                               OK []                             OK                               OK [ faster ]                             OK                                      [ out of memory ]                         [ out of memory ]
# grid14 = data14()   #                               OK                                OK                               OK [ faster ]                             OK                                   OK [ out of memory ]                         [ out of memory ]
# grid15 = data15()   #                               OK [ long time]                   OK [ faster time ]               OK [ faster and better solution ]         OK [ faster and better solution ]       [ out of memory ]                         [ out of memory ]
# grid16 = data16()   #                               OK                                OK                               OK [ faster ]                             OK                                   OK                                           [ out of memory ]
# grid17 = data17()   #                               OK [ better solution]             OK [ better solution]            OK                                        OK                                   OK                                           [ out of memory ]


if __name__ == '__main__':
    try:
        cli()
    except Exception as e:
        output.print(f'Searching Error: [red]{str(e)}[/red] :x:')