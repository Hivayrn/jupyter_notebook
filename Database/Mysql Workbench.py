{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "69d5906c-f25f-4fae-80dc-a4eca384be7f",
   "metadata": {},
   "source": [
    "# MySQL Workbench "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2a51f9f6-611e-4987-8a8d-d9d5b7586510",
   "metadata": {},
   "source": [
    "**1. Create Database**\n",
    "\n",
    "    CREATE DATABASE file_name;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7f298529-d8f8-4495-a981-5830c210b218",
   "metadata": {},
   "source": [
    "**2. Drop Database**\n",
    "\n",
    "    DROP DATABASE file_name;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c60777d8-69a9-40d6-adda-b3ccdf8c211c",
   "metadata": {},
   "source": [
    "**3. Use a Database**\n",
    "\n",
    "    --use a specific Database"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "035e42e6-6fd1-473b-a955-aca9f1d7cde3",
   "metadata": {},
   "source": [
    "**4. Create a Table**\n",
    "\n",
    "    CREATE TABLE table_name (\n",
    "        column 1 data_type,\n",
    "        column 2 data_type,\n",
    "        column 3 data_type\n",
    "        );"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "01842309-a596-4020-95e6-3806c2d470b8",
   "metadata": {},
   "source": [
    "**5. Insert Data In Table**\n",
    "\n",
    "    INSERT INTO table_name;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "86e9d8ee-e116-426a-80a5-10b8b7cbe155",
   "metadata": {},
   "source": [
    "**6. Make a Comment**\n",
    "\n",
    "    --This is a Comment"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0da40986-c0c7-47a8-851f-5cd26e3fd955",
   "metadata": {},
   "source": [
    "**7. Add/ Drop & Alter Columns**\n",
    "\n",
    "    ALTER TABLE table_name\n",
    "    ADD column_name data_type;\n",
    "    DROP column_name;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ad73a452-fa8b-4cf6-9520-765e153056e3",
   "metadata": {},
   "source": [
    "**8. Show Tables**\n",
    "\n",
    "    SHOW TABLES;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a59cae75-80b9-431a-85ba-e57786da0b64",
   "metadata": {},
   "source": [
    "**9. Insert Record**\n",
    "\n",
    "    INSERT INTO table_name (column 1, column 2,column 3)\n",
    "    VALUES (value 1, value 2, value 3 now());"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0ac5055c-fa80-44dc-bfe2-68aeb6cfc2b2",
   "metadata": {},
   "source": [
    "**10. Insert Multiple Records**\n",
    "\n",
    "    INSERT INTO table_name (column 1, column 2, column 3)\n",
    "    VALEUES (value 1, value 2, value 3 now()), ( value 4, value 5, value 6 now()), (value 7, value 8, value 9 now());"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "244282c9-ba05-41a5-bb3f-ecbe0ee760d8",
   "metadata": {},
   "source": [
    "**11. Select Table**\n",
    "\n",
    "    SELECT * FROM table_name;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5ade288d-134f-45a4-a894-402ec4127a20",
   "metadata": {},
   "source": [
    "**12. Select Columns**\n",
    "\n",
    "    SELECT * FROM table_name;\n",
    "    SELECT column 1 FROM table_name;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eead43cd-2d6d-4ecf-8da1-aea1be5cccbc",
   "metadata": {},
   "source": [
    "**13. Drop Exists Table**\n",
    "\n",
    "    DROP DATABADSE IF EXISTS table_name;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f13e35b0-5c57-4f34-aa37-22e0f4443a38",
   "metadata": {},
   "source": [
    "**14. Where Condition**\n",
    "\n",
    "    SELECT * FROM INFO\n",
    "    WHERE column_name condition;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "91250908-8497-4c1c-b152-cc3ee61decbc",
   "metadata": {},
   "source": [
    "**15. Order By (Sort)**\n",
    "\n",
    "    SELECT * FROM INFO\n",
    "    ORDER BY column_name DESC/ ASC;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e3ad7920-90ef-475e-8a45-84e9eb9b03eb",
   "metadata": {},
   "source": [
    "**16. Select Operation:** \n",
    " *It can perform mathematical operation on a specific column and entry its information in a new column that it creates.*\n",
    "\n",
    "  Example:\n",
    "  \n",
    "      SELECT first_name,\n",
    "             last_name,\n",
    "             score * 10 AS final;\n",
    "\n",
    "$$point:$$ Here we say that it will score * 10 and it will save the information in the score * 10  column.\n",
    "If you want to change the column name, you should use AS. Here we want to replace the final column instead of score * 10.  "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f6298b7c-a4eb-4858-83ae-4117880a6d28",
   "metadata": {},
   "source": [
    "**17. Delete Record**\n",
    "\n",
    "    DELETE FROM table_name WHERE column_name (your condition);"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ba5c713d-b1af-4fc9-be66-e266815f0904",
   "metadata": {},
   "source": [
    "**18. Modify Column**\n",
    "\n",
    "    ALTER TABLE table_name MODIFY CLOUMN column_name data_type;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0218a33d-4eff-4e53-b1af-36fb1ca66145",
   "metadata": {},
   "source": [
    "**19. Concat**\n",
    "\n",
    "    SELECT CONCAT ('word 1', ' ', 'word 2') AS new_column_name, dept FROM table_name;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c6b9d63a-a2ac-447f-b061-1c7f597a4e23",
   "metadata": {},
   "source": [
    "**20. Functions In DB:**  *Count, Sum, Avg, Combine*\n",
    "\n",
    "$$1.COUNT$$\n",
    "\n",
    "*1. View all values EVEN duplicate values:*\n",
    "\n",
    "    SELECT COUNT (*) FROM table_name;\n",
    "    \n",
    "*2. View non-null values in a column:*\n",
    "\n",
    "    SELECT COUNT (column_name) FROM table_name;\n",
    "\n",
    "*3. Composition Count & Distinct:*\n",
    "\n",
    "    SELECT COUNT (DISTINCT (column_name)) FROM table_name;\n",
    "\n",
    "$$point:$$\n",
    "\n",
    "$$In this section, null values are not counted,$$\n",
    "$$And duplicate data is counted once!!$$"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "57c80ae5-06ab-42e4-9a15-fe3715103fe2",
   "metadata": {},
   "source": [
    "$$2. SUM$$\n",
    "\n",
    "*1. Toal column:*\n",
    "\n",
    "    SELECT SUM (column_name) FROM table_name;\n",
    "\n",
    "*2. Choose a new name for the SUM column:*\n",
    "\n",
    "    SELECT SUM (column_name) AS new_name FROM table_name;\n",
    "\n",
    "*3. Condition for sum:*\n",
    "\n",
    "    SELECT SUM (column_name) FROM table_name\n",
    "    WHERE condition;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "511d5b4a-7e00-4177-87db-7d3306a44517",
   "metadata": {},
   "source": [
    "$$3. AVG$$\n",
    "\n",
    "*AVG:*\n",
    "\n",
    "    SELECT AVG (column_name) FROM tanle_name;\n",
    "\n",
    "*Example:*\n",
    "\n",
    "    SELECT customer FROM orders\n",
    "    WHERE orderprice > (SELECT AVG (orderprice) FROM orders);"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cdd18429-6db0-4a02-9c9e-409225145f94",
   "metadata": {},
   "source": [
    "$$4. COMBINE$$\n",
    "\n",
    "**Combine:** *It unites 2 queries, and we can see the result 2 tables in one.*\n",
    "\n",
    "    SELECT column 1, column 2, ...\n",
    "    FROM table_name 1\n",
    "    UNION\n",
    "    SELECT column 1, column 2, ...\n",
    "    FROM table_name 2;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8c71b62e-b635-43d6-91df-0dec5f57a07c",
   "metadata": {},
   "source": [
    "$$Other Functions$$\n",
    "\n",
    "**21. Length:** *Show the length of a string.*\n",
    "\n",
    "    SELECT LENGTH ('STRING') AS lengthofstring;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e7fa9321-b1cc-4f58-b03d-a410d86ff246",
   "metadata": {},
   "source": [
    "**22. Lcase:** *Lower case characters of a string.*\n",
    "\n",
    "    SELECT LCASE ('STRING') AS lowercasetext;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "416915d5-12e8-4fbf-bb8e-2cac4b0c35ee",
   "metadata": {},
   "source": [
    "**23. Ucase:** *Upper case characters of a string.*\n",
    "\n",
    "    SELECT UCASE ('STRING') AS uppercasetext;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "436abfca-7e5d-4bc9-a243-de4554679ca8",
   "metadata": {},
   "source": [
    "$$Question:$$\n",
    "\n",
    "*How can we make sure, we haven't entered duplicate record information?*\n",
    "\n",
    "    INSERT INTO table_name 1\n",
    "        (table_name 1- column 1, table_name 1- column 2, ...)\n",
    "    SELECT table_name 2- column 1 AS table_name 1- column 1, ...\n",
    "    FROM table_name 2\n",
    "    WHERE NOT EXISTS (SELECT * FROM table_name 1\n",
    "                      WHERE table_name 1. column 1 = table_name 2. column 2;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a0c2b510-81c8-491d-8540-70065a3e9a46",
   "metadata": {},
   "source": [
    "**24. Between (Select Range)**\n",
    "\n",
    "    SELECT * FROM table_name WHERE column_name BETWEEN value1 AND value2;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f77b6735-cb95-4752-a73a-6e9ebb1d07ea",
   "metadata": {},
   "source": [
    "$$Examples:$$\n",
    "\n",
    "**25. New Table With Foreign Key (Posts)**\n",
    "\n",
    "    CREATE TABLE posts (\n",
    "        user_id INT,\n",
    "        title VARCHAR(20),\n",
    "        publish_date DATETIME DEFAULT CURRENT_TIMESTAMP,\n",
    "        PRIMARY KEY (id),\n",
    "        FOREIGN KEY (user_id) REFRENCES users(id)\n",
    "    );"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9d64f301-c886-4396-a4e4-ee192d760fa4",
   "metadata": {},
   "source": [
    "**26. New Table With 2 Foriegn Keys**\n",
    "\n",
    "    CREATE TABLE comments (\n",
    "        id INT AUTO_INCREMENT,\n",
    "        post_id INT,\n",
    "        user_id INT,\n",
    "        publish_date DATETIME DEFAULT CURRENT_TIMESTAMP,\n",
    "        PRIMARY KEY (id),\n",
    "        FOREIGN KEY (user_id) REFRENCES users(id),\n",
    "        FOREIGN KEY (post_id) REFRENCES posts(id)\n",
    "    );"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4e397e98-3f5a-4683-95b1-054eaf21306f",
   "metadata": {},
   "source": [
    "**27. Aggregate Functions**\n",
    "\n",
    "     SELECT COUNT(id) FROM users,\n",
    "     SELECT MAX(age) FROM users;\n",
    "     SELECT MIN(age) FROM users;\n",
    "     SELECT SUM(age) FROM users;\n",
    "     SELECT UCASE(first_name), LCASE(last_name) FROM users;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d3b5523d-6b4e-469f-b0e1-b37866688f93",
   "metadata": {},
   "source": [
    "**28. Group By**\n",
    "\n",
    "     SELECT age, COUNT(age) FROM users GROUP BY age;\n",
    "     SELECT age, COUNT(age) FROM users WHERE age > 20 GROUP BY age;\n",
    "     SELECT age, COUNT(age) FROM users GROUP BY age HAVING count(age) >= 2;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "91c3618e-5bfc-4f5e-8ac4-98e4700530ef",
   "metadata": {},
   "source": [
    "**29. Like (Searching)**\n",
    "\n",
    "    SELECT * FROM users WHERE dept LIKE 'd%';\n",
    "    SELECT * FROM users WHERE dept LIKE 'dev%';\n",
    "    SELECT * FROM users WHERE dept LIKE '%t';\n",
    "    SELECT * FROM users WHERE dept LIKE '%e%';"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c6398cf4-d70f-4d85-b5f1-c564f31f3577",
   "metadata": {},
   "source": [
    "**30. Not Like**\n",
    "\n",
    "    SELECT * FROM users WHERE dept NOT LIKE 'd%';"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f3691f4b-79ab-47f4-892f-c27a63bd278b",
   "metadata": {},
   "source": [
    "**31. Create & Remove Index**\n",
    "\n",
    "$$CREATE$$\n",
    "     CREATE INDEX LIndex ON users(location);\n",
    "\n",
    "$$DROP$$\n",
    "     DROP INDEX LIndex ON users;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "815b009d-c4b9-4aff-9882-cc851ba26a64",
   "metadata": {},
   "source": [
    "**32. Locate (Position)**\n",
    "\n",
    "    SELECT column1, POSITION ('X' IN column2)\n",
    "    FROM table_name;"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
