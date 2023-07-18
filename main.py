import pandas
import warnings

import json
from pymysql import connect, OperationalError
import os
from string import Template

"""классы и функции для работы с бд"""


class SQLProvider:
    def __init__(self, file_path: str) -> None:
        self._scripts = {}
        for file in os.listdir(file_path):  # file_path - путь до папки sql
            self._scripts[file] = Template(
                open(f'{file_path}/{file}', 'r').read())

    def get(self, name, **kwargs):  # get('avto_by_lift.sql', lift=...
        return self._scripts[name].substitute(**kwargs)


class DBConnection:
    def __init__(self, config):
        self.config = config
        self.connection = None
        self.cursor = None

    def __enter__(self):
        try:
            self.connection = connect(**self.config)
            self.cursor = self.connection.cursor()
            return self.cursor
        except OperationalError:
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection is not None and self.cursor is not None:
            self.connection.commit()
            self.connection.close()
            self.cursor.close()
        if exc_val is not None:
            print(exc_type)
            print(exc_val.args)
        return True


def work_with_db(config, sql) -> list:
    result = []
    with DBConnection(config) as cursor:
        cursor.execute(sql)
        schema = [column[0] for column in cursor.description]
        for item in cursor.fetchall():
            result.append(dict(zip(schema, item)))
    return result


def db_update(config: dict, _sql):
    with DBConnection(config) as cursor:
        if cursor is None:
            raise ValueError('Курсор None')
        elif cursor:
            cursor.execute(_sql)


"""классы и функции для работы с бд"""

"""Основная прога"""


def pars_temp(temp):
    endStr=len(temp)
    for i in range(1,len(temp)):
        if temp[i].isdigit():
            None
        else:
            endStr=i
            break
    return temp[:endStr]


provider = SQLProvider(os.path.join(os.path.dirname('main.  py'), 'sql'))

conf = json.load(open('configs/sql_config.json'))

'''чтобы консоль за чтение xlsx не выебывалась'''
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=UserWarning)
    df = pandas.read_excel('ТO30_2023_00-2.xlsx')
    rows = len(df.axes[0])
    cols = len(df.axes[1])
    columns = ['m_k', 'theme_contaract', 'customer', 'plan_count_sample', 'intensity_plan', 'rubbish1',
               'intensity_fact', 'kind_test', 'temperature', 'material', 'tester', 'count_tested_samples', 'rubbish2',
               'rubbish3', 'recieve_sample_date_plan', 'recieve_sample_date_fact', 'tester_recierve_sample_date',
               'rubbish4', 'test_end_date', 'rubbish5', 'rubbish6', 'protocol', 'report_date,status', 'rubbish7',
               'rubbish8', 'rubbish9', 'rubbish10', 'rubbish11', 'rubbish12', 'rubbish13', 'granta_mi_flag',
               'granta_mi_text', 'rubbish14', 'transfer_act', 'rubbish15', 'rubbish16', 'rubbish17', 'comment',
               'rubbish18', 'machine_list', 'rubbish18', 'rubbish19', 'rubbish20']

    for i in range(3, 6):
        count_col = 0
        for j in range(cols - 4):
            if count_col == 0:      #m_k+
                loc = df.iloc[i]
                if (isinstance(loc[j], str)):
                    columns[count_col] = loc[j]
                    # print(columns[count_col])
                else:
                    columns[count_col] = None
            if count_col == 1:      #theme+
                if (isinstance(loc[j], str)):
                    columns[count_col] = loc[j]
                    # print(columns[count_col])
                else:
                    columns[count_col] = None
            if count_col == 2:      #customer+
                loc[j]=str(loc[j])
                if (loc[j]!='nan'):
                    columns[count_col] = loc[j]
                else:
                    columns[count_col] = None
            if count_col == 3:      #plan_count_sample+
                if (isinstance(loc[j], int)):
                    columns[count_col] = loc[j]
                else:
                    columns[count_col] = None
            if count_col == 4:      #instensity_plan+(проверить есть ли float там)
                if (isinstance(loc[j], int)):
                    columns[count_col] = loc[j]
                else:
                    columns[count_col] = None
            if count_col == 5:      #fact_count_sample+
                if (isinstance(loc[j], int)):
                    columns[count_col] = loc[j]
                else:
                    columns[count_col] = None
                # print(columns[count_col])
            if count_col == 6:      #instensity_fact+(так же проверить)
                if (isinstance(loc[j], int)):
                    columns[count_col] = loc[j]
                else:
                    columns[count_col] = None
                # print(columns[count_col])
            if count_col == 7:      #name_test_type+
                if (isinstance(loc[j], str)):
                    columns[count_col] = loc[j]
                else:
                    columns[count_col] = None
                # print(columns[count_col])
            if count_col == 8:      #temperature+
                if (isinstance(loc[j], int)):
                    columns[count_col] = loc[j]
                elif (isinstance(loc[j], str)):
                    columns[count_col] = pars_temp(loc[j])
                else:
                   columns[count_col] = None
                # print(columns[count_col])
            if count_col == 9:      #material+
                if (isinstance(loc[j], str)):
                    columns[count_col] = loc[j]
                else:
                    columns[count_col] = None
                # print(columns[count_col])
            if count_col == 10:     #tester+
                if (isinstance(loc[j], str)):
                    columns[count_col] = loc[j]
                else:
                    columns[count_col] = None
                # print(columns[count_col])
            if count_col == 11:     #count_tested_sample+
                if (isinstance(loc[j], int)):
                    columns[count_col] = loc[j]
                else:
                    columns[count_col] = None
                # print(columns[count_col])
            if count_col == 14:     #receive_sample_date_plan+
                if (isinstance(loc[j], float) or isinstance(loc[j], str)):
                    columns[count_col] = None
                elif (loc[j] != None) and (type(loc[j]) != str):
                    columns[count_col] = str(loc[j])[:10]
                # print(columns[count_col])
            if count_col == 15:     #receive_sample_date_fact+
                if (isinstance(loc[j], float) or isinstance(loc[j], str)):
                    columns[count_col] = None
                elif (loc[j] != None) and (type(loc[j]) != str):
                    columns[count_col] = str(loc[j])[:10]
                # print(columns[count_col])
            if count_col == 16:     #tester_recierve_sample_date+
                if (isinstance(loc[j], float) or isinstance(loc[j], str)):
                    columns[count_col] = None
                elif (loc[j] != None) and (type(loc[j]) != str):
                    columns[count_col] = str(loc[j])[:10]
                # print(columns[count_col])
            if count_col == 19:     #test_end_date+
                if (isinstance(loc[j], float) or isinstance(loc[j], str)):
                    columns[count_col] = None
                elif (loc[j] != None) and (type(loc[j]) != str):
                    columns[count_col] = str(loc[j])[:10]
                else:
                    columns[count_col] = None

                # print(columns[count_col])
            if count_col == 21:     #protocol+
                if (isinstance(loc[j], str)):
                    columns[count_col] = loc[j]
                else:
                    columns[count_col] = None
                # print(columns[count_col])
            if count_col == 22:     #report_date+
                if (isinstance(loc[j], float) or isinstance(loc[j], str)):
                    columns[count_col] = None
                elif (loc[j] != None) and (type(loc[j]) != str):
                    columns[count_col] = str(loc[j])[:10]
                else:
                    columns[count_col] = None
                # print(columns[count_col])
            if count_col == 23:     #status+(либо 23(текущий статус протокола исп1) либо 33(статус протокола)))
                if (isinstance(loc[j], str)):
                    columns[count_col] = loc[j]
                else:
                    columns[count_col] = None
                # print(columns[count_col])
            if count_col == 31:     #granta_mi_flag+
                if (loc[j]=='-'):
                    columns[count_col]=0
                elif (loc[j]=='+'):
                    columns[count_col]=1
                else:
                    columns[count_col] = None
                # print(columns[count_col])
            if count_col == 32:     #granta_mi_text+
                if (isinstance(loc[j], str)):
                    columns[count_col] = loc[j]
                else:
                    columns[count_col] = None
                # print(columns[count_col])
            if count_col == 34:     #transfer_act+
                if (isinstance(loc[j], str)):
                    columns[count_col] = loc[j]
                else:
                    columns[count_col] = None
                # print(columns[count_col])
            if count_col == 38:     #comment+
                if (isinstance(loc[j], str)):
                    columns[count_col] = loc[j]
                else:
                    columns[count_col] = None
                # print(columns[count_col])
            if count_col == 40:     #machine_list+
                if (isinstance(loc[j], str)):
                    columns[count_col] = loc[j]
                else:
                    columns[count_col] = None
                # print(columns[count_col])
            if columns[count_col] is None:
                columns[count_col] = 'NULL'
            else:
                columns[count_col] = '"' + str(columns[count_col]) + '"'
            count_col += 1

        # print('\n**************\n')
        m_k = columns[0]
        theme_contaract = columns[1]
        customer = columns[2]
        plan_count_sample = columns[3]
        intensity_plan = columns[4]
        fact_count_sample = columns[5]
        intensity_fact = columns[6]
        kind_test = columns[7]
        temperature = columns[8]
        material = columns[9]
        transfer_act = columns[34]
        tester = columns[10]
        count_tested_samples = columns[11]
        status = columns[23]
        report_date = columns[22]
        recieve_sample_date_plan = columns[14]
        recieve_sample_date_fact = columns[15]
        tester_recierve_sample_date = columns[16]
        test_end_date = columns[19]
        protocol = columns[21]
        machine_list = columns[40]
        comment = columns[38]
        granta_mi_flag = columns[31]
        granta_mi_text = columns[32]
        e_list = 1
        machine_list = 1

        # staff
        if tester == 'NULL':
            tester = '"Неизвестно"'
        staff_id = work_with_db(conf, provider.get('select_log_staff.sql', fio=tester))
        if len(staff_id) == 0:
            work_with_db(conf, provider.get('insert_staff.sql', fio=tester))
            staff_id = work_with_db(conf, provider.get('select_log_staff.sql', fio=tester))
        staff_id = staff_id[0].get('staff_id')

        # example_list
        if len(work_with_db(conf, provider.get('select_example_list.sql', elist_id=e_list))) == 0:
            work_with_db(conf, provider.get('insert_example_list.sql', elist_id=e_list))

        # machine_list
        if len(work_with_db(conf, provider.get('select_machine_list.sql', list_id=machine_list))) == 0:
            work_with_db(conf, provider.get('insert_machine_list.sql', list_id=machine_list))


        # tests_type
        if kind_test == 'NULL':
            kind_test = '"Неизвестно"'
        type_id = work_with_db(conf, provider.get('select_type_id_tests_type.sql', tname=kind_test))
        if len(type_id) == 0:
            work_with_db(conf, provider.get('insert_tests_types.sql', tname=kind_test))
            type_id = work_with_db(conf, provider.get('select_type_id_tests_type.sql', tname=kind_test))
        type_id = type_id[0].get('type_id')


        # cust
        if customer == 'NULL':
            customer = '"Неизвестно"'
        cust_id = work_with_db(conf, provider.get('select_cust_id_customer.sql', cname=customer))
        if len(cust_id) == 0:
            work_with_db(conf, provider.get('insert_customer.sql', cname=customer))
            cust_id = work_with_db(conf, provider.get('select_cust_id_customer.sql', cname=customer))
        cust_id = cust_id[0].get('cust_id')

        work_with_db(conf, provider.get('insert_order.sql', m_k=m_k, theme_contract=theme_contaract, transfer_act=transfer_act,\
                                        customer=cust_id, plan_count_sample=plan_count_sample, fact_count_sample=fact_count_sample,\
                                        kind_test=type_id, temperature=temperature, material=material, tester=staff_id,\
                                        count_tested_sample=count_tested_samples, status=status, report_date=report_date,\
                                        receive_sample_date_plan=recieve_sample_date_plan, receive_sample_date_fact=recieve_sample_date_fact,\
                                        tester_receive_sample_date=tester_recierve_sample_date, test_end_date=test_end_date, protocol=protocol,\
                                        intensity_plan=intensity_plan, intensity_fact=intensity_fact, machine_list=machine_list,\
                                        comment=comment, granta_mi_flag=granta_mi_flag, granta_mi_text=granta_mi_text, example_list=e_list))

#
# # work_with_db(conf, provider.get('insert_staff.sql', fio="ai", role="t", log="log", pas="pas"))