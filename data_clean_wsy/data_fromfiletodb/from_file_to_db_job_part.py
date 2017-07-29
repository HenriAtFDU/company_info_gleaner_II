# -*- coding:utf-8 -*-
import pymysql
import traceback
import datetime

#PREPARE CONNECTION WITH DATABASE UP THERE IN CLOUD
source_mysql_host="rm-bp1tp2w15f1qlap94.mysql.rds.aliyuncs.com"
source_mysql_db="buz_source_data"
source_mysql_user="root"
source_mysql_passwd="u8!7-ZXC"
conn = pymysql.connect(host=source_mysql_host, user=source_mysql_user, passwd=source_mysql_passwd, db=source_mysql_db, charset='utf8')
cursor = conn.cursor(pymysql.cursors.DictCursor)


# READ FILE & SEND THE DATA TO CLOUD
myfile = open('liepinhistoire_data196_.csv','r')
allWords = []
line = myfile.readline()
while line:
    list = line.split('|')
    for word in list:
#        if word[-1] == '\n':
        allWords.append(word.strip('\n'))
#       else:
#            allWords.append(word)
    print(len(allWords))

    sql = "insert into lp_info_job_part(lp_job_id, lp_co_nm, lp_job_pub_nm, lp_job_pub_pos, lp_job_apply_check_rate, lp_job_apply_check_dur, lp_job_nm, lp_job_salary, lp_job_apply_fdbk, lp_job_add, lp_job_pub_time, lp_job_quals, lp_job_descr, lp_job_dept, lp_job_major, lp_job_boss, lp_job_subordinate, lp_update_datetime) values ('{0}', '{1}','{2}', '{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}')"

    try:
        print("++++++++++++++++++++++++++++++++++++")
#       self.cursor.execute(sql.format(lp_job_id, lp_co_nm, lp_co_tag, lp_co_ownership, lp_co_stf_num, lp_co_lk, lp_co_add, lp_job_pub_nm, lp_job_pub_pos, lp_job_apply_check_rate, lp_job_apply_check_dur, lp_job_nm, lp_job_salary, lp_job_apply_fdbk, lp_job_add, lp_job_pub_time, lp_job_quals, lp_job_descr, lp_job_dept, lp_job_major, lp_job_boss, lp_job_subordinate, lp_co_intro, lp_update_datetime))
        cursor.execute(sql.format(allWords[0],allWords[1],allWords[7],allWords[8],allWords[9],allWords[10],allWords[11],allWords[12],allWords[13],allWords[14],allWords[15],allWords[16],allWords[17],allWords[18],allWords[19],allWords[20],allWords[21], allWords[23]))
        conn.commit()
    except:
        traceback.print_exc()


    allWords = []
    line = myfile.readline()
myfile.close()



