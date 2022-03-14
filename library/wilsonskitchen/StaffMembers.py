from Table import Table
from constants import LOGGER


class StaffMembers(Table):
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)
        self._username = 1111

    def reset_staffmembers_table(self) -> None:
        try:
            # calls recreate_table 
            # to execute sql
            sql = """CREATE TABLE StaffMembers
                    (StaffID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Email TEXT,
                    Firstname TEXT,
                    Surname TEXT,
                    JobTitle TEXT,
                    AccessLevel INTEGER,
                    Username INTEGER,
                    Password)"""
            self.recreate_table(sql)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("StaffMembers table could not be reset.") from err

    def add_member(self, email, fname, sname, job, accesslevel, password) -> int:
        try:
            # generates new username
            # calls insert_record 
            # to execute sql with values
            # returns username
            staffmembers = self.get_staffmembers()
            if staffmembers == []:
                username = self._username
            else:
                prevusername = staffmembers[len(staffmembers)-1][6]
                username = prevusername + 1
            values = (email, fname, sname, job, accesslevel, username, password)
            sql = """INSERT 
                    INTO StaffMembers 
                    (Email, Firstname, Surname, JobTitle, AccessLevel, Username, Password) 
                    VALUES (?, ?, ?, ?, ?, ?, ?)"""
            self.insert_record(sql, values)
            return username
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Staff member could not be added.") from err

    def get_staffmembers(self) -> tuple:
        try:
            # calls select
            # to execute sql
            # returns records
            sql = """SELECT * 
                    FROM StaffMembers
                    ORDER BY Firstname ASC"""
            return self.select(sql)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Staff members could not be found.") from err

    def delete_member(self, email) -> None:
        try:
            # calls delete_record
            # to execute sql with email
            sql = """DELETE 
                    FROM StaffMembers 
                    WHERE Email=?"""
            self.delete_record(sql, (email,))
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Staff member could not be deleted.") from err

    def update_ownaccount(self, username, email, fname, sname, password) -> None:
        try:
            # calls update
            # to execute sql with values
            values = (email, fname, sname, password, username)
            sql = """UPDATE StaffMembers 
                    SET Email=?, Firstname=?, Surname=?, Password=? 
                    WHERE Username=?"""
            self.update(sql, values)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Staff member could not be updated.") from err

    def update_member(self, oldemail, email, fname, sname, job, access, password) -> None:
        try:
            # calls update
            # to execute sql with values
            values = (email, fname, sname, job, access, password, oldemail)
            sql = """UPDATE StaffMembers 
                    SET Email=?, Firstname=?, Surname=?, JobTitle=?, AccessLevel=?, Password=? 
                    WHERE Email=?"""
            self.update(sql, values)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Staff member could not be updated.") from err

    def check_login(self, username, password) -> list:
        try:
            # checks if username and password exist and match
            values = (username, password)
            sql = """SELECT AccessLevel 
                    FROM StaffMembers 
                    WHERE Username=? AND Password=?"""
            # calls select_dataspecific_fetchone
            # to execute sql with values
            accesstuple = self.select_dataspecific_fetchone(sql, values)
            if accesstuple == None:
                sql = """SELECT Password 
                        FROM StaffMembers 
                        WHERE Username=?"""
                # calls select_dataspecific_fetchone
                # to execute sql with username
                passwordtuple = self.select_dataspecific_fetchone(sql, (username,))
            # return list [a, b]:
                # where a = whether the login details are valid or not 
                # and b = status of the invalid login or access level of the valid login
                if passwordtuple == None:
                    return [False, "neither"]
                else:
                    password = passwordtuple[0]
                    return [False, password]
            else:
                access = accesstuple[0]
                return [True, access]
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Staff member login could not be checked.") from err
