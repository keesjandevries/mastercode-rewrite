import sqlite3


#def initialise_table(filename,table):
#    conn=sqlite3.connect(filename)
#    with conn:
#        cur=conn.cursor()


def store_point_to_table(chi2,obs,table,filename):
    conn=sqlite3.connect(filename)

    #with automatically closes the connnection
    with conn:
        #FIXME: this can be done more effictiently, initialising only once!
        #WARINING: this storage is dependent on how the predictions are parsed
        chi2_data_type     ="chi2 DOUBLE"
        slha_data_type_list=" DOUBLE, ".join(["_".join([first,block,comment]) for (first,(block,comment)), val in obs.items() if first == 'slha'])
        pred_data_type_list=" DOUBLE, ".join(["_".join([first,second]) for (first, second), val in obs.items() if not first == 'slha'  ] )
        name_data_type_list=", ".join([chi2_data_type,slha_data_type_list,pred_data_type_list])
        print(name_data_type_list)
        cur.execute("CREATE TABLE IF NOT EXISTS %s(%s)",(table,name_data_type_list))
        fill_q_marks="?, "*(len(obs)+1)
        #FIXME: this is probably slow!!
        cur.execute(("INSERT INTO %s VALUES(%s)", (table,fill_q_marks) ),tuple([chi2]+list(obs)))


 
