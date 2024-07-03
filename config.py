import sqlite3
# connection = sqlite3.connect('assist.db')

# connection.execute('''
#     CREATE TABLE IF NOT EXISTS cmd_open (
#         cmd_open TEXT
#     )
# ''')
# connection.execute('''
#     CREATE TABLE IF NOT EXISTS cmd_joke (
#         cmd_joke TEXT
#     )
# ''')
# connection.execute('''
#     CREATE TABLE IF NOT EXISTS cmd_browser (
#         cmd_browser TEXT
#     )
# ''')
# connection.execute('''
#     CREATE TABLE IF NOT EXISTS new_joke (
#         new_joke TEXT
#     )
# ''')
# connection.execute('''
#     CREATE TABLE IF NOT EXISTS names (
#         names TEXT
#     )
# ''')

# connection.commit()
# connection.close()

# cursor.execute('INSERT INTO cmd_list (cmd_clock, cmd_joke, cmd_browser, new_jokes, names) VALUES (?, ?, ?, ?, ?)', ("который час", "пошути", "открой браузер", "новый анекдот", "дубина"))

# connect = sqlite3.connect('assist.db')
# cursor = connect.cursor()

# cursor.execute('INSERT INTO cmd_clock (cmd_clock) VALUES (?)', ("время",))
# cursor.execute('INSERT INTO cmd_joke (cmd_joke) VALUES (?)', ("пошути",))
# cursor.execute('INSERT INTO cmd_browser (cmd_browser) VALUES (?)', ("браузер",))
# cursor.execute('INSERT INTO new_joke (new_joke) VALUES (?)', ("анекдот",))
# cursor.execute('INSERT INTO cmd_open (cmd_open) VALUES (?)', ("открой",))

# connect.commit()
# cursor.close()

# VA_EXEC_CMD = 'новая команда'
# VA_NEW_CMDS = ['часы', 'шутки', 'браузер', 'анекдот', 'имя']

def db_name():
    connect = sqlite3.connect('assist.db')
    cursor = connect.cursor()
    
    cursor.execute('SELECT * FROM names')
    cmds = cursor.fetchall()
    
    names = []
    
    for row in cmds:
        names.append(row[0])
    
    cursor.close()
    return names

def db_command(tab: str):
    connect = sqlite3.connect('assist.db')
    cursor = connect.cursor()
    
    cursor.execute(f'SELECT * FROM {tab}')
    cmds = cursor.fetchall()
    
    cmds_1 = []
    
    for row in cmds:
        cmds_1.append(row[0])
    
    connect.close()
    return cmds_1
        
def db_commands():
    
    VA_CMD_LIST = {
        "ctime": db_command('cmd_clock'),
        "joke": db_command('cmd_joke'),
        "open": db_command('cmd_open'),
        "new_joke": db_command('new_joke'),
        "thanks": db_command('thanks')
    }
    
        
    return VA_CMD_LIST