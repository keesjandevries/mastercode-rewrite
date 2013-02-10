import sqlite3


#def initialise_table(filename,table):
#    conn=sqlite3.connect(filename)
#    with conn:
#        cur=conn.cursor()


def store_point_to_table(chi2,obs,table,filename):
    conn=sqlite3.connect(filename)

    #with automatically closes the connnection
    with conn:
        try:
            cur=conn.cursor()
            #FIXME: this can be done more effictiently, initialising only once!
            if obs:
                # FIXME: stupid way of doing this: collumn names are now again vars0 ... varN
                name_data_type_list=" DOUBLE, ".join(["vars"+str(i) for i in range(len(obs)+1) ])
                command="CREATE TABLE IF NOT EXISTS {0}({1})".format(table,name_data_type_list)
                cur.execute(command)

                fill_q_marks=", ".join([ "?" for i in range(len(obs)+1)])
                #FIXME: this is probably slow!!
                command="INSERT INTO {0} VALUES({1})".format(table,fill_q_marks)
                cur.execute( command,tuple([chi2]+list(obs.values())))
        except sqlite3.Error as e:
            if conn:
                conn.rollback()
            print("ERROR in sqlite: ",e.args[0])



 
