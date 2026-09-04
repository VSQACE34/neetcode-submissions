SELECT p.first_name, p.last_name, a.city, a.state FROM address a 
RIGHT JOIN person p ON a.person_id = p.person_id;