print("""
                                    　今天訂哪一家便當　查詢器
                             
                                               星期代碼:
                             
                             * 星期一: 1      * 星期二: 2     * 星期三: 3
                             * 星期四: 4      * 星期五: 5     * 星期六: 6                            """)

day = dict([["1", "星期一"],
            ["2", "星期二"],
            ["3", "星期三"],
            ["4", "星期四"], 
            ["5", "星期五"], 
            ["6", "星期六"]])
print("")
inum = input("星期代碼(1~6): ")
print("")
lunch = dict([["1", "嗎哪"],
              ["2", "粵園"],
              ["3", "如意"],
              ["4", "餅天下"],
              ["5", "金林排骨"],
              ["6", "回家吃自己"]])
print("")
print("今天", day[inum], "訂", lunch[inum]) 
