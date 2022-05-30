Select employee_id  From employees where employee_id not in (Select employee_id from salaries)
Union
Select employee_id  From salaries where employee_id not in (Select employee_id from employees)
order by employee_id asc