from sqlite3 import connect
import os
import json


#::::::::::::::::::::::::::;;;
#::::::::::::::::::::::::::;;;
#::::::::::::::::::::::::::;;;

class data_base():

      def __init__(self):

            self.title = 'data_base'
            self.path = str(os.getcwd())
            self.name = 'data_base.sqlite3'
            self.data_path = self.path + '\\'  + self.name

            #connect

            self.dat = connect(self.data_path)
            self.mang = self.dat.cursor()


            cmd = f"""CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT,
                      admin TEXT,
                      sokot_all TEXT,
                      mutes TEXT,
                      antilink TEXT,
                      block_msg TEXT)"""
            
            self.mang.execute(cmd)
            self.dat.commit()

            cmd = f"""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT,
                      chat_id TEXT,
                      info TEXT,
                      warnings INTEGER)"""
            
            self.mang.execute(cmd)
            self.dat.commit()

            

      #grups data::::::::::::::::::::::::::::::::::::::::::::

      def mute(self, name, chat_id):

            self.mang.execute("SELECT mutes FROM data WHERE name = ?", (str(name),))
            mute = self.mang.fetchone()[0]
            #print(mute)

            #('["406235036"]',)
            #('',)

            #print(mute)

            try:

      
                datas = json.loads(mute)

            except:

                  datas = []

            

            

            

            datas.append(str(chat_id))


            datas = list(set(datas))

            #print(datas)

            datas = json.dumps(datas)

            self.update_item(name, 'mutes', datas)



            
      def unmute(self, name, chat_id):

            self.mang.execute("SELECT mutes FROM data WHERE name = ?", (str(name),))
            mute = self.mang.fetchone()[0]
            

            try:

                  try:

                      datas = json.loads(mute)

                  except:

                        datas = []

                  try:
                        datas.remove(str(chat_id))
                        datas = list(set(datas))
                        datas = json.dumps(datas)
                        self.update_item(name, 'mutes', datas)

                        return 'done'

                  except:

                        return 'not found'

            except:

                  return 'not found'
      

      def add_group(self, group, admin):

            cmd = f"INSERT INTO data (name, admin, sokot_all, mutes, antilink, block_msg) VALUES(?, ?, ?, ?, ?, ?)"

            self.mang.execute(cmd, (str(group), str(admin), 'False', '', 'False', ''))

            self.dat.commit()
            



      def update_item(self, group, item, data):

            cmd = f"UPDATE data SET {item} = ? WHERE name = ? "

            self.mang.execute(cmd, (str(data), str(group)))
            self.dat.commit()

      def get_group_info(self, group):

            cmd = f"SELECT * FROM data WHERE name = ?"

            self.mang.execute(cmd, (str(group), ))
            dt = self.mang.fetchall()

            nones = [None, [], (), '']

            if dt not in nones:

                  return dt

            else:

                  return None


      #USERS DATA :::::::::::::::::::::::::::::::::::

      def add_user(self, name, chat_id):

            self.mang.execute(f"INSERT INTO users (name, chat_id, info, warnings) VALUES(?, ?, ?, ?)",
                              (str(name), str(chat_id), '', 0))
            self.dat.commit()

      def get_user_info(self, name, chat_id):

            self.mang.execute("SELECT * FROM users WHERE name = ? AND chat_id = ?", (str(name), str(chat_id)))
            data = self.mang.fetchone()

            nones = [None, [], (), '']

            if data not in nones:

                  return data

            else:
                  return 'not found'

      def update_user(self, name, chat_id, column, data):

            self.mang.execute(f"UPDATE users SET {column} = ? WHERE name = ? AND chat_id = ?",
                              (data, str(name), str(chat_id)))
            self.dat.commit()

            

            



























      
            
