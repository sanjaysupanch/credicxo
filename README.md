# credicxo

<a href="https://credicxoo.herokuapp.com/branches/">List of all branches!</a><br>
<a href="https://credicxoo.herokuapp.com/branches/ABHY0065001/">Filter through IFSC and get branch details !</a><br>
##### Ex : https://credicxoo.herokuapp.com/branches/ifsc/ 
<a href="https://credicxoo.herokuapp.com/bank_branch/">List of bank branches !</a><br>
<a href="https://credicxoo.herokuapp.com/bank_branches/ABHYUDAYA%20COOPERATIVE%20BANK%20LIMITED/MUMBAI/">Filter through bank name and city, gets details of all branches of the bank in the city. !</a><br>
##### Ex: https://credicxoo.herokuapp.com/bank_branch/bank_name/city/

<br/><br/>

<h4>Command to run this project</h4>
Note: In manage.py directory.<br>
<b>$ pip3 install -r requirements.txt</b></br>
<b>$ python3 manage.py runserver</b></br>

bank=# \d banks_1

            Table "public.banks"
 Column |         Type          | Modifiers 
--------+-----------------------+-----------
 name   | character varying(49) | 
 id     | bigint                | not null
Indexes:
    "banks_id_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "branches" CONSTRAINT "branches_banks_fkey" FOREIGN KEY (bank_id) REFERENCES banks(id)

bank=# \d branches

            Table "public.branches"
  Column  |          Type          | Modifiers 
----------+------------------------+-----------
 ifsc     | character varying(11)  | not null
 bank_id  | bigint                 | 
 branch   | character varying(74)  | 
 address  | character varying(195) | 
 city     | character varying(50)  | 
 district | character varying(50)  | 
 state    | character varying(26)  | 
Indexes:
    "branches_ifsc_pkey" PRIMARY KEY, btree (ifsc)
Foreign-key constraints:
    "branches_banks_fkey" FOREIGN KEY (bank_id) REFERENCES banks(id)

bank=# \d bank_branches

          View "public.bank_branches"
  Column   |          Type          | Modifiers 
-----------+------------------------+-----------
 ifsc      | character varying(11)  | 
 bank_id   | bigint                 | 
 branch    | character varying(74)  | 
 address   | character varying(195) | 
 city      | character varying(50)  | 
 district  | character varying(50)  | 
 state     | character varying(26)  | 
 bank_name | character varying(49)  | 

