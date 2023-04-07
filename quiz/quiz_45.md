![Screen Shot 2023-03-25 at 17 16 08](https://user-images.githubusercontent.com/112072887/227705887-4500ea3a-dbda-42fe-82bc-ee3a8b576596.png)
```.py
SELECT count(account_id) from transactions group by account_id
SELECT sum(amount) from transactions  where transaction_type = "deposit"  group by  account_id - (select sum(amount) from transactions  where transaction_type = "withdraw"  group by  account_id);

ALTER TABLE transactions
ADD deposit integer;
ALTER TABLE transactions
ADD withdraw integer;


select x.dep-y.wit from (select count(amount), sum(amount) as dep, account_id from transactions where transaction_type like "d%" group by account_id) as x left join  (select count(amount), sum(amount) as wit, account_id from transactions where transaction_type like "w%" group by account_id) as y on x.account_id == y.account_id;
select balance from accounts group by account_id;

select account_id from accounts where x.dep-y.wit  == balance

```




![Screen Shot 2023-04-07 at 15 22 04](https://user-images.githubusercontent.com/112072887/230559775-aa7a207d-f5af-478f-96df-7de20077616e.png)
from this table when can observe that customers where  account_id == 12 or 13 or 15 or 17 or 19 have unbalance since the difference between the amount deposited and withdarwed are different
