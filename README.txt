                    Simple menu-driven academic roll system

Default login ->
                                  ID: admin
                                Password: admin

Each user can be either an admin or a student.  Both are presented  a  different
menu to interact. Only admin can add or modify (change password and role) users.
Users of admin role can add/modify grades for students. Grades can't be added to
an admin account but they are preserved when a student account is  converted  to
an admin account.  CPI and SPI are presented along with grades  (SPI  with  each
semester and SPI if grades for all semesters are being viewed). A student can be
allotted different grades for the same course code in different semesters.   The
grade-key followed is:
			AP	10
			AA	10
			AB	09
			BB	08
			BC	07
			CC	06
			CD	05
			DD	04
			FR	00

NOTE: No change is saved implicitly, user must choose save  option  to  save  to
file.  But the program does prompt for confirmation to save/discard when a  exit
is issued with unsaved DB.
