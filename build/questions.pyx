import sqlite3

def question_n3():
    with sqlite3.connect('souko.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT nihongo,kanji,chinese FROM n3 ORDER BY RANDOM() limit 1')
        for row in cur.fetchall():
            global nihongo, kanji, chinese
            nihongo = row[0]
            kanji = row[1]
            chinese = row[2]
        return nihongo

def question_n4():
    with sqlite3.connect('souko.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT nihongo,kanji,chinese FROM n4 ORDER BY RANDOM() limit 1')
        for row in cur.fetchall():
            global nihongo, kanji, chinese
            nihongo = row[0]
            kanji = row[1]
            chinese = row[2]
        return nihongo
		
def question_n5():
    with sqlite3.connect('souko.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT nihongo,kanji,chinese FROM n5 ORDER BY RANDOM() limit 1')
        for row in cur.fetchall():
            global nihongo, kanji, chinese
            nihongo = row[0]
            kanji = row[1]
            chinese = row[2]
        return nihongo