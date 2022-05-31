-- More practice using case and string manipulations with sql, tired today so will only do 1 problem
Select id,
case when p_id is null then 'Root'
when id in (select distinct p_id from tree) then 'Inner'
else 'Leaf' end as Type
From tree